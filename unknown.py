import pygame
import time
pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound("Voices/Importing_preferences.wav")
hello = pygame.mixer.Sound("Voices/hello.wav")
sir = pygame.mixer.Sound("Voices/sir.wav")

sounda.play()
time.sleep(4)
hello.play()
time.sleep(1)

sir.play()
#time.sleep(10)
