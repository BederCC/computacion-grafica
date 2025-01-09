import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def dibujarPunto(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def circuloPolar(Xc, Yc):
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        theta = math.radians(i)
        r = 4 * math.cos(theta) + 2
        x = Xc + r * math.cos(theta)
        y = Yc + r * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

def drawFunc():
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClear(GL_COLOR_BUFFER_BIT)
    glOrtho(-20.0, 20.0, -20.0, 20.0, -1.0, 1.0)
    circuloPolar(0, 0)
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Curva Polar con Ecuaciones")
    glutDisplayFunc(drawFunc)
    glutMainLoop()
