import pygame 
from pygame import *
import random
import math


#initilizing the pygame 
pygame.init()

#screen
screen = pygame.display.set_mode((800, 600))


# Background 
background = pygame.image.load("grass.jpg")
road = pygame.image.load("cel.png")

#caption
pygame.display.set_caption("Escape from Zombie")

#time
time = pygame.time.Clock()

#player
playerImg = pygame.image.load("person.png")
player_radius = playerImg.get_rect().center[0]
playerX = 370
playerY = 480
playerX_change = 0
player_width = playerImg.get_width()
player_height = playerImg.get_height()

# Zombies 
zombieImg = pygame.image.load("zombie.png")
zombie_radius = zombieImg.get_rect().center[0]
zombieX = []
zombieY = []
zombieX_change = []
zombieY_change = []
zombie_width = None
zombie_height = None
num_of_zombies = 7

for i in range(num_of_zombies):

    # Zombie 
    
    zombieX.append(random.randint(200, 550))
    zombieY.append(random.randint(-50, 200))
    zombieX_change.append(60)
    zombieY_change.append(2)

# Game Over 
over_font = pygame.font.Font("cherry.ttf", 64)



#game functions 
def player(x, y):
    screen.blit(playerImg, (x, y))
    

def zombie(x, y, i):
    screen.blit(zombieImg, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

    


#game loop
running = True

while running:

    #rgb
    screen.fill((255, 255, 255))

    # Background Image 
    screen.blit(background, (0, 0))
    screen.blit(road, (200, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #moving of player 
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                playerX_change = -5
            if event.key == K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:        
            if event.key == K_LEFT or event.key == K_RIGHT :
                playerX_change = 0
        


    # Checking for boundaries of spaceship so it does not go out of bounds
    playerX += playerX_change
    
    if playerX <= 200:
        playerX = 200
    elif playerX >= 550:
        playerX = 550

    # Zombie movement
    for i in range(num_of_zombies):

        #game over
        #distance = math.hypot(player_width - zombie_width, player_height - zombie_height)
        #if distance >= player_radius + player_radius:
             #game_over_text()
             #break
    


        zombieY[i] +=zombieY_change[i]

        if zombieY[i] <= 0:
            zombieY[i] = 0
            zombieY_change[i] = 2
        elif zombieY[i] > 600:
            zombieX[i] = random.randint(200, 550)
            zombieY[i] = random.randint(-50, 200)
            
            
            
        zombie(zombieX[i], zombieY[i], i)
    
    player(playerX, playerY)
    
    
    pygame.display.update()
