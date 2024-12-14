import sys
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from  numpy import *


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)  # Vista ortogonal 2D

def drawfun():
    glClear(GL_COLOR_BUFFER_BIT )
    m = 1.0  # Pendiente
    b = 1.0  # Intersección con el eje y
    # sombreando la linea oblicua
    for x in arange(-10.0, 5.0, 0.02):
        for y in arange(-10.0, 5.0, 0.02):
            if y <  m * x + b:
                glColor3f(0.50, 0.50, 0.50)
                glBegin(GL_POINTS)
                glVertex2f(x,y)
                glEnd()
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
    glColor3f(0.0, 0.0, 0.0)  # Rojo
    glBegin(GL_POINTS)
    for i in arange(-10.0, 5.0, 0.01):
        y = m*i + b
        glVertex2f(i, y)
    glEnd()
    glColor3f(0.0, 0.0, 0.0)  # Rojo
    glPointSize(1.0)
    # parablola
    for x in arange(-5.0, 5.0, 0.01):
        y= x*x
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
    glFlush()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50, 50)  # Posición de la ventana
    glutInitWindowSize(400, 400)  # Dimensiones de la ventana<
    glutCreateWindow("Area Sombreada")
    glutDisplayFunc(drawfun)
    init()
    glutMainLoop()  # Inicia el bucle principal de GLUT

if __name__=="__main__":main()