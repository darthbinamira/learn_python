import pygame, sys
from pygame.locals import *
from time import sleep

pygame.init()

sound = pygame.mixer.Sound("../../resources/beep.wav")

while True:
    sound.play()
    sleep(1)

