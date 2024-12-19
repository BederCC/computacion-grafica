from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0) 
    glPointSize(1.0)

    # Dibujar los ejes coordenados
    glBegin(GL_LINES)
    glVertex2f(-1.5, 0.0)
    glVertex2f(1.5, 0.0)
    glVertex2f(0.0, -1.5)
    glVertex2f(0.0, 1.5)
    glEnd()

    # Dibujar la curva de Lissajous
    glBegin(GL_POINTS)
    for t in arange(-6.28, 6.28, 0.001):
        x = cos(3 * t)
        y = sin(5 * t)
        glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Curva de Lissajous (3:5)")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()

main()