import pygame
from pygame.locals import *
from pygame import mixer
import random
# from zero import c1,c2
x_list=[

]
y_list=[
]

for i in range(1,50):
    x_list.append(random.randint(0,1000))
    y_list.append(random.randint(0,1000))

pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("beats.ogg")
# pygame.mixer.music.play()
 


screen=pygame.display.set_mode((550,550))
pygame.font.init()
pygame.display.set_caption("Sammie vs Mimo!!")

clock=pygame.time.Clock()
running =True


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #game starts from here!
    
       
    for i in range(1,49):
        pygame.draw.circle(screen,"pink",(x_list[i],y_list[i]),10) 
    for i in range(1,49):
        pygame.draw.circle(screen,"blue",(x_list[i],y_list[i]),8) 
    for i in range(1,49):
        pygame.draw.circle(screen,"white",(x_list[i],y_list[i]),4)  
   
    for i in range(1,49):
        if x_list[i]>550:
            x_list[i]=0
        if y_list[i]>550:
            y_list[i]=0
        if x_list[i]<0:
            x_list[i]=550
        if y_list[i]<0:
            y_list[i]=550
        x_list[i]+=random.randint(-5,5)
        y_list[i]+=random.randint(-5,5)    
    pygame.display.flip()
    clock.tick(20)
pygame.quit()


