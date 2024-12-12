import pygame as pg
from pygame.locals import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
    glClearColor(0.120, 0.40, 0.60, 1.0) 
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) #establish the coordinates of the screen
    
def plot_points(): #function to plot the points
    glClear(GL_COLOR_BUFFER_BIT) #clear the buffer
    glColor3f(1.0, 0.4, 0.0) #establish the color of the points (green)
    glPointSize(25.0) #establish the size of the points
    glBegin(GL_POINTS) #start plotting points
    glVertex2f(-0.2, 0.3) #plot the point at the origin
    glEnd() #end plotting points
    glFlush() #execute the commands
    
glutInit() #initialize the GLUT library
glutInitDisplayMode(GLUT_RGB) #initialize the display mode
glutCreateWindow(b"OpenGL Window") #create the window
glutInitWindowSize(500, 500) #initialize the window size
glutInitWindowPosition(50, 50) #initialize the window position
glutDisplayFunc(plot_points) #call the plot_points function
clearScreen() #call the clearScreen function
glutMainLoop() #enter the GLUT event processing loop