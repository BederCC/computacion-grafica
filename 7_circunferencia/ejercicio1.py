from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import numpy as np
import math 
import sys 

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def keyboard(key, x, y):
    global color
    if key == b'r':  # Rojo
        color = [1.0, 0.0, 0.0]
    elif key == b'g':  # Verde
        color = [0.0, 1.0, 0.0]
    elif key == b'b':  # Azul
        color = [0.0, 0.0, 1.0]
    glutPostRedisplay()

def plotfunc():
    a, b, c, d = 0.5, 0.5, 0.25, 0.0
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)

    # Plot las coordenadas
    glBegin(GL_LINES)
    glVertex2f(-4.0, 0.0)  # Horizontal
    glVertex2f(4.0, 0.0)
    glVertex2f(0.0, 2.0)  # Vertical
    glVertex2f(0.0, -2.0)
    glEnd()

    # Plot los parámetros de la ecuación
    glPointSize(3) 
    glBegin(GL_POINTS)
    for t in np.arange(0, 15, 0.025):
        x = (c * t + d) * math.sin(t)
        y = math.sin(a * t + b)
        glColor3f(1, 0, 0)
        glVertex2f(x, y)
        y_cos = math.cos(a * t + b)
        glColor3f(0, 1, 0)
        glVertex2f(x, y_cos)
    glEnd()

    glFlush()

# End plotfunc()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 400)
    glutCreateWindow("Gráfica de las funciones Modificadas")
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

main()
# End of program
