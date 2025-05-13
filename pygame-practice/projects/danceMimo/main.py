import pygame
from pygame.locals import *
from pygame import mixer
import random
# mixer init
# from pygame import mixer
pygame.init()


WIDTH=800
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.font.init()
screen.fill("WHITE")
pygame.display.set_caption("danceMimo!!")
mimo=pygame.image.load("E:\Github\Exploration\pygame-practice\ecosystem\pics\cat_flower.jpg").convert()
screen.blit(mimo,(WIDTH/2,HEIGHT/2))
mixer.init()
mixer.music.load("meow.ogg")


pygame.mixer.music.play(1000)
clock=pygame.time.Clock()
running =True
moving=False



while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
    
    #game starts from here!

    pygame.display.flip()
    clock.tick(20)
pygame.quit()


