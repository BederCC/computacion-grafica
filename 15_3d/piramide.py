import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from PIL import Image

vertex_src = """
#version 330 core
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;

uniform mat4 rotation;

out vec2 v_texture;

void main()
{
    gl_Position = rotation * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
#version 330 core
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture);
}
"""

# Callback para el cambio de tamaño de la ventana
def window_resize(window, width, height):
    glViewport(0, 0, width, height)

# Inicialización de GLFW
if not glfw.init():
    raise Exception("¡GLFW no pudo inicializarse!")

# Creación de la ventana
window = glfw.create_window(1280, 720, "Mi ventana OpenGL", None, None)
if not window:
    glfw.terminate()
    raise Exception("¡La ventana de GLFW no pudo crearse!")

# Configuración de posición de la ventana
glfw.set_window_pos(window, 400, 200)
# Configuración del callback de cambio de tamaño de la ventana
glfw.set_window_size_callback(window, window_resize)
# Establecer el contexto actual
glfw.make_context_current(window)

# Coordenadas de los vértices, colores y coordenadas de textura de la pirámide
vertices = [
    # Base
    -0.5, 0.0, -0.5,  0.0, 0.0,  # 0
     0.5, 0.0, -0.5,  1.0, 0.0,  # 1
     0.5, 0.0,  0.5,  1.0, 1.0,  # 2
    -0.5, 0.0,  0.5,  0.0, 1.0,  # 3
    # Punta
     0.0, 0.8,  0.0,  0.5, 0.5   # 4
]

indices = [
    # Base
    0, 1, 2, 2, 3, 0,
    # Lados
    0, 1, 4,
    1, 2, 4,
    2, 3, 4,
    3, 0, 4
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
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(0))
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(12))

texture = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture)

# Configuración de parámetros de la textura
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

# Carga de la imagen de ladrillo
image = Image.open("ladrillo.jpg")
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
