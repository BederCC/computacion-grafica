from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import sys

# Parámetros de la ventana
width, height = 500, 500
axrng = 2.0
num_points = 50000  # Número de puntos para generar rápidamente el fractal

def init():
    """Configuración inicial de OpenGL."""
    glClearColor(1.0, 1.0, 1.0, 0.0)  # Fondo blanco
    glColor3f(0.0, 0.0, 0.0)  # Color negro para los puntos
    glPointSize(1.0)  # Tamaño de los puntos

def sierpinski():
    """Genera y dibuja los puntos del Triángulo de Sierpinski."""
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)

    # Vértices del triángulo
    verts = [[0.0, 2.0], [-2.0, -2.0], [2.0, -2.0]]

    # Punto inicial
    x, y = -1.5, 0.75

    # Generación de puntos
    for _ in range(num_points):
        v = random.randint(0, 2)  # Selecciona un vértice aleatorio
        x = (x + verts[v][0]) / 2
        y = (y + verts[v][1]) / 2
        glVertex2f(x, y)  # Dibuja el punto

    glEnd()
    glFlush()

def reshape(w, h):
    """Mantiene la proporción de la ventana."""
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        gluOrtho2D(-axrng, axrng, -axrng * h / w, axrng * h / w)
    else:
        gluOrtho2D(-axrng * w / h, axrng * w / h, -axrng, axrng)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyboard(key, x, y):
    """Permite cerrar la ventana con la tecla 'q' o 'Esc'."""
    if key == b'\x1b' or key == b'q':  # Tecla Esc o 'q'
        sys.exit()

def main():
    """Función principal para inicializar OpenGL y la ventana."""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Triangulo de Sierpinski con OpenGL")  # Asegurarse de que el título sea un string tipo bytes

    init()
    glutReshapeFunc(reshape)
    glutDisplayFunc(sierpinski)
    glutKeyboardFunc(keyboard)

    glutMainLoop()

# Ejecutar el programa
main()
