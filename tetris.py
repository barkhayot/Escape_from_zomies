import pygame 
from pygame import *

#initilizing the pygame 
pygame.init()

#screen
screen = pygame.display.set_mode((600, 800))

#caption
pygame.display.set_caption("Guy Runner")

#time
time = pygame.time.Clock()

#player
playerImg = pygame.image.load("person.png")
playerX = 370
playerY = 480
playerX_change = 0



#game functions 
def player(x, y):
    screen.blit(playerImg, (x, y))

#game loop
running = True

while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player(playerX, playerY)
    
    
    pygame.display.update()

