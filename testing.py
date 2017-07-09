import pygame, sys, os
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
NO_HIGH_SCORES = 5

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
                TIME = int(TIME*0.95)
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
                if not os.path.exists('high_scores.txt'):
                    with open('high_scores.txt', 'w') as fid:
                        for i in range(NO_HIGH_SCORES):
                            fid.write(chr(65+i)*3 + ' ' + \
                                      str(NO_HIGH_SCORES-i) + '\n')
                        
                    
                with open('high_scores.txt', 'r') as fid:
                    scores = {}
                    for i in range(NO_HIGH_SCORES):
                        tmp = fid.readline().split(' ')
                        print(tmp)
                        scores[i+1] = (tmp[0], int(tmp[1]))
                print(scores)
                myscore = score
                if score > scores[NO_HIGH_SCORES][1]:
                    name = ''
                    text0 = myfont.render('New high score!',
                                          False, (255,)*3)
                    nametxt = myfont.render('Enter your initials',
                                          False, (255,)*3)
                    underlinetxt = myfont.render('_',
                                          False, (255,)*3)
                    playSurface.blit(text0,(100,100))
                    playSurface.blit(nametxt,(100,150))
                    for j in range(3):
                        playSurface.blit(underlinetxt, (100 + j * 30,200))
                    pygame.display.flip()
                    pygame.time.wait(2000)

                    
                    done = False
                    while not done:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                print(event.key)
                                print(pygame.key.get_pressed())
                                if event.key < 97 or event.key > 122:
                                    pass
                                else:
                                    name += chr(event.key - 32)
                                if len(name) == 3:
                                    done = True
                                for j in range(3):
                                    try:
                                        playSurface.blit(myfont.render(name[j],
                                                                       False,
                                                                       (255,)*3),
                                                     (100 + j * 30,200))
                                    except IndexError:
                                        playSurface.blit(underlinetxt,
                                                     (100 + j * 30,200))
                                    pygame.display.flip()
                                    
                                
                    print(name)
                    pos = 1
                    while score <= scores[pos][1]:
                        pos += 1
                    print(pos)
                    for j in range(pos+1, NO_HIGH_SCORES+1)[::-1]:
                        scores[j] = scores[j-1]
                    scores[pos] = (name, score)
                    with open('high_scores.txt', 'w') as fid:
                        for i in range(1,NO_HIGH_SCORES+1):
                            fid.write('%s %d\n' % scores[i])
                    print(scores)
                    
                    

                #fid = open("Scores.txt", 'a') 
                #fid.write(str(score) + "\n") 
                #fid.close() 
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
        text1 = myfont.render('GAME OVER - your score: %d' % myscore,
                              False, (255,)*3)
        text2 = myfont.render('Play again? Y/N',
                              False, (255,)*3)

        text3 = myfont.render('High Scores:', False, (255,)*3)
        with open('high_scores.txt', 'r') as fid:
            for i in range(NO_HIGH_SCORES):
                tmp = fid.readline().split(' ')
                name = tmp[0]
                score = int(tmp[1])
                hs_txt = myfont.render('%d. %s %d' % (i+1, name, score),
                                       False, (255,)*3)
                playSurface.blit(hs_txt,(400,230 + 30*i))

        playSurface.blit(text1,(100,100))
        playSurface.blit(text2,(100,150))
        playSurface.blit(text3,(380,200))
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
                
                
            


