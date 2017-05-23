import pygame, sys
#from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('example')

while True:
    tr = pygame.key.get_pressed()
    #if event.key == K_ESCAPE:
    #    sys.exit()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                print(pygame.key.get_pressed())
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                playSurface.fill(pygame.Color(0,0,0))
                print(event.pos)
                pygame.draw.circle(playSurface,
                                   pygame.Color(250,8,120),
                                   event.pos,
                                   30,0)
                pygame.display.flip()
                

