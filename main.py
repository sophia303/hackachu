import pygame
import sys
#importing libraries (I totally know what I'm doing lmao this is a lie)

pygame.init()
#initializing

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#making screen

screen.fill((100,100,100))
#rgb!!

running = True
while running: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
#refreshing screen, to end game if you exit window

pygame.quit()
sys.exit()
