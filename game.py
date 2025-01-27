import pygame
import random
import time

pygame.init()  #initialize game

clock = pygame.time.Clock()

#Colors
black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Orange = (255, 69, 0)

score_font = pygame.font.SysFont(None, 44)

#Player Variables
player_one_t = 250
player_two_u = 250
player_width = 15
player_height = 75
player_one_move = 0
player_two_move = 0
player_one_score = 0
player_two_score = 0
player_one_x = 75
player_two_x = 650

#Ball Variables
ball_move = 0
ball_x = 400
ball_y = 300
ball_height = 20
ball_width = 20
ball_Color = White

ball_move_right = False
ball_move_down = True

player_one_move_up = True
player_one_move_down = True

gameScreen = pygame.display.set_mode((800, 600))
keepOn = True
gamePaused = False


def render_score(score):
  score_text = score_font.render(str(score), True, White)
  gameScreen.blit(score_text, (300, 5))


def render_score_2(score_2):
  score_text = score_font.render(str(score_2), True, White)
  gameScreen.blit(score_text, (500, 5))


def render_paused(paused):
  paused_text = score_font.render(str(paused), True, White)
  gameScreen.blit(paused_text, (325, 285))


def random_color():
  return (random.randint(0, 255), random.randint(0,
                                                 255), random.randint(0, 255))


while keepOn == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      keepOn = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        player_one_move = -5
      if event.key == pygame.K_s:
        player_one_move = +5
      if event.key == pygame.K_i:
        player_two_move = -5
      if event.key == pygame.K_k:
        player_two_move = +5
      if event.key == pygame.K_p:
        gamePaused = not gamePaused
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_w:
        player_one_move = 0
      if event.key == pygame.K_s:
        player_one_move = 0
      if event.key == pygame.K_i:
        player_two_move = 0
      if event.key == pygame.K_k:
        player_two_move = 0
  #Simulation
  if not gamePaused:
    player_one_t = player_one_t + player_one_move
    player_two_u = player_two_u + player_two_move

    print(str(player_one_score) + "," + str(player_two_score))

    #Check if ball goes past left/right boundaries
    if ball_x <= -10:
      player_two_score = player_two_score + 1
      ball_x = 400
      ball_y = 300
    if ball_x >= 810:
      player_one_score = player_one_score + 1
      ball_x = 400
      ball_y = 300
    #Moving the ball based on its moving direction
    if ball_move_down == True:
      ball_y = ball_y + 5
    else:
      ball_y = ball_y - 5

    if ball_move_right == True:
      ball_x = ball_x + 5
    else:
      ball_x = ball_x - 5

    if ball_y <= 0:
      ball_move_down = True
      ball_Color = random_color()
    if ball_y >= 600 - ball_height:
      ball_move_down = False
      ball_Color = random_color()

      #Collision with player paddle
    if ball_x == 75 + player_width and ball_y >= player_one_t and ball_y <= player_one_t + player_height:
      ball_move_right = True
      ball_Color = random_color()
    if ball_x + ball_width == player_two_x and ball_y <= player_two_u + player_height and ball_y >= player_two_u:
      ball_move_right = False
      ball_Color = random_color()

      #Stops the player paddle from passing the top and bottom
    if player_one_t <= 0:
      player_one_t = 0
    if player_two_u <= 0:
      player_two_u = 0
    if player_one_t >= 600 - player_height:
      player_one_t = 600 - player_height
    if player_two_u >= 600 - player_height:
      player_two_u = 600 - player_height

  #Render

  #Fills the whole screen with orange

  gameScreen.fill(Orange)
  
  render_score(player_one_score)
  render_score_2(player_two_score)

  if gamePaused == True:
    render_paused("PAUSED")

  #Draws the player. (x,y, width, height)
  pygame.draw.rect(gameScreen, White,
                   (player_one_x, player_one_t, player_width, player_height))
  pygame.draw.rect(gameScreen, White,
                   (player_two_x, player_two_u, player_width, player_height))

  #Draws the square
  pygame.draw.rect(gameScreen, ball_Color, (ball_x, ball_y, 20, 20))

  clock.tick(30)

  pygame.display.update()
