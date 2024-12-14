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
color = [0.0, 1.0, 0.0] # Verde inicial
# Algoritmo de Bresenham
def Bresline(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1) 
    slope = dy/float(dx)
    x, y = x1, y1
    
    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x 
        x1, y1 = y1, x1
        x2, y2 = y2, x2 
    p = 2 * dy - dx
    
    glVertex2f(x, y)
    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy
        x = x + 1 if x < x2 else x - 1
        time.sleep(0.01)
        glVertex2f(x, y)

# Manejo del mouse para dibujar líneas def mouseInput(button, state, x, y):
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

# Manejo del teclado para cambiar colores
def keyboard (key, x, y):
    global color
    if key == b'r': # Rojo
        color = [1.0, 0.0, 0.0]
    elif key ==b'g':
        color = [0.0, 1.0, 0.0]
    elif key == b'b':
        color = [0.0, 0.0, 1.0]
    glutPostRedisplay()
# Dibujar las líneas
def drawLines():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    glColor3f(*color)
    for x1, y1, x2, y2 in lines:
        Bresline(x1, y1, x2, y2)
    glEnd()
    glutSwapBuffers()
    
# Configuración principal de la ventana
def main():
    global width, height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Algoritmo de Bresenham')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, width, 0.0, height)
    # Asignar funciones
    glutDisplayFunc(drawLines)
    glutMouseFunc(mouseInput)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
if __name__=="__main__":
    main()