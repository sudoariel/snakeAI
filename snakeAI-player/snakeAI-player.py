#!/bin/sh

# Snake AI player
# Developed by Ariel Lima
# Copyright. All rights reserved © 

import os
from subprocess import Popen, PIPE
import pathlib

# Getting game path to change the main directory
game_path = (str(pathlib.Path(pathlib.Path(__file__).parent.absolute()).parent.absolute()) + "/snakeAIGame/bin")#.replace(" ", "\ ")

# Changing the main directory to the game directory (ready to execute the java)
os.chdir(game_path)

# Opening the game using JRE
game = Popen(['java', 'snakeAIGame.snakeAIGameMain'], stdin=PIPE, stdout=PIPE, text=True)

# Method to send and receive data from the process (if you send data and don't receive the program will stuck here)
def command(process, data):
    data = str(data)
    if not data.endswith("\n"):
        data = data + "\n"
    game.stdin.write(data)
    game.stdin.flush()
    return game.stdout.readline()

# Main loop
while True:
    text = input()
    output = command(game, text)
    if game.poll() is not None:
        break
    else:
        print(output)
    

