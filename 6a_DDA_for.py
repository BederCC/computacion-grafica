import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

width, height = 800, 600

def lineDDA(x1, y1, x2, y2):
    m=(y2-y1)/(x2-x1)
    x=x1
    y=y1
    for x in range(x1, x2 + 1):
        glVertex2f(x, y)
        y += m

def line():
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(1.0, 1.0, 0.0)
    lineDDA(50, 50, 350, 350)
    glEnd()
    glutSwapBuffers()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize (width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'linea DDA')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0) 
    glutDisplayFunc(line)
    glutIdleFunc(line)
    glutMainLoop()
main()