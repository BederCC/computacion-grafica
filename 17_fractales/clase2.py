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

# Define los vértices de los triángulos para formar una estrella
def estrella_sierpinski(depth):
    p1 = (0.5, 1)
    p2 = (0.65, 0.65)
    p3 = (1, 0.5)
    p4 = (0.65, 0.35)
    p5 = (0.5, 0)
    p6 = (0.35, 0.35)
    p7 = (0, 0.5)
    p8 = (0.35, 0.65)

    sierpinski(p1, p2, p8, depth)
    sierpinski(p2, p3, p4, depth)
    sierpinski(p8, p6, p7, depth)
    sierpinski(p4, p5, p6, depth)

# Nivel de profundidad del fractal
depth = 4  # Ajusta este valor para cambiar la cantidad de subdivisiones

# Crea la figura y llama a la función para dibujar el fractal en forma de estrella
plt.figure(figsize=(8, 8))
estrella_sierpinski(depth)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
