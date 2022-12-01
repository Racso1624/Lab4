#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Lab 4

from matrix import *
import random
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import *
import glm
from obj import *
from numpy import *

pygame.init()

screen = pygame.display.set_mode(
    (1080, 720),
    pygame.OPENGL | pygame.DOUBLEBUF
)

model = Obj('./human.obj')
vertex = array(model.vertices)

degrees = 0
while (running):

  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  first_color = random.random()
  second_color = random.random()
  third_color = random.random()

  full_color = glm.vec3(first_color, second_color, third_color)
  first_color_location = glGetUniformLocation(shader, "color")
  glUniform3fv(first_color_location, 1, glm.value_ptr(full_color))

  calculateMatrix(degrees)

  pygame.time.wait(100)

  glDrawArrays(GL_TRIANGLES, 0, len(vertex))

  pygame.display.flip()

  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      running = False
    if (event.type == pygame.KEYDOWN):
      if (event.key == pygame.K_a):
        degrees -= 10
      if (event.key == pygame.K_d):
        degrees += 10