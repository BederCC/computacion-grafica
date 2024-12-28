from OpenGL.GL import *
from OpenGL.GLUT import *
import math

# Window dimensions
w, h = 500, 500

def draw_hexagon(x, y, size):
    """Draws a hexagon centered at (x, y) with the given size, rotated 90 degrees."""
    glBegin(GL_POLYGON)
    for i in range(6):
        angle = math.radians(i * 60 + 90)  # Rotate each vertex by 90 degrees
        glVertex2f(x + size * math.cos(angle), y + size * math.sin(angle))
    glEnd()

def draw_honeycomb():
    """Draws a honeycomb pattern with 7 hexagons."""
    size = 50  # Size of each hexagon
    offset = size * math.sqrt(3)  # Distance between hexagon centers

    # Define a list of colors for each hexagon
    colors = [
        (1, 0, 0),      # Red
        (0, 1, 0),      # Green
        (0, 0, 1),      # Blue
        (1, 1, 0),      # Yellow
        (1, 0, 1),      # Magenta
        (0, 1, 1),      # Cyan
        (1, 0.5, 0)     # Orange
    ]

    # Central hexagon
    glColor3f(*colors[0])  # Use the first color
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
        glColor3f(*colors[i + 1])  # Assign each surrounding hexagon a different color
        draw_hexagon(x, y, size)

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Apply a 90-degree rotation around the center (250, 250)
    glTranslatef(250, 250, 0)  # Move to the center
    glRotatef(90, 0, 0, 1)     # Rotate by 90 degrees around the Z axis
    glTranslatef(-250, -250, 0)  # Move back to the original position

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
