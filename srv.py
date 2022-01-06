from flask import Flask, render_template, session, copy_current_request_context, current_app
from flask_executor import Executor
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
from threading import Thread
import random,time

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Letsplaybitball!'
socket_ = SocketIO(app, async_mode=async_mode)
executor = Executor(app)
thread = None
thread_lock = Lock()

################################# Bitball goes hurr
def background_stuff():
     print ('In background_stuff')
     while True:
        print('running bitball actions')
        with app.test_request_context('/'):
            print(app.name)
            test_msg = ["sure"]
            test_message(test_msg[0])
        time.sleep(5)

################################### Flask schtuff
@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)

@socket_.on('connect', namespace='/bitball')
def on_connect():
    print("connected server!!")
    emit('my_response',{'data': 'Connected!'})


@socket_.on('my_event', namespace='/bitball')
def test_message(message):
    emit('my_response',{'data': message['data']})


@socket_.on('my_broadcast_event',namespace='/bitball')
def test_broadcast_message(message):
    emit('my_response',{'data': message['data']})


@socket_.on('disconnect_request',namespace='/bitball')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',{'data': 'Disconnected!'},callback=can_disconnect)


# running main
if __name__ == '__main__':
    #starting the bitball actions in the background so it will always run - will eventually need to make this safer to run
    x = Thread(target=background_stuff)
    x.start()
    # start the flask app for connections
    socket_.run(app,debug=True)
