import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)

def draw_triangle():
    glBegin(GL_TRIANGLES)

    # Vértice 1: arriba, color rojo
    glColor3f(1.0, 0.0, 0.0)
    glVertex3fv(vertices[0])

    # Vértice 2: abajo izquierda, color verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex3fv(vertices[1])

    # Vértice 3: abajo derecha, color azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex3fv(vertices[2])

    glEnd()

def EjesCoordenadas():
    glBegin(GL_LINES)

    # Eje X (blanco)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-6, -1.5, 0)
    glVertex3f(5, -1.5, 0)

    # Eje Y (blanco)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2, -5, 0)
    glVertex3f(-2, 5, 0)

    glEnd()

def draw_coordinates():
    font = pygame.font.Font(None, 36)
    text_surface = font.render('X: 0 Y: 0', True, (255, 255, 255))
    screen = pygame.display.get_surface()
    screen.blit(text_surface, (10, 10))

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    rotation_angle = 0
    zoom_factor = 1.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibuja los ejes sin aplicar la transformación
        EjesCoordenadas()

        # Aplica la transformación solo al triángulo
        glPushMatrix()

        # Rotación del triángulo
        glRotatef(rotation_angle, 0, 0, 0)
        rotation_angle += 1  # Ajusta la velocidad de rotación cambiando este valor

        # Zoom cuadrático del triángulo
        zoom_factor *= 0.99  # Reduce el zoom en cada iteración
        if zoom_factor < 0.01:  # Si el triángulo es muy pequeño, reinicia el zoom
            zoom_factor = 1.0
        glScalef(zoom_factor, zoom_factor, 1.0)

        draw_triangle()
        glPopMatrix()

        draw_coordinates()
        pygame.display.flip()
        pygame.time.wait(20)

if __name__ == "__main__":
    main()
