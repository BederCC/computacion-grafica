import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def dibujarPunto(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def circulo(Xc, Yc, r):
    X = 0
    Y = r
    while X <= Y:
        dibujarPunto(X + Xc, Y + Yc)
        dibujarPunto(-X + Xc, Y + Yc)
        dibujarPunto(X + Xc, -Y + Yc)
        dibujarPunto(-X + Xc, -Y + Yc)
        dibujarPunto(Y + Xc, X + Yc)
        dibujarPunto(-Y + Xc, X + Yc)
        dibujarPunto(Y + Xc, -X + Yc)
        dibujarPunto(-Y + Xc, -X + Yc)

        X += 1
        Y = math.sqrt(r**2 - X**2)

def drawFunc():
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClear(GL_COLOR_BUFFER_BIT)
    glOrtho(-20.0, 20.0, -20.0, 20.0, -1.0, 1.0)
    circulo(0, 0, 15)
    glFlush()
    
if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Circunferencia Canonica")
    glutDisplayFunc(drawFunc)
    glutMainLoop()
