from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT import *
import math

# Window dimensions
w, h = 500, 500

def draw_hexagon(x, y, size):
    """Draws a hexagon centered at (x, y) with the given size."""
    glBegin(GL_POLYGON)
    for i in range(6):
        angle = math.radians(i * 60)
        glVertex2f(x + size * math.cos(angle), y + size * math.sin(angle))
    glEnd()

def draw_honeycomb():
    """Draws a honeycomb pattern with 7 hexagons."""
    size = 50  # Size of each hexagon
    offset = size * math.sqrt(3)  # Distance between hexagon centers

    # Central hexagon
    glColor3f(1, 0.5, 0)  # Orange color
    draw_hexagon(250, 250, size)

    # Surrounding hexagons
    positions = [
        (250 + offset, 250),  # Right
        (250 - offset, 250),  # Left
        (250 + offset / 2, 250 + 1.5 * size),  # Top-right
        (250 - offset / 2, 250 + 1.5 * size),  # Top-left
        (250 + offset / 2, 250 - 1.5 * size),  # Bottom-right
        (250 - offset / 2, 250 - 1.5 * size)   # Bottom-left
    ]

    for i, (x, y) in enumerate(positions):
        glColor3f((i + 1) % 2, (i + 2) % 2, (i + 3) % 2)  # Different colors
        draw_hexagon(x, y, size)

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
    draw_honeycomb()
    glutSwapBuffers()

# Main program
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("Honeycomb Pattern")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
