import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0
width, height = 800, 600

def lineDDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))  
    incx = dx / steps if steps != 0 else 0
    incy = dy / steps if steps != 0 else 0

    x, y = x1, y1
    glBegin(GL_LINE_STRIP)  
    for _ in range(int(steps) + 1):  
        glVertex2f(x, y)
        x += incx
        y += incy
    glEnd()

def line():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    # Dibujar la recta y = (1/3)x entre los puntos (0,0) y (12,4)
    lineDDA(0, 0, 12, 4)

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Recta con DDA')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 15.0, -1.0, 5.0)  # Ajuste del espacio de dibujo para mejor visualización
    glutDisplayFunc(line)
    glutMainLoop()

main()
