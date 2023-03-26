import pygame
import random
import sys
from pygame.locals import *

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

def ball_init(right):
  global ball_pos, ball_vel
  ball_pos = [width // 2, height // 2]
  horz = random.randrange(2, 4)
  vert = random.randrange(1, 3)
  if right == False:
    horz = -horz
  ball_vel = [horz, -vert]

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

def draw(canvas):
  global paddle_1_pos, paddle_2_pos, ball_pos, ball_vel, left_score, right_score
  canvas.fill(black)
  pygame.draw.line(canvas, white, [width//2, 0], [width//2, height], 1)
  pygame.draw.line(canvas, white, [pad_width, 0], [pad_width, height], 1)
  pygame.draw.line(canvas, white, [width - pad_width, 0], [width - pad_width, height], 1)
  pygame.draw.circle(canvas, white, [width//2, height//2], 70, 1)

def keydown(event):
  global paddle_1_vel, paddle_2_vel
  if event.key == K_UP:
    paddle_2_vel = -8
  elif event.key == K_DOWN:
    paddle_2_vel = 8
  elif event.key == K_w:
    paddle_1_vel = -8
  elif event.key == K_s:
    paddle_1_vel = 8

def keyup(event):
  global paddle_1_vel, paddle_2_vel
  if event.key in (K_w, K_s):
    paddle_1_vel = 0
  elif event.key in (K_UP, K_DOWN):
    paddle_2_vel = 0

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