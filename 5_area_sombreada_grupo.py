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
    
    # Dibujar la parábola
    for x in arange(-5.0, 5.0, 0.01):
        y = x * x
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
    
    # Sombrear la región encerrada entre la parábola y la pendiente
    for x in arange(-5.0, 5.0, 0.01):  # Ajustar el rango de x para la región encerrada
        y_parabola = x * x
        y_line = x + 2
        if y_parabola < y_line:
            for y in arange(y_parabola, y_line, 0.01):
                glColor3f(0.5, 0.5, 0.5)
                glBegin(GL_POINTS)
                glVertex2f(x, y)
                glEnd()
    
    # Dibujar los ejes
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
    
    # Dibujar la línea oblicua
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, -3.0)
    glVertex2f(5.0, 7.0)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Function Plotter")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()

main()