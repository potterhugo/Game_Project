import pygame, sys
#from pygame.locals import *

import random, math

pygame.init()
fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640,480))
pygame.display.set_caption('CHASE THE DOT!!!')
RESETEVENT = pygame.USEREVENT + 1

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)

def d(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

INIT_TIME = 2200

flag = True
PLAYING = True
score = 0
TIME = INIT_TIME
while True:
    if PLAYING:
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
                if d(event.pos, circle_pos) <= 30:
                    score += 1
                    pygame.draw.circle(playSurface,
                                       pygame.Color(0,255,0),
                                       circle_pos,
                                       30,0)
                    pygame.display.flip()
                    pygame.time.wait(150)
                else:
                    pygame.draw.circle(playSurface,
                                       pygame.Color(255,0,0),
                                       circle_pos,
                                       30,0)
                    pygame.display.flip()
                    pygame.time.wait(150)
                flag = True
                TIME = int(TIME*0.9)
                print(TIME)
            elif event.type == RESETEVENT:
                print('asdf')
                pygame.draw.circle(playSurface,
                                   pygame.Color(255,0,0),
                                   circle_pos,
                                   30,0)
                pygame.display.flip()
                pygame.time.wait(150)
                PLAYING = False
                break
        if flag:
            playSurface.fill(pygame.Color(0,0,0)) # Clear screen

            circle_pos = (random.randint(0,610)+15, random.randint(0,450)+15)

            pygame.draw.circle(playSurface,
                               pygame.Color(255,255,255),
                               circle_pos,
                               30,0)
            flag = False
            pygame.time.set_timer(RESETEVENT, TIME)

            pygame.display.flip()
    else:
        playSurface.fill(pygame.Color(0,0,0))
        text1 = myfont.render('GAME OVER - your score: %d' % score,
                              False, (255,)*3)
        text2 = myfont.render('Play again? Y/N',
                              False, (255,)*3)
        playSurface.blit(text1,(100,100))
        playSurface.blit(text2,(100,150))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
                print(pygame.key.get_pressed())
                if event.key == 110:
                    pygame.quit()
                elif event.key == 121:
                    PLAYING = True
                    flag = True
                    score = 0
                    TIME = INIT_TIME
                    break
            


