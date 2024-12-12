from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
# Coordenadas de los puntos
points = {
    'C': (1, 1),
    'D': (0, 2),
    'E': (2, 2),
    'F': (3, 3),
    'G': (4, 2),
    'H': (6, 2),
    'I': (5, 1),
    'J': (1, 1)
}
# Función de inicialización
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Color de fondo blanco
    glColor3f(0.0, 0.0, 0.0)  # Color de las líneas negro
    glPointSize(8.0)  # Tamaño de los puntos
    glLineWidth(2.0)  # Grosor de las líneas
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1, 7, -1, 5)  # Configuración del sistema de coordenadas
# Función para dibujar los puntos
def draw_points():
    glColor3f(0.0, 0.0, 1.0)  # Color azul para los puntos
    glBegin(GL_POINTS)
    for p in points.values():
        glVertex2f(*p)
    glEnd()
# Función para dibujar las líneas conectando los puntos
def draw_lines():
    glColor3f(0.0, 0.0, 0.0)  # Color negro para las líneas
    glBegin(GL_LINE_STRIP)
    glVertex2f(*points['C'])
    glVertex2f(*points['D'])
    glVertex2f(*points['E'])
    glVertex2f(*points['F'])
    glVertex2f(*points['G'])
    glVertex2f(*points['H'])
    glVertex2f(*points['I'])
    glVertex2f(*points['J'])
    glEnd()
# Función principal de dibujo
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_points()
    draw_lines()
    glFlush()
# Módulo principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)  # Tamaño de la ventana
    glutInitWindowPosition(100, 100)  # Posición de la ventana
    glutCreateWindow(b"Figura con Puntos y Lineas")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
if __name__ == "__main__":
    main()
