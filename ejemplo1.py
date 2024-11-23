from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

print('hola')

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

# Módulo principal
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Proyecto de beder")  # Pasar el título de la ventana como bytes
glutDisplayFunc(showScreen)  # Vincula la función de renderizado
glutIdleFunc(showScreen)  # Vincula la función de animación
glutMainLoop()  # Inicia el bucle principal de GLUT





# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# def init():
#     glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
#     glOrtho(-1, 1, -1, 1, -1, 1)  # Configurar el espacio de proyección

# def draw():
#     glClear(GL_COLOR_BUFFER_BIT)  # Limpia la pantalla

#     glBegin(GL_TRIANGLES)  # Empieza a dibujar un triángulo
#     glColor3f(1.0, 0.0, 0.0)  # Rojo
#     glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
#     glColor3f(0.0, 1.0, 0.0)  # Verde
#     glVertex2f(0.5, -0.5)  # Vértice inferior derecho
#     glColor3f(0.0, 0.0, 1.0)  # Azul
#     glVertex2f(0.0, 0.5)  # Vértice superior
#     glEnd()  # Termina de dibujar el triángulo

#     glFlush()  # Ejecuta los comandos de renderizado

# # Módulo principal
# glutInit()
# glutInitDisplayMode(GLUT_RGB)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)
# glutCreateWindow(b"Triangulo OpenGL")
# glutDisplayFunc(draw)  # Configura la función de dibujo
# init()  # Inicialización de parámetros
# glutMainLoop()  # Inicia el bucle principal de GLUT