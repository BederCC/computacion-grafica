from OpenGL.GL import* 
from OpenGL.GLU import* 
from OpenGL.GLUT import* 
from numpy import*
import sys
def init():
    glClearColor(1.0,1.0,1.0,1.0) 
    gluOrtho2D(-5.0,5.0, -5.0,5.0)
def plotfun():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0,0.0,0.0)
    glPointSize(3.0)
    for x in arange(-5.0, 5.0, 0.1):
        y=2*x+7
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition (50,50)
    glutInitWindowSize (500,500)
    glutCreateWindow("Ecuacion de la Recta")
    glutDisplayFunc(plotfun)
    init()
    glutMainLoop()
    #Ejecutamos
main()