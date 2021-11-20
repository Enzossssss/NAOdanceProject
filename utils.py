from naoqi import ALProxy
from positions import *


class Nao:
    MADATORY_POSITION = ['SitRelax', 'Sit', 'Wipe_Forehead',
                         'Stand', 'StandInt', 'Hello', 'StandZero', 'Crouch']

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
            'Arms_opening': Arms_opening,
            'Crouch': Crouch,
            'Diagonal_left': Diagonal_left,
            'Diagonal_right': Diagonal_right,
            'Double_movement': Double_movement,
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
            'Left_sprinkler': Left_sprinkler,
            'Right_sprinkler': Right_sprinkler,
        }

        function = switch.get(string, None)

        if function == None:
            print("\n....")
            print("Not Valid Position")
            print("Move to the next")
            print("....\n")
        else:
            function.main(self.ip, self.port)
