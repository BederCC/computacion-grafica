import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices = (
    (0, 1, 0),  
    (1, -1, 1),    
    (-1, -1, 1),    
    (0, -1, -1)    
)

caras = (
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 1),
    (1, 2, 3) 
)

colores = [
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
]

def Piramide():
    glBegin(GL_TRIANGLES)
    for i, cara in enumerate(caras[:-1]):
        for j, vertice in enumerate(cara):
            glColor3fv(np.array(colores[j]) * (1 - i * 0.3)) 
            glVertex3fv(vertices[vertice]) 
    glEnd()

    glBegin(GL_TRIANGLES) 
    glColor3fv((1.0, 1.0, 0.0)) 
    for vertice in caras[-1]:
        glVertex3fv(vertices[vertice])  
    glEnd()

def EjesCoordenadas():
    glBegin(GL_LINES)

    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-6, -1.5, 0)
    glVertex3f(5, -1.5, 0)

    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2, -5, 0)
    glVertex3f(-2, 5, 0)

    glEnd()

rotacion = [0, 0, 0]
traslacion = [0, 0, -5]
escalacion = [1, 1, 1]

def main():
    global rotacion, traslacion, escalacion
    
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(traslacion[0], traslacion[1], traslacion[2])
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotacion[1] -= 5
                elif event.key == pygame.K_RIGHT:
                    rotacion[1] += 5
                elif event.key == pygame.K_UP:
                    rotacion[0] -= 5
                elif event.key == pygame.K_DOWN:
                    rotacion[0] += 5
                elif event.key == pygame.K_w:
                    traslacion[1] += 0.1
                elif event.key == pygame.K_s:
                    traslacion[1] -= 0.1
                elif event.key == pygame.K_a:
                    traslacion[0] -= 0.1
                elif event.key == pygame.K_d:
                    traslacion[0] += 0.1
                elif event.key == pygame.K_q:
                    traslacion[2] += 0.1
                elif event.key == pygame.K_e:
                    traslacion[2] -= 0.1
                elif event.key == pygame.K_i:
                    escalacion[1] += 0.1
                elif event.key == pygame.K_k:
                    escalacion[1] -= 0.1
                elif event.key == pygame.K_j:
                    escalacion[0] -= 0.1
                elif event.key == pygame.K_l:
                    escalacion[0] += 0.1
                elif event.key == pygame.K_u:
                    escalacion[2] += 0.1
                elif event.key == pygame.K_o:
                    escalacion[2] -= 0.1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(traslacion[0], traslacion[1], traslacion[2])
        glPushMatrix()
        EjesCoordenadas()
        glPopMatrix()
        glPushMatrix()
        glScalef(escalacion[0], escalacion[1], escalacion[2])
        glRotatef(rotacion[0], 1, 0, 0)
        glRotatef(rotacion[1], 0, 1, 0)
        glRotatef(rotacion[2], 0, 0, 1)
        Piramide()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(13)

# Ejecutar el programa
main()
