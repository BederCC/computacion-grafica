import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

caras = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (
    (1, 0, 1),
    (1, 1, 0),
    (1, 0, 0.3),
    (1, 1, 0.4),
    (0, 1, 1),
    (1, 0.5, 0.5)
)

def gradient_color(v1, v2, t):
    return [(1-t)*v1[i] + t*v2[i] for i in range(3)]

def Cubo():
    glBegin(GL_QUADS)
    for i, cara in enumerate(caras):
        color1 = colors[i]
        color2 = colors[(i+1) % len(colors)]
        for j, vertex in enumerate(cara):
            t = j / (len(cara) - 1)
            color = gradient_color(color1, color2, t)
            glColor3fv(color)
            glVertex3fv(vertices[vertex])
    glEnd()

def Ejes():
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    glVertex3f(-8, 0, 0)
    glVertex3f(8, 0, 0)
    glColor3f(1, 1, 1)
    glVertex3f(0, -8, 0)
    glVertex3f(0, 8, 0)
    glColor3f(1, 1, 1)
    glVertex3f(0, 0, -20)
    glVertex3f(0, 0, 20)
    glEnd()

def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -10)
    glRotatef(25, 2, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cubo()
        Ejes()
        pygame.display.flip()
        pygame.time.wait(10)

main()
