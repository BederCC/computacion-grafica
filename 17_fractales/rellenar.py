import matplotlib.pyplot as plt

# Función para calcular el punto medio entre dos puntos
def punto_medio(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Función recursiva para dibujar el triángulo de Sierpinski
def sierpinski(p1, p2, p3, depth, linewidth=1):
    if depth == 0:
        # Dibuja el triángulo con un borde de grosor especificado
        plt.fill([p1[0], p2[0], p3[0], p1[0]], [p1[1], p2[1], p3[1], p1[1]], 'b', edgecolor='white', linewidth=linewidth)
    else:
        # Calcula los puntos medios de los lados
        pm1 = punto_medio(p1, p2)
        pm2 = punto_medio(p2, p3)
        pm3 = punto_medio(p1, p3)

        # Llama a la función recursivamente en los nuevos triángulos
        sierpinski(p1, pm1, pm3, depth - 1, linewidth)
        sierpinski(pm1, p2, pm2, depth - 1, linewidth)
        sierpinski(pm3, pm2, p3, depth - 1, linewidth)
        sierpinski(pm1, pm2, pm3, depth - 1, linewidth)  # Añade esto para rellenar el triángulo central vacío

# Define los vértices del triángulo grande
p1 = (0, 0)
p2 = (1, 0)
p3 = (0.5, 0.866)  # Altura del triángulo equilátero

# Nivel de profundidad del fractal
depth = 5  # Ajusta este valor para cambiar la cantidad de subdivisiones

# Crea la figura y llama a la función para dibujar el fractal
plt.figure(figsize=(8, 8))
sierpinski(p1, p2, p3, depth, linewidth=2)  # Ajusta el grosor de la línea aquí
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
