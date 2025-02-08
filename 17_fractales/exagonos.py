import matplotlib.pyplot as plt
import numpy as np

# Función para calcular el vértice de un pentágono con rotación de 180 grados
def pentagon(center, size):
    points = []
    for i in range(5):
        angle = 2 * np.pi * i / 5 + np.pi / 2  # 72 grados entre cada vértice, rotado 180 grados
        x = center[0] + size * np.cos(angle)
        y = center[1] + size * np.sin(angle)
        points.append((x, y))
    return points

# Función para dibujar el patrón de pentágonos de forma organizada
def draw_flower(center, size, depth, scale_factor=1.6):
    if depth == 0:
        # Dibuja un pentágono en la posición especificada
        pentagon_points = pentagon(center, size * scale_factor)  # Aplicar factor de escala
        pentagon_x, pentagon_y = zip(*pentagon_points)
        plt.fill(pentagon_x, pentagon_y, 'yellowgreen', edgecolor='red')  # Color verde con borde rojo
    else:
        # Dibuja 5 pentágonos alrededor de la posición central
        pentagon_points = pentagon(center, size)
        for i in range(5):
            new_center = pentagon_points[i]  # Nuevo centro es una esquina del pentágono central
            draw_flower(new_center, size / 2.6, depth - 1, scale_factor)  # Llamada recursiva con tamaño reducido

# Configuración de la figura
plt.figure(figsize=(8, 8))

# Parámetros iniciales: posición, tamaño y profundidad de la recursión
center = (0, 0)  # Centro de la figura
size = 1         # Tamaño del pentágono
depth = 2        # Nivel de recursión ajustado para que se vea más denso

# Llamada a la función recursiva
draw_flower(center, size, depth)

# Ajustes de la gráfica
plt.gca().set_aspect('equal')
plt.axis('off')  # Desactivar el eje
plt.show()
