import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

vertices = (
    (-1, -1, 0),
    (1, -1, 0),
    (0, 1, 0)
)

bordes = (
    (0, 1),
    (1, 2),
    (2, 0)
)

class OG1():
    @staticmethod
    def three_func(a, b, func):
        return (func(a[0], b[0]), func(a[1], b[1]), func(a[2], b[2]))

class GLCamera():
    def __init__(self):
        self.pos = [0.0, 0.0, 5.0]
        self.rot = [0.0, 0.0, 0.0]
        self.rotating = False
        self.mouse_pos = [0, 0]

    def add_to_scene(self):
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])
        
    def change_of_basis(self):
        c = np.cos(self.rot[1] * (np.pi / 180))
        s = np.sin(self.rot[1] * (np.pi / 180))
        m1 = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
        c = np.cos(self.rot[0] * (np.pi / 180))
        s = np.sin(self.rot[0] * (np.pi / 180))
        m2 = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
        m = m1.dot(m2)
        return m

    def handle_camera_events(self, event):
        if event.type == pygame.KEYDOWN:
            cb = self.change_of_basis()
            if event.key == pygame.K_RIGHT:
                m = np.dot(cb, np.array([-0.5, 0, 0]))
                self.pos = OG1.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_LEFT:
                m = np.dot(cb, np.array([0.5, 0, 0]))
                self.pos = OG1.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_UP:
                m = np.dot(cb, np.array([0, -0.5, 0]))
                self.pos = OG1.three_func(self.pos, m, lambda x, y: x + y)
            if event.key == pygame.K_DOWN:
                m = np.dot(cb, np.array([0, 0.5, 0]))
                self.pos = OG1.three_func(self.pos, m, lambda x, y: x + y)

def Triangulo():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    for edge in bordes:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    for vertex in vertices:
        glRasterPos3fv(vertex)
        for char in f"{vertex}":
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    camera = GLCamera()
    glutInit()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    while True:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        camera.add_to_scene()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            camera.handle_camera_events(event)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Triangulo()
        pygame.display.flip()
        pygame.time.wait(10)
main()
