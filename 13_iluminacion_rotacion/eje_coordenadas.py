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

# Color inicial de la esfera
sphere_color = [1.0, 1.0, 1.0, 1.0]  # Rojo

def draw_axes():
    glLineWidth(3.0)  # Ajustar grosor de las líneas
    glBegin(GL_LINES)
    # Eje X (Rojo)
    # glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)
    # Eje Y (Verde)
    # glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)
    # Eje Z (Azul)
    # glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)
    glEnd()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            # Cambiar color con las teclas
            if event.key == pygame.K_r:  # Rojo
                sphere_color = [1.0, 0.0, 0.0, 1.0]
            if event.key == pygame.K_g:  # Verde
                sphere_color = [0.0, 1.0, 0.0, 1.0]
            if event.key == pygame.K_b:  # Azul
                sphere_color = [0.0, 0.0, 1.0, 1.0]

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

    # Dibujar ejes de coordenadas
    glPushMatrix()
    draw_axes()
    glPopMatrix()

    # Dibujar esfera
    glPushMatrix()
    glTranslatef(-1.5, 0, 0)

    # Configurar el material con el color deseado
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, sphere_color)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Activar la iluminación
    gluSphere(sphere, 1.0, 32, 16)
    glPopMatrix()

    # Movimiento
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
