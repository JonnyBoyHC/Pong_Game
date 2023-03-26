import pygame
import random
import sys

pygame.init()
FPS = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

width = 600
height = 400
ball_radius = 20
pad_width = 8
pad_height = 80
half_pad_width = pad_width // 2
half_pad_height = pad_height // 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle_1_vel = 0
paddle_2_vel = 0
left_score = 0
right_score = 0

window = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('PONG GAME')

init()

while True:
  draw(window)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == KEYDOWN:
      keydown(event)
    elif event.type == KEYUP:
      keyup(event)

  pygame.display.update()
  FPS.tick(60)