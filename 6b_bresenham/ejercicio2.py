import sys
import time
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Configuración inicial de la ventana
window = 0
width, height = 800, 600

# Variables globales
lines = []
x_start, y_start = 0, 0
x_end, y_end = 0, 0
is_drawing = False
color = [0.0, 1.0, 0.0]  # Verde inicial

def lineaPuntoPendiente(x0, y0, xn, yn):
    """
    Algoritmo para dibujar una línea con pendiente arbitraria usando
    la ecuación punto-pendiente.
    """
    if xn == x0:  # Línea vertical
        for y in range(min(y0, yn), max(y0, yn) + 1):
            glVertex2f(x0, y)
    else:
        m = (yn - y0) / (xn - x0)  # Calcular la pendiente
        b = y0 - m * x0  # Calcular la constante b

        x = x0
        while x <= xn:
            y = m * x + b  # Ecuación punto-pendiente
            glVertex2f(x, round(y))  # Dibujar un punto en la posición (x, y)
            x += 1 if x0 < xn else -1

def mouseInput(button, state, x, y):
    global x_start, y_start, x_end, y_end, is_drawing
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x_start, y_start = x, height - y
        is_drawing = True
    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        x_end, y_end = x, height - y
        is_drawing = False
        lines.append((x_start, y_start, x_end, y_end))
        glutPostRedisplay()

def keyboard(key, x, y):
    global color
    if key == b'r':  # Rojo
        color = [1.0, 0.0, 0.0]
    elif key == b'g':  # Verde
        color = [0.0, 1.0, 0.0]
    elif key == b'b':  # Azul
        color = [0.0, 0.0, 1.0]
    glutPostRedisplay()

def drawLines():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    glColor3f(*color)
    for x1, y1, x2, y2 in lines:
        if abs(y2 - y1) > abs(x2 - x1):  # Verificar la pendiente
            # Intercambiar coordenadas para líneas con pendiente pronunciada
            lineaPuntoPendiente(y1, x1, y2, x2)
        else:
            lineaPuntoPendiente(x1, y1, x2, y2)
    glEnd()
    glutSwapBuffers()

def main():
    global width, height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Algoritmo de Lineas con Pendiente Arbitraria')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, width, 0.0, height)
    # Asignar funciones
    glutDisplayFunc(drawLines)
    glutMouseFunc(mouseInput)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
