# NAOdanceProject

# ------------------------------------------------------------------------------------------------------------------
Just-Dance-NAO

Team Name: Just Dance NAO
Fundamentals of Artificial Intelligence and Knowledge Representation 
NAO Planning Challenge 2019

Getting Started
1. Open the Command Prompt
2. Change the directory to the project folder 
3. Launch the project by typing: `just_dance_nao.py --port YourNAORobotPortNumber`

Prerequisites
- Choregraphe suite
- py_plan - https://pypi.org/project/py-plan/
- py_search - https://pypi.org/project/py-search/
- pygame - https://pypi.org/project/pygame/
- mutagen - https://pypi.org/project/mutagen/


Authors

Simone Gayed Said - simone.gayed@studio.unibo.it 
Pietro Obbiso - pietro.obbiso@studio.unibo.it 
Ramsiya Ramanathan - ramsiya.ramanathan@studio.unibo.it

Useful Links

Special Movements - https://funlab.nd.edu/the-nao-base/special-movements/
Spotify playlist - https://open.spotify.com/playlist/3nBdD3CigeiexPsubKnCxb?si=BkxprH0FSWOMZ9PjHQ9bkA

# ------------------------------------------------------------------------------------------------------------------

latinNAO
Project of Fundamental of AI in which NAO robot will dance following a choreography

Song: Con Calma by Daddy Yankee ( The file song3.wav is inside of the project folder)
Gender: Reggaeton
Participants:   Angely Oyola and 
				Marcello Sicbaldi

Goals:
This project has got the following goals:

1) To stimulate the comprehension and
   the discussion regarding the basic
   algorithm for planning, in the context of
   AI discipline   
2) To test your skill on a fun and intuitive
   case study: the humanoid NAO robot
3) To devise techniques for automatic and creative generation of
   complex movements in robots, such as choreographies
 
Rules:
And the rules are:

1) Each group must plan a choreography (sequence of
   positions) given a problem description
2) Each group must choose a music suitable for the
   choreography (by respecting the total time limit of 3 minutes)
   and test it on the virtual NAO (using Choregraphe)
3) A day of voting will then take place (during the last lectures)
   in which the winning choreography will be decided,
   considered the most satisfying from the artistic point of view
4) We must use mandatory positions and also intermadiate ones.

This project can be cloned or forked using github 

Requirements:
1) Python 3.5 installed
2) Choregraphe 2.1.4.13 ( or above ) installed 

# ------------------------------------------------------------------------------------------------------------------

---PROJECT OF FUNDAMENTALS OF ARTIFICIAL INTELLIGENCE A.A. 2019/2020---
Name of the group: PartyNAO
Partecipants: Mancini Eleonora 0000949698, Rambaldi Francesco 0000927342
E-mails: eleonora.mancini5@studio.unibo.it , francesco.rambaldi@studio.unibo.it
Necessary libraries:

                        math 
                        sys
                        random 
                        naoqi


                        crouch 
                        diagonal_left
                        diagonalright
                        doublemovement
                        move_forward
                        movebackward
                        right_arm 
                        rotation_foot_left_leg
                        rotation_foot_right_leg
                        rotationhandgun
                        sit 
                        sit_relax
                        stand_init
                        stand_zero
                        stand
                        union_arms
                        hello
                        wipe_forehead
                        new_speedy
                        new_superman 
                        sprinkler
                        sing_with_me
                        birthday_dance
                        workout




                        time
                        argparse
                        operator
                        math
                        random
                        glob, os 
                        pydub 
                        threading 
                        itertools 
                        time 
                        pydub 
                        glob, os 
                        random
                        scipy
                        numpy 
                        matplotlib
                        
It's necessary to install ffmpeg in order to be able to process the audio. 

To run our project you have to set the correct port of the robot in the file "party_nao_project.py" and "party_nao_problem_def.py".
Then, you have to open a terminal in the main folder of the project and launch "party_nao_project.py". 


Our program will select a song randomly, plot its amplitude, run simulated annealing e find the best sequence for that song. 
Then, it will automatically start the music and the choreography.

We tested our project on Linux system, so it is recommended to run the program on a UNIX system (4 GB of RAM at least). 

# ------------------------------------------------------------------------------------------------------------------

