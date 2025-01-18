import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

# Coordenadas de los vértices del cuadrado
vertices = (
    (1, -1, 0),
    (1, 1, 0),
    (-1, 1, 0),
    (-1, -1, 0)
)

# Definición de las caras del cuadrado
caras = [
    (0, 1, 2, 3)  # Cara formada por los vértices 0, 1, 2, 3
]

# Aristas del cuadrado (opcional para dibujar bordes)
bordes = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
)

# Colores (rojo, verde, azul, amarillo)
colores = [
    (1.0, 0.0, 0.0),  # Rojo
    (0.0, 1.0, 0.0),  # Verde
    (0.0, 0.0, 1.0),  # Azul
    (1.0, 1.0, 0.0)   # Amarillo
]

# Función para dibujar el cuadrado con colores
def dibujar_cuadrado():
    glBegin(GL_QUADS)  # Inicia el modo de dibujo de cuadriláteros
    for i, cara in enumerate(caras):
        glColor3fv(colores[i % len(colores)])  # Asigna un color a cada cara
        for vertice in cara:
            glVertex3fv(vertices[vertice])  # Dibuja los vértices de la cara
    glEnd()

# Función para dibujar los bordes del cuadrado
def dibujar_bordes():
    glBegin(GL_LINES)  # Inicia el modo de dibujo de líneas
    glColor3f(0.0, 0.0, 0.0)  # Color negro para los bordes
    for borde in bordes:
        for vertice in borde:
            glVertex3fv(vertices[vertice])  # Dibuja los vértices de los bordes
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glRotatef(1, 3, 1, 1)  # Rotación animada
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia el buffer
        dibujar_cuadrado()  # Dibuja el cuadrado con colores
        dibujar_bordes()  # Dibuja los bordes del cuadrado
        pygame.display.flip()  # Actualiza la pantalla
        pygame.time.wait(10)

main()
