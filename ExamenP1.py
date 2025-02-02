from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0, 0.0, 0.0) 
    glPointSize(1.0)
    
    glBegin(GL_POINTS)
    for x in arange(0.0, 5.0, 0.01):
        for a in arange(0.0, 5.0, 0.01):
            if a > -x * x:
                glColor3f(0.50, 0.50, 0.50)
                glVertex2f(x, a)
            if a > x * x:
                glColor3f(1.00, 1.00, 1.00)
                glVertex2f(x, a)
    
    for x in arange(-5.0, 0.0, 0.01):
        for a in arange(0.0, 5.0, 0.01):
            if a > x * x or a < (0.8 * x + 1):
                glColor3f(0.50, 0.50, 0.50)
                glVertex2f(x, a)
            if a > x * x:
                glColor3f(1.00, 1.00, 1.00)
                glVertex2f(x, a)
    glEnd()
                
    glBegin(GL_POINTS)
    for x in arange(-5.0, 5.0, 0.01):
        y = x * x
        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(x, y)
    glEnd()
        
    # Ejes coordenados
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()

    # Agregar la linea oblicua
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, -3.0)
    glVertex2f(5.0, 5.0)
    glEnd()

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Function Plotter")  # Aquí se hace la conversión a bytes
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()

main()
