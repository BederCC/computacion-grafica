from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glMatrixMode(GL_PROJECTION) 
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)

def linea_y_triangulo():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Triángulo con aristas de colores
    # Lado 1: Amarillo
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(20,15)
    glVertex2f(60,50)
    glEnd()

    # Lado 2: Verde
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(60,50)
    glVertex2f(100,15)
    glEnd()

    # Lado 3: Rojo
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(100,15)
    glVertex2f(20,15)
    glEnd()

    glFlush()

# Modulo Principal main
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 300)
    glutInitWindowPosition(50, 100)
    glutCreateWindow(b"Linea y Triangulo")
    init()
    glutDisplayFunc(linea_y_triangulo)
    glutMainLoop()

if __name__ == "__main__":
    main()
