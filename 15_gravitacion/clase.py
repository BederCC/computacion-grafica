# Gravitacion.py
# use in Python OpenGL/GLUT
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

# Establecer el ancho y alto de la ventana
global width
global height

# Valores iniciales
width = 500
height = 500

# valores iniciales de posición, componentes de velocidad y tiempo de incremento
global vx1, vy1, vz1, x1, y1, z1, r2, r3, ax1, ay1, az1, dt
global vx2, vy2, vz2, x2, y2, z2, ax2, ay2, az2, G

# posiciones iniciales x, y, z para ambas estrellas
x1 = 1.0
y1 = 0.0
z1 = 0.0
x2 = -1.0
y2 = 0.0
z2 = 0.0

# velocidades iniciales vx, vy, vz para ambas estrellas
vx1 = 0.0
vy1 = -0.128571428
vz1 = 0.0
vx2 = 0.0
vy2 = 0.3
vz2 = 0.0

# masas iniciales para ambas estrellas
m1 = 0.7
m2 = 0.3
rad1 = 0.1 * m1
rad2 = 0.1 * m2

# constante gravitacional arbitraria "Big G"
G = 1.0

# calcular la distancia y el denominador r**3 para la gravitación universal
r2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
r3 = r2 * sqrt(r2)

# calcular componentes de aceleración a lo largo de los ejes x, y, z
# Primero para m1
ax1 = -G * (x1 - x2) * m2 / r3
ay1 = -G * (y1 - y2) * m2 / r3
az1 = -G * (z1 - z2) * m2 / r3

# ahora para m2
ax2 = -G * (x2 - x1) * m1 / r3
ay2 = -G * (y2 - y1) * m1 / r3
az2 = -G * (z2 - z1) * m1 / r3

# Este valor mantiene una órbita suave en mi estación de trabajo. 
# Los valores más pequeños ralentizan la órbita, los valores más altos aceleran la órbita
dt = 0.001

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def reshape(w, h):
    # Para asegurarnos de que no tenemos una altura cero
    if h == 0:
        h = 1

    # ¡Llene toda la ventana de gráficos!
    glViewport(0, 0, w, h)

    # Establecer la matriz de proyección... nuestra "vista"
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Establecer cómo vemos el mundo y posicionar nuestro globo ocular 
    gluPerspective(45.0, float(w)/float(h), 1.0, 1000.0)

    # Establecer la matriz para el objeto que estamos dibujando. 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Coloque la posición de la cámara, la dirección de la vista. y cual eje es ARRIBA
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def keyboard(key, x, y):
    # Nos permite salir pulsando 'Esc' o 'q'
    if key == chr(27):
        sys.exit()
    if key == 'q':
        sys.exit()

def orbits():
    global vx1, vy1, vz1, x1, y1, z1, r2, r3, ax1, ay1, az1
    global vx2, vy2, vz2, x2, y2, z2, ax2, ay2, az2
    
    # calcular la mitad frontal de los componentes del vector de velocidad 
    vx1 += 0.5 * ax1 * dt
    vy1 += 0.5 * ay1 * dt 
    vz1 += 0.5 * az1 * dt 
    vx2 += 0.5 * ax2 * dt 
    vy2 += 0.5 * ay2 * dt 
    vz2 += 0.5 * az2 * dt

    # calcular las posiciones x, y, z para ambas estrellas
    x1 += vx1 * dt
    y1 += vy1 * dt
    z1 += vz1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt
    z2 += vz2 * dt

    # calcular el nuevo denominador r**3 para cada posición de estrella 
    r2 = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 
    r3 = r2 * sqrt(r2)

    # calcular los nuevos componentes de aceleración
    ax1 = -G * (x1 - x2) * m2 / r3
    ay1 = -G * (y1 - y2) * m2 / r3
    az1 = -G * (z1 - z2) * m2 / r3
    ax2 = -G * (x2 - x1) * m1 / r3
    ay2 = -G * (y2 - y1) * m1 / r3
    az2 = -G * (z2 - z1) * m1 / r3

    # calcular los componentes de velocidad de la mitad trasera 
    vx1 += 0.5 * ax1 * dt
    vy1 += 0.5 * ay1 * dt 
    vz1 += 0.5 * az1 * dt
    vx2 += 0.5 * ax2 * dt
    vy2 += 0.5 * ay2 * dt
    vz2 += 0.5 * az2 * dt

    # enviar las posiciones calculadas de las estrellas x, y, z a la pantalla
    glutPostRedisplay()

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)

    # trazar la posición de la primera estrella (m1)
    glPushMatrix()
    glTranslatef(x1, y1, z1)
    glColor3ub(245, 230, 100)
    glutSolidSphere(rad1, 10, 10)
    glPopMatrix()

    # trazar la posición de la segunda estrella (m2) 
    glPushMatrix()
    glTranslatef(x2, y2, z2)
    glColor3ub(245, 150, 30)
    glutSolidSphere(rad2, 10, 10) 
    glPopMatrix()

    # intercambiar los búferes de dibujo 
    glutSwapBuffers()

def main():
    global width
    global height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Gravitacion Universal")  # Usa una cadena de bytes
    glutReshapeFunc(reshape)
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(orbits)
    init()
    glutMainLoop()


main()
