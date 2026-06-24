import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
TITLE = "Aura+Ego"
import pgzrun
from pgzero.builtins import Actor 
import pygame
pygame.init()

background= Actor('inferno.png')

charlie= Actor('charlie.png')
charlie.pos= (700,450)

jeremias= Actor('jeremy.png')
jeremias.pos=(550,500)

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
    if jeremias.colliderect(charlie):
        print("oi")
        x= jeremias.pos
        jeremias=Actor('jeremiasaberto.png')  
        jeremias.pos= x

pgzrun.go()