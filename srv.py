from flask import Flask, render_template, session, copy_current_request_context, current_app
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
from threading import Thread
import random,time

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Letsplaybitball!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


################################ Bitball goes hurr ###########################
# emulate a background_thread that is constantly running creating new exciting events
def background_stuff():
     while True:
        send_msg(str(random.randint(0,10)))
        time.sleep(1)


################################ handle msg sending here
def send_msg(msg):
    with app.app_context():
        msg_package = {'data': msg}
        #print('Sending MSG to Clients: ' + msg)
        emit('my_response', msg_package, namespace='/bitball', broadcast=True)

################################### Flask schtuff

# load the template folder index.html - handle any HTTP/HTML stuff here
# will eventually need some more configurations for hosting
@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)


# define the socket actions. connect/my_event/broadcast_event/disconnect
# this should be the methods called for writing to the screen from the main bitball code.
@socket_.on('connect', namespace='/bitball')
def on_connect():
    print("A Client Connected to the server!!")
    emit('my_response',{'data': 'Connected to Socket Server!'})


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


def start_srv():
    socket_.run(app,debug=True,use_reloader=False)


# running main
if __name__ == '__main__':
    #starting the bitball actions in the background so it will always run - will eventually need to make this safer to run
    x = Thread(target=background_stuff)
    x.start()

    
    # start the flask app for connections
    socket_.run(app,debug=True)
