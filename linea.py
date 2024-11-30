from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glMatrixMode(GL_PROJECTION) 
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)

def linea():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(20, 15)  # Correcto uso de la función
    glVertex2f(60, 50)  # Correcto uso de la función
    glEnd() 
    glFlush()

# Modulo Principal main
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 300)  # Tamaño de la ventana
    glutInitWindowPosition(50, 100)
    glutCreateWindow(b"Grafica de la linea")  # Cadena codificada en bytes
    init()
    glutDisplayFunc(linea)
    glutMainLoop()

if __name__ == "__main__":
    main()
