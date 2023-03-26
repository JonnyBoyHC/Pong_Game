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

def init():
  global paddle_1_pos, paddle_2_pos, paddle_1_vel, paddle_2_vel, left_score, right_score
  global score_1, score_2
  paddle_1_pos = [half_pad_width - 1, height // 2]
  paddle_2_pos = [width + 1 - half_pad_width, height // 2]
  left_score = 0
  right_score = 0

  if random.randrange(0, 2) == 0:
    ball_init(True)
  else:
    ball_init(False)


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