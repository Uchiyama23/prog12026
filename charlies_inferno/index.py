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

def update():
    global jeremias
    if keyboard.up:
        jeremias.y-= 5
    if keyboard.down:
        jeremias.y += 5
    if keyboard.left:
        jeremias.x -= 5
    if keyboard.right:
        jeremias.x += 5
    while jeremias.colliderect(charlie):
        print("oi")
        jeremias=Actor('jeremiasaberto.png')


pgzrun.go()
