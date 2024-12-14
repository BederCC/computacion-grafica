from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
import sys

# Variable global para el color
color = [0.0, 0.0, 1.0]  # Color inicial (azul)

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def keyboard(key, x, y):
    global color
    if key == b'r':  # Rojo
        color = [1.0, 0.0, 0.0]
    elif key == b'g':  # Verde
        color = [0.0, 1.0, 0.0]
    elif key == b'b':  # Azul
        color = [0.0, 0.0, 1.0]
    glutPostRedisplay()  # Solicita volver a renderizar

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    # Plot de las coordenadas
    glBegin(GL_LINES)
    glVertex2f(-4.0, 0.0)  # Horizontal
    glVertex2f(4.0, 0.0)
    glVertex2f(0.0, 2.0)  # Vertical
    glVertex2f(0.0, -2.0)
    glEnd()
    # Plot de los parámetros de la ecuación
    glPointSize(3)
    glBegin(GL_POINTS)
    for px in np.arange(0, 15, 0.025):
        glColor3f(*color)  # Usa el color seleccionado
        glVertex2f(px, math.sin(px))
        glVertex2f(px, math.cos(px))
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 400)
    glutCreateWindow("Grafica de la funcion Seno y Coseno")
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

main()
