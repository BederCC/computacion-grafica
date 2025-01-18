import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

# Definición de los vértices de la pirámide
vertices = (
    (0, 1, 0),    # Vértice superior
    (1, -1, 1),   # Esquina frontal derecha
    (-1, -1, 1),  # Esquina frontal izquierda
    (-1, -1, -1), # Esquina trasera izquierda
    (1, -1, -1)   # Esquina trasera derecha
)

# Definición de las caras de la pirámide
caras = (
    (0, 1, 2),  # Cara frontal
    (0, 2, 3),  # Cara izquierda
    (0, 3, 4),  # Cara trasera
    (0, 4, 1),  # Cara derecha
    (1, 2, 3, 4) # Base
)

# Colores para cada cara de la pirámide
colores = [
    (1.0, 0.5, 0.5),  # Rojo pastel
    (0.5, 1.0, 0.5),  # Verde pastel
    (0.5, 0.5, 1.0),  # Azul pastel
    (1.0, 1.0, 0.5),  # Amarillo pastel
    (1.0, 0.5, 1.0)   # Magenta pastel
]


# Función para dibujar la pirámide con colores
def Piramide():
    glBegin(GL_TRIANGLES)  # Inicia el modo de dibujo de triángulos
    for i, cara in enumerate(caras[:-1]):  # Dibujamos las caras excepto la base
        glColor3fv(colores[i])  # Asigna un color a la cara
        for vertice in cara:
            glVertex3fv(vertices[vertice])  # Dibuja los vértices de la cara
    glEnd()

    glBegin(GL_QUADS)  # Inicia el modo de dibujo de cuadriláteros para la base
    glColor3fv(colores[4])  # Asigna color a la base
    for vertice in caras[-1]:
        glVertex3fv(vertices[vertice])  # Dibuja los vértices de la base
    glEnd()

# Función para dibujar los ejes de coordenadas
def EjesCoordenadas():
    glBegin(GL_LINES)

    # Eje X (blanco)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-6, -1.5, 0)
    glVertex3f(5, -1.5, 0)

    # Eje Y (blanco)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-2, -5, 0)
    glVertex3f(-2, 5, 0)

    glEnd()

# Función principal
def main():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Habilitar el depth testing para evitar transparencia en las caras
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia la pantalla y el buffer de profundidad

        # Dibuja los ejes de coordenadas
        glPushMatrix()
        EjesCoordenadas()
        glPopMatrix()
        
        # Dibuja la pirámide girando alrededor de su centro
        glPushMatrix()
        glRotatef(pygame.time.get_ticks() / 1000 * 50, 3, 1, 1)  # Rotación animada
        Piramide()  # Dibuja la pirámide
        glPopMatrix()

        pygame.display.flip()  # Actualiza la pantalla
        pygame.time.wait(13)

# Ejecutar el programa
main()
