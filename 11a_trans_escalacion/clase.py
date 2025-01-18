
import pygame # Importa el módulo pygame para manejar gráficos y eventos de ventana
from pygame.locals import * # Importa constantes y funciones de pygame para facilitar el acceso
from OpenGL.GL import * # Importa funciones OpenGL para gráficos 3D
from OpenGL.GLUT import * # Importa funciones adicionales de OpenGL para gráficos
from OpenGL.GLU import * # Importa funciones de utilidad de OpenGL para configuraciones de perspectiv
vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)
# Vértice 2: abajo derecha
def draw_triangle():
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex3fv (vertex)
    glEnd()

def main():
    pygame.init() # Inicializa pygame para manejar la ventana y los eventos 
    display = (800, 600) # Tamaño de la ventana
    pygame.display.set_mode (display, DOUBLEBUF | OPENGL) # Crea una ventana OpenGL con doble buffer
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0) # Establece la perspectiva de visualizac 
    glTranslatef(0.0, 0.0, -5) # Traslada la escena en el eje z hacia adelante
    
    while True: # Bucle principal del programa
        for event in pygame.event.get():
    # Manejo de eventos de pygame
            if event.type == pygame.QUIT: # Si se cierra la ventana
                pygame.quit() # Finaliza pygame
                quit() # Sale del programa
        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpia el buffer de color y profundidad
        # Escalando el triángulo
        glScalef(0.5, 0.5, 0.5) # Escala el triángulo por un factor de 0.5 en todas las dimensiones
        draw_triangle() # Dibuja el triángulo escalado
        pygame.display.flip()
        pygame.time.wait(200)

if __name__ == "__main__":
    main() # Ejecuta la función principal del programa