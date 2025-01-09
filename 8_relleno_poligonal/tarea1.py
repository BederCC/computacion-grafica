from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500, 500

def triangle_acutangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 1)
    glVertex2f(100, 300)
    glVertex2f(150, 450)
    glVertex2f(200, 300)
    glEnd()

def triangle_obtusangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 0)
    glVertex2f(300, 300)
    glVertex2f(450, 400)
    glVertex2f(350, 300)
    glEnd()

def triangle_rectangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 1)
    glVertex2f(200, 100)
    glVertex2f(300, 100)
    glVertex2f(200, 200)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    triangle_acutangulo()
    triangle_obtusangulo()
    triangle_rectangulo()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("Triángulos")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
