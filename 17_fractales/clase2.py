import matplotlib.pyplot as plt

# Función para calcular el punto medio entre dos puntos
def punto_medio(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Función recursiva para dibujar el triángulo de Sierpinski
def sierpinski(p1, p2, p3, depth):
    if depth == 0:
        # Dibuja el triángulo
        plt.fill([p1[0], p2[0], p3[0], p1[0]], [p1[1], p2[1], p3[1], p1[1]], 'b')
    else:
        # Calcula los puntos medios de los lados
        pm1 = punto_medio(p1, p2)
        pm2 = punto_medio(p2, p3)
        pm3 = punto_medio(p1, p3)

        # Llama a la función recursivamente en los nuevos triángulos
        sierpinski(p1, pm1, pm3, depth - 1)
        sierpinski(pm1, p2, pm2, depth - 1)
        sierpinski(pm3, pm2, p3, depth - 1)

# Define los vértices de los triángulos para formar una estrella con cinco esquinas
def estrella_sierpinski(depth):
    p1 = (0.5, 1)
    p2 = (0.61, 0.81)
    p3 = (0.95, 0.81)
    p4 = (0.68, 0.61)
    p5 = (0.79, 0.24)
    p6 = (0.5, 0.5)
    p7 = (0.21, 0.24)
    p8 = (0.32, 0.61)
    p9 = (0.05, 0.81)
    p10 = (0.39, 0.81)

    sierpinski(p1, p2, p10, depth)
    sierpinski(p2, p3, p4, depth)
    sierpinski(p10, p8, p9, depth)
    sierpinski(p4, p5, p6, depth)
    sierpinski(p6, p7, p8, depth)

# Nivel de profundidad del fractal
depth = 4  # Ajusta este valor para cambiar la cantidad de subdivisiones

# Crea la figura y llama a la función para dibujar el fractal en forma de estrella
plt.figure(figsize=(8, 8))
estrella_sierpinski(depth)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
