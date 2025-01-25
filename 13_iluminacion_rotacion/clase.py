import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (800, 600)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)

# Crear una esfera
sphere = gluNewQuadric()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()
displayCenter = [screen.get_size()[i] // 2 for i in range(2)]

mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)
up_down_angle = 0.5
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False

    keypress = pygame.key.get_pressed()

    # Visualizar view matrix
    glLoadIdentity()

    # Inicializar el view matrix
    glPushMatrix()
    glLoadIdentity()

    # Rotacion
    up_down_angle += mouseMove[0] * 0.5
    glRotatef(up_down_angle, 0.0, 0.0, 1.0)  # Cambié el eje de rotación a Z

    # Aplicar los movimientos de tecla
    if keypress[pygame.K_UP]:
        glTranslatef(0, 0, 0.1)
    if keypress[pygame.K_DOWN]:
        glTranslatef(0, 0, -0.1)
    if keypress[pygame.K_LEFT]:
        glTranslatef(-0.1, 0, 0)
    if keypress[pygame.K_RIGHT]:
        glTranslatef(0.1, 0, 0)

    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    # Aplicar la matriz
    glPopMatrix()
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(-1.5, 0, 0)

    glColor4f(1.0, 0.5, 0.0, 1.0)  # Cambié el valor alfa a 1.0
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Cambié GL_LIGHT a GL_LIGHT0
    gluSphere(sphere, 1.0, 32, 16)
    glPopMatrix()

    # Movimiento
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
