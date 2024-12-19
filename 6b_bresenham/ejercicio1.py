import sys
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window dimensions
window = 0
width, height = 800, 600

def lineaPuntoPendiente(x0, y0, xn, yn):
    """
    Implementa el algoritmo de punto pendiente para dibujar una línea
    desde (x0, y0) hasta (xn, yn).
    """
    m = (yn - y0) / (xn - x0)  # Calcular la pendiente
    b = y0 - m * x0  # Calcular la constante b
    x = x0
    while x <= xn:
        y = m * x + b  # Ecuación punto pendiente
        glVertex2f(x, y)  # Dibujar un punto en la posición (x, y)
        x += 1

def line():
    """
    Función para renderizar la escena.
    """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpiar la pantalla
    glBegin(GL_POINTS)  # Iniciar el dibujo en modo puntos
    glColor3f(0.0, 1.0, 0.0)  # Establecer el color de la línea
    lineaPuntoPendiente(50, 50, 350, 350)  # Llamar al algoritmo de punto pendiente
    glEnd()
    glutSwapBuffers()  # Intercambiar los buffers

def main():
    """
    Configuración inicial de la ventana y el entorno OpenGL.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Punto Pendiente")
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Color de fondo
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)  # Establecer el sistema de coordenadas
    glutDisplayFunc(line)  # Función de renderizado
    glutIdleFunc(line)  # Llamar continuamente a la función de renderizado
    glutMainLoop()  # Iniciar el bucle principal de GLUT

# Llamada al módulo principal
if __name__ == "__main__":
    main()
