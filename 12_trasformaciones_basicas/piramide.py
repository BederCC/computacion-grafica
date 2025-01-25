import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define los vértices de la pirámide
vertices = (
    (0, 1, 0),  # Vértice superior
    (-1, -1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1)
)

# Define las caras de la pirámide
caras = (
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 1),
    (1, 2, 3, 4)  # Base cuadrada
)

# Colores para cada cara
colores = (
    (1, 0, 0),  # Rojo
    (0, 1, 0),  # Verde
    (0, 0, 1),  # Azul
    (1, 1, 0),  # Amarillo
    (0, 1, 1),  # Cyan
)

def Piramide():
    glBegin(GL_QUADS)  # La base cuadrada
    glColor3fv(colores[4])
    for vertex in caras[4]:
        glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)  # Las caras laterales
    for i in range(4):
        glColor3fv(colores[i])
        for vertex in caras[i]:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    glRotatef(25, 2, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)

                if event.key == pygame.K_UP:
                    glTranslatef(0, 0.5, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -0.5, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.5)
                if event.button == 5:
                    glTranslatef(0, 0, -0.5)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Piramide()
        pygame.display.flip()
        pygame.time.wait(10)

main()
