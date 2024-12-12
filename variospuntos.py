import pygame as pg
from pygame.locals import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
    glClearColor(0.244, 0.132, 0.247, 1.0) # Establece el color de fondo (negro)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Establece las coordenadas del espacio 2D
    
def plot_points(): # Función para dibujar puntos
    glClear(GL_COLOR_BUFFER_BIT) # Limpia el buffer de color
    glPointSize(10.0) # Tamaño de los puntos
    
    # Lista de coordenadas y colores (r, g, b)
    points = [
        ((0.1, 0.2), (1.0, 1.0, 0.0)),   
        ((-0.3, 0.5), (0.0, 1.0, 1.0)),  
        ((0.2, -0.5), (0.0, 0.0, 1.0)),  
        ((0.4, 0.7), (1.0, 0.1, 0.0)),   
        ((-0.1, -0.7), (1.0, 1.0, 1.0))  
    ]
    
    glBegin(GL_POINTS) # Inicia el dibujo de puntos
    for (x, y), (r, g, b) in points:
        glColor3f(r, g, b)  # Establece el color del punto
        glVertex2f(x, y)    # Dibuja el punto
    glEnd() # Finaliza el dibujo de puntos
    
    glFlush() # Ejecuta los comandos

# Inicializa la ventana y configura OpenGL
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow(b"OpenGL Window")
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_points)
clearScreen()
glutMainLoop()
