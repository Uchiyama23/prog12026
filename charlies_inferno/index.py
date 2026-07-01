import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
TITLE = "Aura+Ego"
import pgzrun
from pgzero.builtins import Actor 
import pygame
pygame.init()

background= Actor('inferno.png')

charlie= Actor('charlie.png')
charlie.pos= (550,250)

jeremias= Actor('jeremy.png')
jeremias.pos=(350,250)

WIDTH = 800
HEIGHT = 400
def draw():
    screen.clear()
    background.draw()
    jeremias.draw()
    charlie.draw()
i=0
def update():
    global jeremias
    global charlie
    global i
    if keyboard.up:
        jeremias.y-= 5
    if keyboard.down:
        jeremias.y += 5
    if keyboard.left:
        jeremias.x -= 5
    if keyboard.right:
        jeremias.x += 5
    if jeremias.colliderect(charlie):
        y=jeremias.pos
        print("oi")
        jeremias=Actor('jeremiasaberto.png')
        jeremias.pos=y
        i= i+1
    else: 
        y=jeremias.pos
        print("ai")
        jeremias=Actor('jeremy.png')
        jeremias.pos=y
    if i>3:
        y= charlie.pos
        charlie= Actor('charlieejere.png')
        jeremias= Actor(0)
        charlie.pos=y



pgzrun.go()
