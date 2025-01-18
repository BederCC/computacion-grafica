import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

# Definición de los vértices del cubo
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Definición de los bordes del cubo
bordes = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

# Función para dibujar el cubo
def Cubo():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para los bordes
    for edge in bordes:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Función principal
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
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia la pantalla
        Cubo()  # Dibuja el cubo
        pygame.display.flip()  # Actualiza la pantalla
        pygame.time.wait(13)

# Ejecutar el programa
main()
