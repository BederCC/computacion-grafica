import pygame  # Importa el módulo pygame para manejar gráficos y eventos de ventana
from pygame.locals import *  # Importa constantes y funciones de pygame para facilitar el acceso
from OpenGL.GL import *  # Importa funciones OpenGL para gráficos 3D
from OpenGL.GLUT import *  # Importa funciones adicionales de OpenGL para gráficos
from OpenGL.GLU import *  # Importa funciones de utilidad de OpenGL para configuraciones de perspectiva

# Definir los vértices del triángulo en coordenadas (x, y, z)
vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)

# Definir los bordes del triángulo, indicando índices de vértices
bordes = (
    (0, 1),  # Borde entre vértices 0 y 1
    (1, 2),  # Borde entre vértices 1 y 2
    (2, 0)   # Borde entre vértices 2 y 0
)

# Cambia el color del triángulo a rojo
color = (1.0, 0.0, 0.0)  # Rojo (RGB)

# Función para dibujar el triángulo
def dibujar_triangulo():
    glBegin(GL_TRIANGLES)  # Inicia el modo de dibujo de triángulos en OpenGL
    glColor3fv(color)  # Establece el color actual para los vértices (rojo)
    for vertice in vertices:
        glVertex3fv(vertice)  # Dibuja cada vértice del triángulo con sus coordenadas
    glEnd()  # Finaliza el dibujo de triángulos

# Función para dibujar los bordes del triángulo
def dibujar_bordes():
    glBegin(GL_LINES)  # Inicia el modo de dibujo de líneas en OpenGL
    glColor3f(0.0, 0.0, 0.0)  # Establece el color de los bordes (negro)
    for borde in bordes:
        for vertice in borde:
            glVertex3fv(vertices[vertice])  # Dibuja cada borde del triángulo
    glEnd()  # Finaliza el dibujo de líneas

# Función para dibujar los ejes de coordenadas
def dibujar_ejes():
    glBegin(GL_LINES)  # Inicia el modo de dibujo de líneas en OpenGL
    # Eje x
    glColor3f(1.0, 1.0, 1.0)  # Color rojo para el eje x
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)
    # Eje y
    glColor3f(1.0, 1.0, 1.0)  # Color verde para el eje y
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)
    glEnd()  # Finaliza el dibujo de líneas

# Función para rotar el triángulo según un ángulo dado
def rotar_triangulo(angle):
    glRotatef(angle, 0, 1, 0)  # Aplica una rotación al triángulo alrededor del eje y

# Función principal del programa
def main():
    pygame.init()  # Inicializa pygame para manejar la ventana y los eventos
    display = (800, 600)  # Tamaño de la ventana
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # Crea una ventana OpenGL con doble buffer
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Establece la perspectiva de visualización
    glTranslatef(0.0, 0.0, -5)  # Traslada la escena en el eje z hacia adelante
    
    angle = 0  # Ángulo inicial de rotación
    
    while True:
        for event in pygame.event.get():  # Manejo de eventos de pygame
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                pygame.quit()  # Finaliza pygame
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia el buffer de color y profundidad
        
        # Dibuja los ejes de coordenadas en su posición fija
        dibujar_ejes()
        
        # Guarda la matriz de transformaciones actual, rota y dibuja el triángulo, y restaura la matriz
        glPushMatrix()
        glTranslatef(0, 0, 0)  # Traslada el triángulo al origen
        glRotatef(angle, 0, 1, 0)  # Aplica una rotación al triángulo
        dibujar_triangulo()  # Dibuja el triángulo en su posición actual
        dibujar_bordes()  # Dibuja los bordes del triángulo
        glPopMatrix()
        
        angle += 1  # Incrementa el ángulo de rotación
        
        pygame.display.flip()  # Actualiza la ventana con el contenido dibujado
        pygame.time.wait(10)  # Espera un breve lapso de tiempo antes de la próxima iteración

main()  # Llama a la función principal para ejecutar el programa
