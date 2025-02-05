import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Luz(object):
    encendida = True
    colores = [(1., 1., 1., 1.), (1., 0.5, 0.5, 1.), 
               (0.5, 1., 0.5, 1.), (0.5, 0.5, 1., 1.)]

    def __init__(self, luz_id, posicion):
        self.luz_id = luz_id
        self.posicion = posicion
        self.color_actual = 0

    # Iluminación
    def iluminar(self):
        light_id = self.luz_id
        color = Luz.colores[self.color_actual]
        glLightfv(light_id, GL_POSITION, self.posicion)
        glLightfv(light_id, GL_DIFFUSE, color)
        glLightfv(light_id, GL_CONSTANT_ATTENUATION, 0.1)
        glLightfv(light_id, GL_LINEAR_ATTENUATION, 0.05)

    def cambiar_color(self):
        self.color_actual += 1
        self.color_actual %= len(Luz.colores)

    def enable(self):
        if not Luz.encendida:
            glEnable(GL_LIGHTING)
            Luz.encendida = True
        glEnable(self.luz_id)

# --Construcción de la esfera
class Esfera(object):
    meridiano = 40
    paralelos = 40

    # Constructor
    def __init__(self, radio, posicion, color):
        self.radio = radio
        self.posicion = posicion
        self.color = color

    # Dibujar la esfera
    def dibujar(self):
        glPushMatrix()
        glTranslatef(*self.posicion)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.color)
        glutSolidSphere(self.radio, Esfera.meridiano, Esfera.paralelos)
        glPopMatrix()

# --Sistema Planetario----
class Planetario(object):
    def __init__(self, largo=800, ancho=600):
        self.titulo = 'Sistema planetario'
        self.largo = largo
        self.ancho = ancho
        self.angulo = 0
        self.distancia = 20
        self.iluminacion = Luz(GL_LIGHT0, (15, 5, 15, 1))
        # Crear las esferas (planetas)
        self.planetas = [
            Esfera(0.5, (4, 0, 0), (0.8, 0.4, 0.1, 1.0)),  # Planeta 1 café
            Esfera(0.7, (6, 0, 0), (1.0, 0.75, 0.0, 1.0)),  # Planeta 2 ámbar
            Esfera(0.3, (5, 0, 0), (1.0, 1.0, 0.6, 1.0)),  # Planeta 3 amarillo
            Esfera(0.3, (7, 0, 0), (0.2, 0.6, 0.8, 1.0)),  # Planeta 4 azul
            Esfera(0.3, (8, 0, 0), (0.5, 0.0, 0.4, 1.0)),  # Planeta 5 morado
            Esfera(0.3, (9, 0, 0), (0.75, 0.0, 1.0, 1.0)),  # Planeta 6 púrpura
            Esfera(0.3, (3, 0, 0), (0.2, 0.8, 0.2, 1.0))   # Planeta 7 verde
        ]

    def iniciar(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowPosition(50, 50)
        glutInitWindowSize(self.largo, self.ancho)
        glutCreateWindow(self.titulo)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        self.iluminacion.enable()
        glClearColor(.1, .1, .1, 1)
        aspect = self.largo / self.ancho
        glMatrixMode(GL_PROJECTION)
        gluPerspective(40., aspect, 1., 40.)
        glMatrixMode(GL_MODELVIEW)
        glutDisplayFunc(self.dibujar)
        glutSpecialFunc(self.keyboard)
        glutIdleFunc(self.actualizar)
        glutMainLoop()

    def dibujar(self):
        x = math.sin(self.angulo) * self.distancia
        z = math.cos(self.angulo) * self.distancia
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(x, 0, 2, 0, 0, 0, 0, 1, 0)

        self.iluminacion.iluminar()

        # Dibujar cada planeta
        for planeta in self.planetas:
            planeta.dibujar()

        glutSwapBuffers()

    def keyboard(self, tecla, x, y):
        if tecla == GLUT_KEY_INSERT:
            sys.exit()
        if tecla == GLUT_KEY_UP:
            self.distancia -= 0.1
        if tecla == GLUT_KEY_DOWN:
            self.distancia += 0.1
        if tecla == GLUT_KEY_LEFT:
            self.angulo -= 0.05
        if tecla == GLUT_KEY_RIGHT:
            self.angulo += 0.05
        if tecla == GLUT_KEY_F1:
            self.iluminacion.cambiar_color()
        self.distancia = max(10, min(self.distancia, 20))
        self.angulo %= math.pi * 2
        glutPostRedisplay()

    def actualizar(self):
        glutPostRedisplay()

if __name__ == '__main__':
    Aplicar = Planetario()
    Aplicar.iniciar()
