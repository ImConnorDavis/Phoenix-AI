import speech_recognition as sr
import RPi.GPIO as GPIO
from time import sleep
import pygame
import time
import datetime
import random
p1 = 1
t1 = 0
myname = 'access'
saidtrue = 0
completeSetup = 1
yesSir = 1
myChoice = 0


greetingsl = ['hi', 'hello']
gendersl = ['him', 'he', 'her', 'she']
tensesl = ['is', 'was']
emotionsbl = ['mad', 'upset', 'angry']
questionsl = ['who', 'what', 'where', 'when', 'why']

# obtain audio from the microphone
pygame.init()
pygame.mixer.init()

sir = pygame.mixer.Sound("Voices/sir.wav")
#Greetings
hello = pygame.mixer.Sound("Voices/hello.wav")
hi = pygame.mixer.Sound("Voices/hi.wav")
welcome = pygame.mixer.Sound("Voices/welcome.wav")
#Other
i = pygame.mixer.Sound("Voices/i.wav")
am = pygame.mixer.Sound("Voices/am.wav")
sorry = pygame.mixer.Sound("Voices/sorry.wav")
school = pygame.mixer.Sound("Voices/school.wav")
was = pygame.mixer.Sound("Voices/school.wav")
back = pygame.mixer.Sound("Voices/back.wav")
#Question
how = pygame.mixer.Sound("Voices/how.wav")

##Motor controls
GPIO.setmode(GPIO.BOARD)
Motor1A = 16
Motor1B = 18
Motor1E = 22
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

with open("info", "r+") as f:
    if "complete" not in f.read():
        firstSound = pygame.mixer.Sound("Voices/Importing_preferences.wav")
        firstSound.play()
        f.write("complete\n")
        completeSetup = 0
with open("info", "r+") as f:
    if "sir" not in f.read():
        yesSir = 0

r = sr.Recognizer()


while True:
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        ctime = datetime.datetime.now()
        
# recognize speech using Sphinx
    try:
        if completeSetup == 0:
            print("sirorno?")
            with open("info", "r+") as f:
                if 'sir' not in f.read():
                    sirOrNo = pygame.mixer.Sound("Voices/sir or no.wav")
                    sirOrNo.play()
                    said = r.recognize_google(audio)
                    if "yes" in said:
                        f.write("sir\n")

        said = r.recognize_google(audio)
        print(said)
        
        if myname in said or saidtrue == 1:
            saidtrue = 1
            
            if 'now' in said:
                p1 = p1 + 1
                p2 = p1 - 1
                with open("me", "r+") as f:
                    f.truncate()
                    f.write(str(p1))
            if 'shut up' in said:
                p1 = p1 + 1
                with open("me", "r+") as f:
                    f.truncate()
                    f.write(str(p1))

            if any(word in said for word in greetingsl):
                
                if said.strip().find(' ') != -1:
                    if any(word in said for word in greetingsl):
                         myChoice == int(random.uniform(0,2))
                         if myChoice == 0:
                             hello.play()
                             time.sleep(.7)
                             if (yesSir == 1):
                                 sir.play()
                                 time.sleep(.5)
            if 'turn' in said:
                if 'on lights' in said:
                    yes.play()
                    sleep(.5)
                    sir.play()
                    GPIO.output(Motor1A,GPIO.HIGH)
                    GPIO.output(Motor1B,GPIO.LOW)
                    GPIO.output(Motor1E,GPIO.HIGH)
                if 'off lights' in said:
                    GPIO.output(Motor1A,GPIO.LOW)
                    GPIO.output(Motor1B,GPIO.HIGH)
                    GPIO.output(Motor1E,GPIO.HIGH)
                sleep(1)
                GPIO.output(Motor1E,GPIO.LOW)
                    

                if 'back from' in said:
                    if 'school' in said:
                        myChoice = int(random.uniform(0,2))
                        if myChoice == 0:
                            hello.play()
                            time.sleep(1)
                            if (yesSir == 1):
                                sir.play()
                                time.sleep(.5)
                        if myChoice >= 1:
                            welcome.play()
                            time.sleep(.6)
                            back.play()
                            time.sleep(.6)
                            if (yesSir == 1):
                                sir.play()
                                time.sleep(.5)
                        
                        
                
                
            
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
