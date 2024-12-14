
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
    glClear (GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0, 0.0, 0.0) 
    glPointSize(1.0)
    # Plot las cordenadas
    glBegin(GL_LINES)
    glVertex2f(-2.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, -2.0)
    glEnd()
    
# Plot los parametros de la ecuacion 
    for t in arange(0.0,6.28, 0.001):
        x = sin(t)
        y = cos(t)
        glBegin(GL_POINTS) 
        glVertex2f(x, y)
        glEnd()
        glFlush()
# End plotfunc()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition (50,50)
    glutInitWindowSize (400,400)
    glutCreateWindow("Grafica de la circunferencia")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()
main()
# End of program