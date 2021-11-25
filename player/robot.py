from naoqi import ALProxy
from positions import *
import sys
import os
import time


class Nao:
    def __init__(self, NAO_IP, PORT):
        self.tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
        self.player = ALProxy("ALAudioPlayer", NAO_IP, PORT)
        self.ip = NAO_IP
        self.port = PORT

    def say(self, string):
        return self.tts.say(string)

    def playMusic(self, music_path):
        return self.player.post.playFile(music_path)

    def stopMusic(self, song):
        return self.player.stop(song)

    def applyPosture(self, string):
        switch = {
            'Stand_from_sit': Stand_from_sit,
            'Arms_opening': Arms_opening,
            'Crouch': Crouch,
            'Diagonal_left': Diagonal_left,
            'Diagonal_right': Diagonal_right,
            'Move_backward': Move_backward,
            'Move_forward': Move_forward,
            'Right_arm': Right_arm,
            'Rotation_foot_LLeg': Rotation_foot_LLeg,
            'Rotation_foot_RLeg': Rotation_foot_RLeg,
            'Rotation_handgun_object': Rotation_handgun_object,
            'Sit': Sit,
            'SitRelax': SitRelax,
            'Stand': Stand,
            'StandInit': StandInit,
            'StandZero': StandZero,
            'Union_arms': Union_arms,
            'Hello': Hello,
            'Wipe_Forehead': Wipe_Forehead,
            'AirGuitar': AirGuitar,
            'ComeOn': ComeOn,
            'Dab': Dab,
            'DanceMove': DanceMove,
            'PulpFiction': PulpFiction,
            'TheRobot': TheRobot,
            'Mani_sui_fianchi': Mani_sui_fianchi,
            'Ballo_braccia': Ballo_braccia,
            'Right_sprinkler': Right_sprinkler,
            'Happy_Birthday': Happy_Birthday
        }

        function = switch.get(string, None)

        if function == None:
            print("\n....")
            print("Not Valid Position")
            print("Move to the next")
            print("....\n")
        else:
            function.main(self.ip, self.port)


def main():
    NAO_IP = sys.argv[1]
    PORT = int(sys.argv[2])

    print(NAO_IP)
    print(PORT)

    music_path = os.path.abspath(os.getcwd()) + '/music.wav'

    nao = Nao(NAO_IP, PORT)

    #song = nao.playMusic(music_path)

    with open('time.txt', 'r') as file:
        choreography = [line.strip() for line in file]

    time.sleep(0.2)

    list = []

    try:
        for move in choreography:
            start = time.time()
            nao.applyPosture(move)
            end = time.time()
            print(move, end - start)
            if move != 'Stand':
                list.append((move, end - start))
    except Exception as e:
        # nao.stopMusic(song)
        print(e)

    with open("t.txt", "w") as file:
        for row in list:
            file.write(str(row) + '\n')

    # nao.stopMusic(song)


if __name__ == '__main__':
    main()
