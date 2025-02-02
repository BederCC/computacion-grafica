import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from PIL import Image

vertex_src = """
#version 330 core
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;
layout(location = 2) in vec2 a_texture;

uniform mat4 rotation;

out vec3 v_color;
out vec2 v_texture;

void main()
{
    gl_Position = rotation * vec4(a_position, 1.0);
    v_color = a_color;
    v_texture = a_texture;
}
"""

fragment_src = """
#version 330 core
in vec3 v_color;
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture) * vec4(v_color, 1.0f);
}
"""

# Callback para el cambio de tamaño de la ventana
def window_resize(window, width, height):
    glViewport(0, 0, width, height)

# Inicialización de GLFW
if not glfw.init():
    raise Exception("¡GLFW no pudo inicializarse!")

# Creación de la ventana
window = glfw.create_window(1800, 1200, "Mi ventana OpenGL", None, None)
if not window:
    glfw.terminate()
    raise Exception("¡La ventana de GLFW no pudo crearse!")

# Configuración de posición de la ventana
glfw.set_window_pos(window, 400, 200)
# Configuración del callback de cambio de tamaño de la ventana
glfw.set_window_size_callback(window, window_resize)
# Establecer el contexto actual
glfw.make_context_current(window)

vertices = [
    # Coordenadas      # Colores     # Coordenadas de textura
    -0.5, -0.5,  0.5,  1.0, 0.0, 0.0,  0.0, 0.0,  # Frente
     0.5, -0.5,  0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
     0.5,  0.5,  0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
    -0.5,  0.5,  0.5,  1.0, 1.0, 0.0,  0.0, 1.0,
    
    -0.5, -0.5, -0.5,  1.0, 0.0, 0.0,  0.0, 0.0,  # Atrás
     0.5, -0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
     0.5,  0.5, -0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
    -0.5,  0.5, -0.5,  1.0, 1.0, 0.0,  0.0, 1.0,
    
    -0.5,  0.5, -0.5,  0.0, 1.0, 1.0,  0.0, 0.0,  # Izquierda
    -0.5,  0.5,  0.5,  1.0, 0.0, 1.0,  1.0, 0.0,
    -0.5, -0.5,  0.5,  1.0, 1.0, 0.0,  1.0, 1.0,
    -0.5, -0.5, -0.5,  0.0, 0.0, 1.0,  0.0, 1.0,
    
     0.5,  0.5, -0.5,  1.0, 0.5, 0.0,  0.0, 0.0,  # Derecha
     0.5,  0.5,  0.5,  0.5, 0.5, 1.0,  1.0, 0.0,
     0.5, -0.5,  0.5,  0.5, 1.0, 1.0,  1.0, 1.0,
     0.5, -0.5, -0.5,  0.0, 1.0, 0.5,  0.0, 1.0,
    
    -0.5, -0.5, -0.5,  1.0, 0.0, 0.5,  0.0, 0.0,  # Abajo
     0.5, -0.5, -0.5,  0.5, 1.0, 0.5,  1.0, 0.0,
     0.5, -0.5,  0.5,  0.5, 0.5, 0.5,  1.0, 1.0,
    -0.5, -0.5,  0.5,  0.0, 0.5, 1.0,  0.0, 1.0,
    
    -0.5,  0.5, -0.5,  0.0, 0.5, 0.0,  0.0, 0.0,  # Arriba
     0.5,  0.5, -0.5,  1.0, 0.5, 1.0,  1.0, 0.0,
     0.5,  0.5,  0.5,  1.0, 1.0, 0.5,  1.0, 1.0,
    -0.5,  0.5,  0.5,  0.5, 0.0, 1.0,  0.0, 1.0,
]

indices = [
    0,  1,  2,  2,  3,  0,  # Frente
    4,  5,  6,  6,  7,  4,  # Atrás
    8,  9, 10, 10, 11,  8,  # Izquierda
    12, 13, 14, 14, 15, 12, # Derecha
    16, 17, 18, 18, 19, 16, # Abajo
    20, 21, 22, 22, 23, 20  # Arriba
]

vertices = np.array(vertices, dtype=np.float32)
indices = np.array(indices, dtype=np.uint32)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(0))
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(12))
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, vertices.itemsize * 8, ctypes.c_void_p(24))

texture = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture)

# Configuración de parámetros de la textura
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

# Carga de la imagen (continuación)
image = Image.open("satelite.jpg")
image = image.transpose(Image.FLIP_TOP_BOTTOM)
img_data = image.convert("RGBA").tobytes()
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

glUseProgram(shader)
glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)

rotation_loc = glGetUniformLocation(shader, "rotation")

# Bucle principal de la aplicación
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
    glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, pyrr.matrix44.multiply(rot_x, rot_y))

    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    glfw.swap_buffers(window)

# Terminación de GLFW y liberación de recursos
glfw.terminate()
