import sys
import os
import time
from utils import Nao

NAO_IP = sys.argv[1]
PORT = int(sys.argv[2])
print(NAO_IP)
print(PORT)

music_path = os.path.abspath(os.getcwd()) + '/music.wav'

Nao = Nao(NAO_IP, PORT)

Nao.say("Team Becchi pagliacci <3. P.S.: vi vogliamo bene ugualmente")

song = Nao.playMusic(music_path)

# TODO: function to create choreogarfy

with open('choreography.txt', 'r') as file:
    choreography = [line.strip() for line in file]

time.sleep(1)

try:
    for move in choreography:
        if move in Nao.MADATORY_POSITION:
            print('\n' + move.upper() + '\n')
        else:
            print(move)
        Nao.applyPosture(move)
except Exception as e:
    Nao.stopMusic(song)
    print(e)

Nao.stopMusic(song)
