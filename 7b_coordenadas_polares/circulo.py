import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawCircle():
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for i in range(180, 361 + 180): 
        theta = i * 2 * math.pi / 360 
        x = 16 * (math.sin(theta)) 
        y = 16 * (math.cos(theta))
        glVertex3f(x,y,0)
    glEnd()
    
def drawFunc():
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClear(GL_COLOR_BUFFER_BIT)
    # Cambiar la matriz de proyección
    glOrtho(-17.0, 17.0, -18.0, 17.0, -1.0, 1.0)
    drawCircle()
    glFlush()
    
#Programa Principal

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Circunferencia")
    glutDisplayFunc(drawFunc)
    glutMainLoop()
    