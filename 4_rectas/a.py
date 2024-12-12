from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
from numpy import * 
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def plotfun():
    glClear(GL_COLOR_BUFFER_BIT) 

    # Dibujar ejes
    glColor3f(0.0, 0.0, 0.0)  # Color negro
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)  # Eje X
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, -5.0)  # Eje Y
    glVertex2f(0.0, 5.0)
    glEnd()

    # Graficar y = x^2 - 2
    glColor3f(1.0, 0.0, 0.0)  # Color rojo
    glPointSize(5.0)  # Tamaño del punto (en píxeles)
    glBegin(GL_POINTS)
    for x in arange(-5.0, 5.0, 0.05):
        y = x**2 - 2
        glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Graficas de Funciones")
    glutDisplayFunc(plotfun)
    init()
    glutMainLoop()

# Ejecutar programa
main()
