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
sphere_color = [1.0, 1.0, 1.0, 1.0]  

def draw_axes():
    glLineWidth(3.0)  # Ajustar grosor de las líneas
    glBegin(GL_LINES)
    # Eje X (Rojo)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)
    # Eje Y (Verde)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)
    # Eje Z (Azul)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)
    glEnd()

def draw_planet(radius, distance, color, angle):
    glPushMatrix()
    glRotatef(angle, 0, 1, 0)  # Rotar alrededor del eje Y
    glTranslatef(distance, 0, 0)  # Alejar el planeta
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, color)
    gluSphere(sphere, radius, 32, 16)  # Crear el planeta
    glPopMatrix()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            # Cambiar color con las teclas
            if event.key == pygame.K_r:  # Rosa
                sphere_color = [1.0, 0.0, 0.5, 1.0]
            if event.key == pygame.K_a:  # Amarillo
                sphere_color = [1.0, 1.0, 0.0, 1.0]
            if event.key == pygame.K_b:  # Azul
                sphere_color = [0.0, 0.0, 1.0, 1.0]

    keypress = pygame.key.get_pressed()

    # Visualizar view matrix
    glLoadIdentity()

    # Inicializar el view matrix
    glPushMatrix()
    glLoadIdentity()

    # Rotación
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

    # Dibujar la esfera central (Sol)
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glRotate(1,0,3,0)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 0.85, 0.2, 1.0])  # Color amarillo para el sol
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Activar la iluminación
    gluSphere(sphere, 2.0, 32, 16)  # Sol
    glPopMatrix()

    # Dibujar los planetas (esferas pequeñas)
    draw_planet(0.5, 4, [0.2, 0.7, 0.3, 1.0], pygame.time.get_ticks() * 0.05)  # Planeta 1 verde musgo
    draw_planet(0.7, 6, [0.9, 0.9, 0.1, 1.0], pygame.time.get_ticks() * 0.03)  # Planeta 2 amarillo brillante
    draw_planet(0.3, 5, [0.6, 0.2, 0.8, 1.0], pygame.time.get_ticks() * 0.04)  # Planeta 3 lila
    draw_planet(0.3, 7, [0.3, 0.3, 0.7, 1.0], pygame.time.get_ticks() * 0.02)  # Planeta 4 azul oscuro
    draw_planet(0.3, 8, [1.0, 0.4, 0.5, 1.0], pygame.time.get_ticks() * 0.06)  # Planeta 5 rosa fuerte
    draw_planet(0.3, 9, [0.2, 0.9, 0.7, 1.0], pygame.time.get_ticks() * 0.08)  # Planeta 6 aguamarina
    draw_planet(0.3, 3, [0.7, 0.5, 0.1, 1.0], pygame.time.get_ticks() * 0.09)  # Planeta 7 marrón dorado

    # Movimiento
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
