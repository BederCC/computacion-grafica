from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import numpy as np
import math
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

def plotfunc():
    a, b = 1.0, 1.0  # Valores de los ejes
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    for t in np.arange(0, 2 * math.pi, 0.01):
        x = a * math.cos(t)
        y = b * math.sin(t)
        glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Gráfica de una Elipse")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()

main()
# Fin del programa
