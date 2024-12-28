from OpenGL.GL import*
from OpenGL.GLUT import* 
from OpenGL.GLUT import*

w,h=500,500
def triangle():
    glBegin(GL_TRIANGLES)
    glVertex(100,250) #Vertice A
    glVertex(250,450)
    glVertex(400,250) 
    glEnd()
#Triangulo con color degradado
def triangle2():
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex(100,200) #Vertice A
    glColor3f(0,1,0)
    glVertex(250,400)
    glColor(1,1,0) 
    glVertex(400,200) 
    glEnd()
def square():
    glBegin(GL_QUADS)
    glVertex2f(100,10)
    glVertex2f(200,100) 
    glVertex2f(200,200) 
    glVertex2f(100,200)
    glEnd()
def iterate():
    glViewport(0,0,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,500, 0.0,500, 0.0,1.0) 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear (GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    #glColor3f(1,1,0) #Color solido
    #square()
    #glColor3f(0.0,1.0,0.0)
    #triangle()
    triangle2()
    glutSwapBuffers()
#---Modulo principal
glutInit()
glutInitDisplayMode (GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
glutCreateWindow("Grafica del cuadrado")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()