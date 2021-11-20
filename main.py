from naoqi import ALProxy
import sys
import os
from positions import *

NAO_IP = sys.argv[1]
PORT = int(sys.argv[2])
print(NAO_IP)
print(PORT)

music_path = os.path.abspath(os.getcwd()) + '/music.wav'

tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
tts.say("Team Becchi pagliacci <3. P.S.: vi vogliamo bene ugualmente")

player = ALProxy("ALAudioPlayer", NAO_IP, PORT)

song = player.post.playFile(music_path)

try:
    # sleep(3)

    Rotation_foot_LLeg.main(NAO_IP, PORT)
    Move_backward.main(NAO_IP, PORT)
    Union_arms.main(NAO_IP, PORT)
    Stand.main(NAO_IP, PORT)
    Hello.main(NAO_IP, PORT)
    AirGuitar.main(NAO_IP, PORT)
    ComeOn.main(NAO_IP, PORT)
    Dab.main(NAO_IP, PORT)
    DanceMove.main(NAO_IP, PORT)
    PulpFiction.main(NAO_IP, PORT)
    TheRobot.main(NAO_IP, PORT)

    Mani_sui_fianchi.main(NAO_IP, PORT)
    Ballo_braccia.main(NAO_IP, PORT)
    Left_sprinkler.main(NAO_IP, PORT)
    Right_sprinkler.main(NAO_IP, PORT)
    Happy_Birthday.main(NAO_IP, PORT)


except Exception as e:
    player.stop(song)
    print(e)


player.stop(song)
