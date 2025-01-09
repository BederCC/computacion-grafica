from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500

def draw_star_polygon():
    glColor3f(0.2, 0.7, 0.9)
    glBegin(GL_POLYGON)
    glVertex2f(350, 400)      
    glVertex2f(370, 350)
    glVertex2f(450, 350)
    glVertex2f(390, 300)
    glVertex2f(410, 250)
    glVertex2f(350, 280)
    glVertex2f(290, 250)      
    glVertex2f(310, 300)
    glVertex2f(250, 350)
    glVertex2f(330, 350)
    glEnd()

def draw_c_shape_polygon():

    glColor3f(0.9, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex2f(100, 150)
    glVertex2f(300, 150)
    glVertex2f(300, 200)
    glVertex2f(150, 200)
    glVertex2f(150, 300)
    glVertex2f(300, 300)
    glVertex2f(300, 320)
    glVertex2f(100, 350)
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
    draw_star_polygon()
    draw_c_shape_polygon()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("Polígonos Cóncavos en Diferentes Posiciones")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
