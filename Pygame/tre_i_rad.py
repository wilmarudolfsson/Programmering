import pygame as pg
import sys
import time
from pygame.locals import *

XO = 'x'

winner = None
draw = None

width = 400
height = 400

white = (255, 255, 255)
line_color = (0, 0, 0)

board = [[None]*3, [None]*3, [None]*3]

pg.init()

fps = 30

CLOCK = pg.time.Clock()

screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tre i Rad")

initiating_window = pg.image.load("")
x_img = pg.image.load("")
y_img = pg.image.load("")

initiating_window = pg.transform.scale(
    initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))

def game_initiating_window():
    screen.blit(initiating_window, (0, 0))

    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0),
                 (width / 3 * 2, height), 7)
    
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2),
                 (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    global draw
    
    if winner is None:
        message = XO.upper() + "'s Tur"
    else:
        message = winner.upper() + " vann !"
    if draw:
        message = "Spel lika !"

    font = pg.font.Font(None, 30)
    text= font. render(message, 1, (255, 255, 255))

    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
    
    

