import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices_triangulo = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
)

vertices_pentagono = (
    (0, 1, 0),
    (-0.95, 0.31, 0),
    (-0.59, -0.81, 0),
    (0.59, -0.81, 0),
    (0.95, 0.31, 0),
)

color_triangulo = (0.5, 0.5, 0.5)
color_pentagono = (0.7, 0.7, 0.3)

escala = 1.0
incremento_escala = 0.01
traslacion_x = 0.0
incremento_traslacion = 0.02

def dibujar_triangulo():
    glBegin(GL_TRIANGLES)
    glColor3fv(color_triangulo)
    for vertice in vertices_triangulo:
        glVertex3fv(vertice)
    glEnd()

def dibujar_pentagono():
    glBegin(GL_POLYGON)
    glColor3fv(color_pentagono)
    for vertice in vertices_pentagono:
        glVertex3fv(vertice)
    glEnd()

def main():
    global escala, incremento_escala, traslacion_x, incremento_traslacion

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glScalef(escala, escala, escala)
        dibujar_triangulo()
        glPopMatrix()
        glPushMatrix()
        glTranslatef(traslacion_x, 0.0, 0.0)
        dibujar_pentagono()
        glPopMatrix()
        escala += incremento_escala
        if escala >= 2.0 or escala <= 0.5:
            incremento_escala = -incremento_escala
        traslacion_x += incremento_traslacion
        if traslacion_x >= 3.0 or traslacion_x <= -3.0:
            incremento_traslacion = -incremento_traslacion
        pygame.display.flip()
        pygame.time.wait(10)
main()
