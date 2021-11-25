import sys
import os
import time
from generator.position import MANDATORY_POSITION
from robot import Nao

NAO_IP = sys.argv[1]
PORT = int(sys.argv[2])
print(NAO_IP)
print(PORT)

music_path = os.path.abspath(os.getcwd()) + '/music.wav'

Nao = Nao(NAO_IP, PORT)

Nao.say("Team Becchi pagliacci <3. P.S.: vi vogliamo bene ugualmente")

song = Nao.playMusic(music_path)

with open('choreography.txt', 'r') as file:
    choreography = [line.strip() for line in file]

time.sleep(0.2)

try:
    for move in choreography:
        if move in MANDATORY_POSITION:
            print('\n' + move.upper() + '\n')
        else:
            print(move)
        Nao.applyPosture(move)
except Exception as e:
    Nao.stopMusic(song)
    print(e)

Nao.stopMusic(song)
