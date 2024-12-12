from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Inicialización de parámetros
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Color de fondo negro
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)  # Configuración del sistema de coordenadas

# Función para dibujar un cuadrado sin relleno
def draw_square(size):
    glColor3f(0.2, 0.5, 0.7)  # Color verde para el cuadrado
    glBegin(GL_LINE_LOOP)
    glVertex2f(-size, -size)
    glVertex2f(size, -size)
    glVertex2f(size, size)
    glVertex2f(-size, size)
    glEnd()

# Función para dibujar un triángulo equilátero sin relleno
def draw_triangle(size):
    glColor3f(1.0, 0.5, 0.3)  # Color rojo para el triángulo
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, size)               # Vértice superior
    glVertex2f(-size, -size)          # Vértice inferior izquierdo
    glVertex2f(size, -size)           # Vértice inferior derecho
    glEnd()

# Función principal de dibujo
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar el cuadrado en la parte izquierda
    glPushMatrix()
    glTranslatef(-30, 0, 0)  # Trasladar el cuadrado a la izquierda
    draw_square(20)          # Tamaño del cuadrado
    glPopMatrix()
    
    # Dibujar el triángulo en la parte derecha
    glPushMatrix()
    glTranslatef(30, 0, 0)   # Trasladar el triángulo a la derecha
    draw_triangle(20)        # Tamaño del triángulo (proporcional al cuadrado)
    glPopMatrix()
    
    glFlush()

# Módulo principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)  # Tamaño de la ventana
    glutInitWindowPosition(100, 100)  # Posición de la ventana
    glutCreateWindow(b"Cuadrado y Triangulo sin Relleno")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
