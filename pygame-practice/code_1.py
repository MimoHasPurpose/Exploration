import pygame

#setup pygame
pygame.init()
screen=pygame.display.set_mode((550,550))
pygame.font.init()
pygame.display.set_caption("Sammie vs Mimo!!")

clock=pygame.time.Clock()
running =True
i=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #game starts from here!

    screen.fill("purple")

    pygame.draw.circle(screen,"red",(200+i,200),40)
    i=i+1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

