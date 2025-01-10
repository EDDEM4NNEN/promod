import pygame
import sys
from player import *
from platformer import *
import numpy as np
#from kamera import *

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()


platforms = pygame.sprite.Group()
player = Player(50, 50)
ground = Platform(-1000, 550, 10000, 500) # (fra x, posy, til x, lengde y) kommer til å glemme
ground.image.fill("dark green") 
platnr1 = Platform(300,300,400,100)
platnr1.image.fill("green")  # Grønn yeah buddy
platforms.add(ground)
platforms.add(platnr1)


def death():
    print("you dead")

def collisions(x):  
  if x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
    player.rect.bottom = x.rect.top +1
    player.velocity_y = 0

  if x.rect.bottom -17 < player.rect.top < x.rect.bottom and pygame.sprite.spritecollide(player, platforms, False):
    player.rect.top =x.rect.bottom +1
    player.velocity_y = 0

  if player.rect.top <= x.rect.bottom - 17:
    if x.rect.right -17 < player.rect.left < x.rect.right and not x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
      player.rect.left = x.rect.right +0.1
      player.velocity_x = 0 

    if x.rect.left +17 > player.rect.right > x.rect.left and not x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
      player.rect.right = x.rect.left -0.1
      player.velocity_x = 0

    if x.rect.right -17 < player.rect.left < x.rect.right and x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
      player.rect.bottom = x.rect.top -1

    if x.rect.left +17 > player.rect.right > x.rect.left and x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
      player.rect.bottom = x.rect.top -1

def deathcollisions(x):  #kopierte fra den orginale bare at denne gjør andre ting hvis den berører platformen
  if x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
    death()
  if x.rect.bottom -17 < player.rect.top < x.rect.bottom and pygame.sprite.spritecollide(player, platforms, False):
    death()
  if x.rect.right -17 < player.rect.left < x.rect.right and x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
    death()
  if x.rect.left +17 > player.rect.right > x.rect.left and x.rect.top +17 > player.rect.bottom > x.rect.top and pygame.sprite.spritecollide(player, platforms, False):
    death()
  


while True:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            exit()

  
    collisions(ground)
    collisions(platnr1)

    player.input(platforms)
    player.update()
    player.draw(screen)
    platforms.draw(screen)

    
    if player.kill == True:
       event.type = pygame.QUIT


    #All the technicality yeah buddy
    clock.tick(60)
    pygame.display.flip()
    screen.fill("light blue") 

