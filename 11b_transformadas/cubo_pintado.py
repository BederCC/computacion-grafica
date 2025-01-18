import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

# Definición de los vértices del cubo
vertices = (
    (1, -1, -1),  # 0
    (1, 1, -1),   # 1
    (-1, 1, -1),  # 2
    (-1, -1, -1), # 3
    (1, -1, 1),   # 4
    (1, 1, 1),    # 5
    (-1, -1, 1),  # 6
    (-1, 1, 1)    # 7
)

# Definición de las caras del cubo
caras = (
    (0, 1, 2, 3),  # Cara frontal
    (4, 5, 7, 6),  # Cara trasera
    (0, 4, 5, 1),  # Cara derecha
    (3, 2, 7, 6),  # Cara izquierda
    (1, 5, 7, 2),  # Cara superior
    (0, 3, 6, 4)   # Cara inferior
)

# Colores para cada cara del cubo
colores = [
    (1.0, 0.5, 0.5),  # Rojo pastel
    (0.5, 1.0, 0.5),  # Verde pastel
    (0.5, 0.5, 1.0),  # Azul pastel
    (1.0, 1.0, 0.5),  # Amarillo pastel
    (1.0, 0.5, 1.0),  # Magenta pastel
    (0.5, 1.0, 1.0)   # Cian pastel
]


# Función para dibujar el cubo con colores
def Cubo():
    glBegin(GL_QUADS)  # Inicia el modo de dibujo de cuadriláteros
    for i, cara in enumerate(caras):
        glColor3fv(colores[i])  # Asigna un color a la cara
        for vertice in cara:
            glVertex3fv(vertices[vertice])  # Dibuja los vértices de la cara
    glEnd()

# Función para dibujar los ejes de coordenadas
def EjesCoordenadas():
    glBegin(GL_LINES)

    # Eje X (rojo)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-6, -1.5, 0)
    glVertex3f(5, -1.5, 0)

    # Eje Y (verde)
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
        
        # Dibuja el cubo girando alrededor de su centro
        glPushMatrix()
        glRotatef(pygame.time.get_ticks() / 1000 * 50, 3, 1, 1)  # Rotación animada
        Cubo()  # Dibuja el cubo
        glPopMatrix()

        pygame.display.flip()  # Actualiza la pantalla
        pygame.time.wait(13)

# Ejecutar el programa
main()
