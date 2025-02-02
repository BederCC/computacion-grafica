# Gravitacion.py
# use in Python OpenGL/GLUT
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

# Establecer el ancho y alto de la ventana
global width, height
width = 800
height = 800

# Definir clases para las esferas
class Esfera:
    def __init__(self, x, y, z, vx, vy, vz, m, rad, color):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.m = m
        self.rad = rad
        self.color = color
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.trail = []

# Crear una lista de esferas
esferas = [
    Esfera(1.0, 0.0, 0.0, 0.0, 0.7, 0.1, 0.7, 0.07, (245, 230, 100)),
    Esfera(0.0, 1.1, 0.0, -0.7, 0.0, 0.1, 0.3, 0.03, (245, 150, 30)),
    Esfera(-1.0, 0.0, 0.0, 0.0, -0.5, 0.1, 0.5, 0.05, (100, 230, 245)),
    Esfera(0.0, -1.5, 0.0, 0.5, 0.0, 0.1, 0.6, 0.06, (30, 150, 245)),
    Esfera(1.3, 0.0, 0.0, 0.0, 0.3, 0.1, 0.4, 0.04, (30, 245, 150)), 
    Esfera(0.3, 1.4, 0.0, -0.3, 0.0, 0.1, 0.8, 0.08, (150, 245, 30)),
    Esfera(-1.5, 0.0, 0.0, 0.0, -0.2, 0.1, 0.3, 0.03, (245, 30, 150))
]

# constante gravitacional arbitraria "Big G"
G = 2.0

# Este valor mantiene una órbita suave en mi estación de trabajo. 
# Los valores más pequeños ralentizan la órbita, los valores más altos aceleran la órbita
dt = 0.001

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(w)/float(h), 1.0, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def keyboard(key, x, y):
    if key == chr(27):
        sys.exit()
    if key == b'q':
        sys.exit()

def orbits():
    global esferas, G, dt
    # Punto central alrededor del cual orbitan las esferas
    cx, cy, cz = 0.0, 0.0, 0.0
    cm = 1.0  # Masa del punto central (sol)

    for i in range(len(esferas)):
        esferas[i].ax = esferas[i].ay = esferas[i].az = 0
        
        # Calcular la fuerza gravitacional hacia el punto central
        dx = cx - esferas[i].x
        dy = cy - esferas[i].y
        dz = cz - esferas[i].z
        r2 = dx**2 + dy**2 + dz**2
        r3 = r2 * sqrt(r2)
        
        esferas[i].ax += G * dx * cm / r3
        esferas[i].ay += G * dy * cm / r3
        esferas[i].az += G * dz * cm / r3

    for esfera in esferas:
        esfera.vx += esfera.ax * dt
        esfera.vy += esfera.ay * dt
        esfera.vz += esfera.az * dt

        esfera.x += esfera.vx * dt
        esfera.y += esfera.vy * dt
        esfera.z += esfera.vz * dt

        # Guardar la posición actual en el rastro
        esfera.trail.append((esfera.x, esfera.y, esfera.z))

        # Limitar la longitud del rastro
        if len(esfera.trail) > 10000:  # Ajusta este valor para cambiar la longitud del rastro
            esfera.trail.pop(0)

    glutPostRedisplay()

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    for esfera in esferas:
        # Dibujar el rastro
        glBegin(GL_LINE_STRIP)
        glColor3ub(*esfera.color)
        for pos in esfera.trail:
            glVertex3f(pos[0], pos[1], pos[2])
        glEnd()

        # Dibujar la esfera
        glPushMatrix()
        glTranslatef(esfera.x, esfera.y, esfera.z)
        glColor3ub(*esfera.color)
        glutSolidSphere(esfera.rad, 10, 10)
        glPopMatrix()
    glutSwapBuffers()

def main():
    global width, height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Gravitacion Universal")
    glutReshapeFunc(reshape)
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(orbits)
    init()
    glutMainLoop()

main()
