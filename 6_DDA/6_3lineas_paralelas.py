import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0
width, height = 800, 600

def lineDDA(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    x, y = x1, y1
    while (x <= x2+1):
        glVertex2f(x, y)
        x += 1
        y += m

def line():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)

    # Dibujar tres líneas paralelas
    lineDDA(50, 200, 350, 500)  
    lineDDA(50, 100, 350, 400)  
    lineDDA(50, 0, 350, 300)  

    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Lineas Paralelas')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(line)
    glutMainLoop()

main()

