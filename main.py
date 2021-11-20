from time import sleep
from warnings import catch_warnings
from naoqi import ALProxy
import sys
import os
from positions import *

music_path = os.path.abspath(os.getcwd()) + '/music.wav'

NAO_IP = sys.argv[1]
PORT = int(sys.argv[2])
print(NAO_IP)
print(PORT)

tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
tts.say("Team Becchi pagliacci <3. P.S.: vi vogliamo bene ugualmente")

posture = ALProxy("ALRobotPosture", NAO_IP, PORT)
player = ALProxy("ALAudioPlayer", NAO_IP, PORT)

song = player.post.playFile(music_path)

try:
    # sleep(3)

    for i in range(1000000):
        print(i)

        # if i == 1456432:
       #     print('infinite')
       # print(i)
    posture.applyPosture('Crouch', 3.0)

    Rotation_foot_LLeg.main(NAO_IP, PORT)
    Move_backward.main(NAO_IP, PORT)
    Union_arms.main(NAO_IP, PORT)
    Stand.main(NAO_IP, PORT)
    Hello.main(NAO_IP, PORT)

    for i in range(1000000):
        print(i)


except Exception as e:
    player.stop(song)
    print(e)


player.stop(song)
