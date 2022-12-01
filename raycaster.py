#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Lab 4


import numpy
import random
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import *
import glm

pygame.init()

screen = pygame.display.set_mode(
    (1080, 720),
    pygame.OPENGL | pygame.DOUBLEBUF
)

