import pygame, sys
from pygame.locals import *
from time import sleep

pygame.init()

# mp3 source - https://inkbunny.net/submissionview.php?id=274773
pygame.mixer.music.load("../../resources/Foxflash_-_Seiken_Densetsu_3_-_Hope._Isolation._Pray.mp3")

pygame.mixer.music.play(-1, 0.0)

while True:
    sleep(1)

