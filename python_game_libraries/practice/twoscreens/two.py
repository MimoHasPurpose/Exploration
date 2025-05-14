import pygame
from pygame.locals import *
from pygame import mixer
import random


pygame.init()

 


screen=pygame.display.set_mode((550,550))
screen2=pygame.display.set_mode((550,550))
pygame.font.init()
pygame.display.set_caption("Sammie vs Mimo!!")

clock=pygame.time.Clock()
running =True


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip()
    clock.tick(20)
pygame.quit()


