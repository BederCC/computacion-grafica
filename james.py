import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

texture_tip = pygame.image.load("ladrillo.jpg")  # textura para el medio de la figura
texture_rest = pygame.image.load("ladrillo.jpg")  # textura para el resto de la figura
texture_pointer = pygame.image.load("ladrillo.jpg")  # textura para la punta de la figura que sigue al puntero

texture_tip = pygame.transform.scale(texture_tip, (70, 70))
texture_rest = pygame.transform.scale(texture_rest, (20, 20))
texture_pointer = pygame.transform.scale(texture_pointer, (50, 50))  # Corregido el nombre de la variable

elems = [{'x': WIDTH // 2, 'y': HEIGHT // 2} for _ in range(10)]  # Corregido el nombre de la variable
pointer = {'x': WIDTH // 2, 'y': HEIGHT // 2}

frm = 0  # Este es el contador de frames
rad = 100  # Radio para las coordenadas
N = 10  # Número de elementos
width, height = WIDTH, HEIGHT

def run():
    global frm, pointer, elems
    screen.fill((255, 255, 255))  # Limpiar la pantalla con color blanco

    # Detectar eventos (como el movimiento del ratón)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            pointer['x'], pointer['y'] = event.pos  # Actualizamos la posición del puntero

    for i in range(N):
        e = elems[i]
        if i == 0:
            # Primer elemento (punta) sigue al puntero
            ax = (math.cos(3 * frm) * rad * width) / height
            ay = (math.sin(4 * frm) * rad * height) / width
            e['x'] += (ax + pointer['x'] - e['x']) / 10
            e['y'] += (ay + pointer['y'] - e['y']) / 10
            s = (162 + 4 * (1 - i)) / 40  # Definir s en el primer caso
            texture = texture_pointer  # Usar textura para la punta
        elif i == 5:
            ep = elems[i - 1]
            m = math.atan2(e['y'] - ep['y'], e['x'] - ep['x'])
            e['x'] += (ep['x'] - e['x'] + (math.cos(m) * (100 - i)) / 5) / 4
            e['y'] += (ep['y'] - e['y'] + (math.sin(m) * (100 - i)) / 5) / 4
            texture = texture_tip  # Asignar textura diferente para el elemento en la posición 5
            s = (200 + 4 * (1 - i)) / 20  # Definir s para este caso
        else:
            ep = elems[i - 1]
            a = math.atan2(e['y'] - ep['y'], e['x'] - ep['x'])
            e['x'] += (ep['x'] - e['x'] + (math.cos(a) * (100 - i)) / 5) / 4
            e['y'] += (ep['y'] - e['y'] + (math.sin(a) * (100 - i)) / 5) / 4
            s = (162 + 4 * (1 - i)) / 50  # Definir s en el resto de los casos
            texture = texture_rest  # Usar textura para el resto

        # Dibujar la textura en lugar de un círculo
        texture_scaled = pygame.transform.scale(texture, (int(s * 10), int(s * 10)))  # Escalar textura
        texture_rect = texture_scaled.get_rect(center=(int(e['x']), int(e['y'])))  # Establecer el centro de la textura
        screen.blit(texture_scaled, texture_rect)  # Dibujar la textura

    texture_scaled = pygame.transform.scale(texture_pointer, (int(s * 60), int(s * 60)))
    pointer_rect = texture_pointer.get_rect(center=(int(pointer['x']), int(pointer['y'])))  # Establecer el centro del puntero
    screen.blit(texture_pointer, pointer_rect)  # Dibujar el puntero

    # Aumentar el contador de frames
    frm += 1

    # Actualizar la pantalla
    pygame.display.flip()

while True:
    run()
    clock.tick(60)  # Limitar a 60 FPS
