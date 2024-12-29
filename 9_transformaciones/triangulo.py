import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
)

color = (0.5, 0.5, 0.5)
escala = 1.0
incremento = 0.01

def dibujar_triangulo():
    glBegin(GL_TRIANGLES)
    glColor3fv(color)
    for vertice in vertices:
        glVertex3fv(vertice)
    glEnd()

def main():
    global escala, incremento
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
        escala += incremento
        if escala >= 2.0 or escala <= 0.5:
            incremento = -incremento
        pygame.display.flip()
        pygame.time.wait(10)

main()
