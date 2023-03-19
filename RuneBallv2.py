#!/usr/bin/env python3
# Welcome to RuneBall!

# init
import pyttsx3
import random
import time
import sqlite3
import argparse
from database import db
from lore import games

def lets_play():
        print("Let's goooooo")

if __name__ == "__main__":
        # get cmdline args and parse them. 
        parser = argparse.ArgumentParser(description='Welcome to RuneBall!')
        parser.add_argument('--no-t2s', dest='t2s', action='store_false')
        args = parser.parse_args()

        # so we can use an arg parser to check and see if a user has access to 
        # text to speech or just give them the option to turn it off. 
        if (args.t2s):
                # enable a flag that will be checked later
                # when deciding wether to send to t2s or not. 
                print("using t2s")
        else:
                # turn off and maybe don't even load the t2s lib. 
                print("disabling text to speech....")

        # let's check the db if it exists and if it's valid. 
        d = db.DatabaseConnection()

        # main game loop - threading for better perf tbd 
        game = games.BallGame()
        game.game_loop()

