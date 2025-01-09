from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w, h = 500, 500

def draw_polygon(x, y, radius, sides, color):
    glColor3f(*color)
    glBegin(GL_POLYGON)
    for i in range(sides):
        angle = 2 * math.pi * i / sides  # Ángulo en radianes
        glVertex2f(x + math.cos(angle) * radius, y + math.sin(angle) * radius)
    glEnd()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_polygon(150, 400, 50, 3, (1, 0, 0))  # Triángulo
    draw_polygon(350, 400, 50, 4, (0, 1, 0))  # Cuadrado
    draw_polygon(150, 250, 50, 5, (0, 0, 1))  # Pentágono
    draw_polygon(350, 250, 50, 6, (1, 1, 0))  # Hexágono
    draw_polygon(150, 100, 50, 7, (0, 1, 1))  # Heptágono
    draw_polygon(350, 100, 50, 8, (1, 0, 1))  # Octágono
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("Polígonos de Diferentes")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
