import pygame, sys
#from pygame.locals import *

import random, math

pygame.init()
fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('CHASE THE DOT!!!')
RESETEVENT = pygame.USEREVENT + 1



def d(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

flag = True
score = 0
while True:
    tr = pygame.key.get_pressed()
    #if event.key == K_ESCAPE:
    #    sys.exit()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Your score = %d' % score)
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                print(pygame.key.get_pressed())
                if event.key == pygame.K_ESCAPE:
                    print('Your score = %d' % score)
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                score += 1
                if d(event.pos, circle_pos) <= 30:
                    pygame.draw.circle(playSurface,
                                       pygame.Color(0,255,0),
                                       circle_pos,
                                       30,0)
                    pygame.display.flip()
                    pygame.time.wait(150)
                else:
                    score -= 1
                    pygame.draw.circle(playSurface,
                                       pygame.Color(255,0,0),
                                       circle_pos,
                                       30,0)
                    pygame.display.flip()
                    pygame.time.wait(150)
                flag = True
            elif event.type == RESETEVENT:
                print('asdf')
                pygame.draw.circle(playSurface,
                                   pygame.Color(255,0,0),
                                   circle_pos,
                                   30,0)
                pygame.display.flip()
                pygame.time.wait(150)
                flag = True
    if flag:
        playSurface.fill(pygame.Color(0,0,0)) # Clear screen

        circle_pos = (random.randint(0,610)+15, random.randint(0,450)+15)
        
        pygame.draw.circle(playSurface,
                           pygame.Color(255,255,255),
                           circle_pos,
                           30,0)
        flag = False
        pygame.time.set_timer(RESETEVENT, 1000)
        
        pygame.display.flip()                
                

