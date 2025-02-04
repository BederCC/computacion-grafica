import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (800, 600)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)
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
sphere_color = [1.0, 0.0, 0.0, 1.0]
spheres = [
    {"pos": (-3.0, 0, 0), "size": 0.5, "color": [1.0, 0.5, 0.0, 1.0]},  
    {"pos": (-1.0, 0, 0), "size": 0.8, "color": [0.0, 1.0, 0.5, 1.0]},  
    {"pos": (1.0, 0, 0), "size": 1.2, "color": [0.0, 0.6, 1.0, 1.0]}, 
    {"pos": (3.0, 0, 0), "size": 0.75, "color": [1.0, 1.5, 0.0, 1.0]}
]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False

    keypress = pygame.key.get_pressed()
    glLoadIdentity()
    glPushMatrix()
    glLoadIdentity()
    up_down_angle += mouseMove[0] * 0.5
    glRotatef(up_down_angle, 0.0, 0.0, 1.0)
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
    glPopMatrix()
    glMultMatrixf(viewMatrix)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for sphere_data in spheres:
        glPushMatrix()
        glTranslatef(*sphere_data["pos"])
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, sphere_data["color"])
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        gluSphere(sphere, sphere_data["size"], 32, 16)
        glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