# NAO Planning Challenge
**Group:** You're a big boy, NAO  
**Students:**
 - Agostino Aiezzo, <agostino.aiezzo@studio.unibo.it>
 - Emmanuele Bollino, <emmanuele.bollino@studio.unibo.it>

### Files
Presentation of the project in in the file "\_PRESENTATION/Slides.pdf"  
Video demonstration of the dance is in the file "\_PRESENTATION/Video_choreography.mp4"

### Instructions
 - Use the NAO Virtual Machine
 - Make sure that both Python 2 and Python 3 are installed. Default version should be 2
 - Create a PyCharm project and add all the files in here (use PyCharm just to import NaoQi)
 - Import NaoQi from the download (Scaricati) folder, it is already in there
 - Open a terminal in the project path
 - Change permission for scripts
    ```sh
    chmod 777 ./start.sh
    chmod 777 ./install.sh
    ```
 - Install all the requirements
    ```sh
    ./install.sh
    ```
 - Open Choregraphe in order to simulate NAO
 - Copy the ip and the port of the simulated (or real) NAO
 - Launch the starting script
    ```sh
    ./start.sh <nao_ip> <nao_port>
    ```
 - Planning generation may take a while, just be patient
 - Look at NAO!

# ------------------------------------------------------------------------------------------------------------------

NAO Challange - Cobiat Team
Omar Younis - omargallal.younis@studio.unibo.it
Mattia Bertè - mattia.berte@studio.unibo.it

-------------------------------------------------------------------------

Necessary library: numpy

In the python project:

1) Open configuration.py and set the correct ip and port for nao.
2) Launch main.py
3) Enjoy it!


search.py implements the search algorithm for planning postures sequence
performer.py perform a given sequence of postures

# ------------------------------------------------------------------------------------------------------------------

# DuoNao
This work was done by Ludovico Granata and Simone Persiani
as a study project for the "Fundamentals of AI and Knowledge
Representation" course (Master Degree in Artificial Intelligence - University of Bologna).

Our team was named "DuoNao" and our goal was to win the 2020 edition of the so called NaoChallenge.
The project was submitted on December 5th 2020.

