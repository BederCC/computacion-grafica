import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# Variables globales para el radio y el color del círculo 
circle_radius = 5.0
circle_color = [1.0, 0.0, 0.0] # Inicialmente rojo
color_increment = [0.01, 0.01, 0.01] # Incremento para el cambio de color 
increasing_radius = True # Bandera para alternar entre expandir y contraer
def drawCircle():
    """Dibuja un círculo dinámico con el radio y el color actuales."""
    glColor3f(*circle_color)#El operador * desempaqueta los valores
    #de la lista o tupla, enviándolos como argumentos individuales a la función. 
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for i in range(360):
        theta = i * 2 * math.pi / 360
        x = circle_radius * math.cos(theta) 
        y = circle_radius * math.sin(theta) 
        glVertex2f(x, y)
    glEnd()
    

def updateCircle():
    """Actualiza el radio y el color del círculo dinámicamente."""
    global circle_radius, increasing_radius, circle_color, color_increment
    # Actualizar el radio
    if increasing_radius:
        circle_radius += 0.1
        if circle_radius >= 20.0: # Límite máximo
            increasing_radius = False
    else:
        circle_radius -= 0.1
        if circle_radius <= 5.0: # Límite mínimo 
            increasing_radius = True
    # Actualizar el color
    for i in range(3):
        circle_color[i] += color_increment[i]
        if circle_color[i] > 1.0 or circle_color[i] < 0.0:
            color_increment[i] = -color_increment[i]
    # Redibujar la pantalla
    glutPostRedisplay()
    
def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT) # Limpia el buffer de color, borrando la pantalla #para que no se acumulen los dibujos anteriores.
    glPushMatrix() # Guarda la matriz actual en la pila, permitiendo #aplicar transformaciones locales sin afectar la matriz global.
    drawCircle() # Llama a la función para dibujar el círculo en la escena. 
    glPopMatrix() # Restaura la última matriz guardada en la pila, #revirtiendo las transformaciones locales aplicadas.
    glFlush() # Fuerza a OpenGL a ejecutar todos los comandos pendientes, #asegurando que se renderice el dibujo en la pantalla.


def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA) #Configura el modo de visualiz #OpenGL con un único buffer de dibujo (GLUT_SINGLE)
    # #y colores basados en los canales RGBA (GLUT_RGBA).
    glutInitWindowSize(600, 600)
    glutCreateWindow("Círculo Dinámico")
    glClearColor(0.0, 0.0, 0.0, 0.0) # Fondo negro 
    gluOrtho2D(-25, 25, -25, 25) # Proyección ortogonal
    # Funciones de dibujo y animación
    #Llamar al main
    glutDisplayFunc (drawFunc)
    glutIdleFunc(updateCircle)
    glutMainLoop()
main()