#!/usr/bin/env python3
# Welcome to RuneBall!

# init
import pyttsx3
import random
import time
import sqlite3
import argparse

def lets_play():
        print("Let's goooooo")

if __name__ == "__main__":
        # get cmdline args and parse them. 
        parser = argparse.ArgumentParser(description='Welcome to RuneBall!')
        parser.add_argument('--no-t2s', dest='t2s', action='store_false')
        args = parser.parse_args()

        if (args.t2s):
                print("using t2s")
        else:
                print("disabling text to speech....")

        # let's check the db if it exists and if it's valid. 
        

        # main game loop - threading for better perf   


