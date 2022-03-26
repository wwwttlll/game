from cgi import print_form
import pygame as pg
import random
import sys
import time
pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Snake")
white = (255,255,255)
black = (0,0,0)
headpos = [410,300]
cell = 10
bodypos = [[410,300],[400,300],[390,300]]
size = 3
fd=[0,0]

def drawbody(color,pos):
    pg.draw.rect(screen,color,(pos[0],pos[1],10,10))

def Init_body():
    drawbody(white,[410,300])
    drawbody(white,[400,300])
    drawbody(white,[390,300])
    pg.display.update()
Init_body() 
fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
def Print_food():
    pg.draw.rect(screen,(0,255,0),(fd[0],fd[1],10,10))
    pg.display.update()
Print_food() 
def Print(): 
    for pos in bodypos:
        drawbody(white,pos)
    pg.display.update()

def judge_eat():
    if abs(fd[0] - headpos[0]) == 0 and abs(fd[1] - headpos[1]) == 0 :
        return True
    else:
        return False
def die():
    pic = pg.image.load("F://GitHub//Game//snake//youdied.jpg")
    screen.blit(pic,(0,0))
    pg.display.update()

def judge_die():
    if headpos[0] <= 0 or headpos[0] >= 800 or headpos[1] <= 0 or headpos[1] >= 600:
        return True
    if headpos in bodypos[1:]:
        return True
    else: return False
dir = "right"
def change_pos():
    bodypos.insert(0,list(headpos))
    if judge_eat() == False :
        bodypos.pop()
        return 0
    else : 
        return 1
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if(event.key == pg.K_a or event.key == pg.K_LEFT):
                dir = "left"
                headpos[0] -= cell
                f = change_pos()
                if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
                screen.fill(black)
                Print_food()
                Print()
            if(event.key == pg.K_d or event.key ==pg.K_RIGHT):
                #print('right')
                dir = "right"
                headpos[0] += cell
                f = change_pos()
                if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
                screen.fill(black)
                Print_food()
                Print()
            if(event.key == pg.K_w or event.key == pg.K_UP):
                #print('up')
                dir = "up"
                headpos[1] -= cell
                f = change_pos()
                if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
                screen.fill(black)
                Print_food()
                Print()
            if(event.key == pg.K_s or event.key == pg.K_DOWN):
                #print('down')
                dir = "down"
                headpos[1] += cell
                f = change_pos()
                if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
                screen.fill(black)
                Print_food()
                Print()       
    time.sleep(0.25)
    if dir == "right": #r
        headpos[0] += cell
        f = change_pos()
        if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
        screen.fill(black)
        Print_food()
        Print()
    if dir == "left": #l
        headpos[0] -= cell
        f = change_pos()
        if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
        screen.fill(black)
        Print_food()
        Print()
    if dir == "down": #d
        headpos[1] += cell
        f = change_pos()
        if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
        screen.fill(black)
        Print_food()
        Print()
    if dir == "up": #u
        headpos[1] -= cell
        f = change_pos()
        if f == 1: fd = [random.randrange(1,80) * 10, random.randrange(1,60) * 10 ]
        screen.fill(black)
        Print_food()
        Print()    #'''
    if judge_die() == True:
        die() 
        time.sleep(3) 
        pg.quit() 
        sys.exit()