## Resources
  * [Music](https://github.com/iosonopersia/duonao/blob/main/Don't%20stop%20me%20now%20-%20Queen.mp3)
  * [Demo video](https://github.com/iosonopersia/duonao/blob/main/Don't%20stop%20me%20NAO%20(queen).mp4)
  * [Presentation slides](https://github.com/iosonopersia/duonao/blob/main/NAO%20Challenge.pdf)

## Instructions
Starting from a working instance of the "NaoUbuntu" virtual machine:
  1. Install VLC and GIT:
```bash
sudo apt-get update
sudo apt-get install vlc git
```
  2. Download the repository:
```bash
git clone https://github.com/iosonopersia/duonao
```
  3. Get the needed Python3 tools:
```bash
cd duonao
pip3 install -U pip setuptools
sudo apt-get install python3-venv
```
  4. Prepare the virtual environment:
```bash
python3 -m venv venv
```
  5. Install the Python3 dependencies:
```bash
. venv/bin/activate
pip3 install -r requirements.txt
deactivate
```
  6. Run the script inside a terminal emulator
     (let's say the virtual robot is listening on the 42135 port):
```bash
cd duonao
. venv/bin/activate
python3 main.py localhost 42135
deactivate
```

**To run the script, Choreograph must be opened with a proper virtual robot available for external connections**
**Please, remember to do the following steps before launching the script:**
  1. **open Choreograph**
  2. **go to Edit->Preferences and open the 'General' tab**
  3. **set 'Motor speed (%)' to 100**
  4. **switch to the 'Virtual Robot' tab**
  5. **select the 'NAO H25 (V40)' as the 'Robot model'**
  6. **click on the 'OK' button in the bottom right of the modal window**

# ------------------------------------------------------------------------------------------------------------------

# NAOChallenge FAST-FREQUENCY
**Participants:** 
[Zarmina Ursino](https://github.com/Zarmina97) , 
[Sandeep Kumar Kushwaha](https://github.com/xandie985) , 
[Samral Tahirli](https://github.com/samraltahirli)

**OBTAIN THE CHOREGRAPHE FILE HERE:** https://drive.google.com/drive/folders/1pIRpZiDuBrvC3VIPP3ZKrkusU_yLcD5j?usp=sharing 

**Folder description:**
The folder contains the actions files
  > those starting with "m_" are mandatory ones
  >  those starting with "o_" are the optional ones that we have created
"mainFile.py" contains the code the run the action figures based on the most appropriate costs

**How it works:**
1. The action files are saved with extra lists- keyValues & finalPositionValue. 
    keyValues - contains the key positions i.e. - LshoulderPitch, LshoulderRoll, LElbowYaw, LElbowRoll, LHipYawPitch, LHipPitch, LKneePitch
    finalPositionValues - contain the final position of above parameters for each movement
    
2. The mainFile.py contains following:
    >*the action files are imported and saved into two seperate lists
    
    >*execute_performance() - runs the code the action that has been provided through the parameter; need to provide specific port address
    
    >*costDofference(val1, val2, val3) - val1 is intial mandatory position, val3 is final mandatory position, val2 is the position that needs to be picked from the availablePos[]
    
    >*findTheNextNode() - finds the most optimum movement from the optional positions with the help of costDifference function and thereby executes that particular funxtion and removes it from the list, so the optional movements is not considered later
    
    >*mainFunctionToRun() - this is main driver function that initiates the actions!
    
    >*commented code below - was used to fetcht the important list values for action files.

# ------------------------------------------------------------------------------------------------------------------

NAO PLANNING - SAMUELE DI TULLIO - samuele.ditullio@studio.unibo.it - A.Y. 2020/2021

Choreographe version: 2.8.6.23

The project includes a 3 minute choreograph, planned as follow:

- Initial position: Stand Init;
- An ".ogg" file is loaded and then played with the service "ALAudioPlayer", executed in parallel with the Animation box;
- A set of positions are executed, both using the Pose Library included in the software and some Timelines;
- The series of standing positions are executed at the beginning, while the sitting ones are executed at the end, thus saving time for the transition from one pose to another;
- Final position: Crouch;

* Timelines have been written by me and consists of a series of new positions drawn using the Inspector window, with wich I specified the angular grade of each joint, and the Behaviour Layer, with wich I decided the order and the duration of each position;
** First I decided to move a single joint at a time, starting from the standing position, then to combine the movements of more joints together playing with the equilibrium of the robot, and then to move more joints together mirroring the behaviour of left and right sides;

# ------------------------------------------------------------------------------------------------------------------

# Robot-Bolle-2.0
A Choreograph project to make dance a virtual NAO, created for the NAO Competition of the Artificial Intelligence M.Sc. of University of Bologna by Valentina Boriano, Piero Castriota and Pietro Fanti.

The Robot use a breadth-first graph search to choose mooves to best fit the duration of the dance. Eventual pauses are evenly distributed over the entire dance.

Check Robot Bolle on TikTok: https://www.tiktok.com/@robotbolle

## Requirements
To run the code you need Choreograph and the following Python modules (probably most of these are already installed):
- bisect
- collections
- abc
- functools
- heapq
- operator
- os.path
- random
- itertools
- sys
- math
- time

They must be installed inside the Python directory of Choreograph, usually it is: 

C:\Program Files (x86)\Softbank Robotics\Choregraphe Suite 2.8\lib\python2.7\Lib\site-packages



# -----------------------------------------------------------------------------------------------------------------

//Setup and Environments
Software License - Choregraphe version 2.1.4 - Set up in Ubuntu Environment
Tested on Windows Environment - Choregraphe version 2.8.6.23
Tested on Ubuntu Environment - Choregraphe version 2.8.6.23

Please set up the right port (achievable in Nao's connection Preferences)
for each python box inside the diagram boxes 'Passi' and 'Passi(1)'. 
The variable 'port' is always in the end of the code. 

//Directory files
Cicirinao.crg
Demo.mp4
heapq.py
queue.py
almath.py
CicirinaoPresentation.pdf

//Suggestions 
If the song continue the execution after stopping it, please make a double click
On the last output of the last block (in this case, output of Crouch box)

//Developer's contacts
marco.aspromonte@studio.unibo.it
francesco.romito2@studio.unibo.it


Thanks for your consultation of the project, 
enjoy the Cicirinao choreography
 
# ---------------------------------------------------------------------------------------------------------------------