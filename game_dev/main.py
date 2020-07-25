import pygame
import random

pygame.init()  # initialize PyGame

# create screen
screen = pygame.display.set_mode((600, 600))  # width, height - notice this is a tuple

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('background.jpg')

# player
playerImg = pygame.image.load('spaceship.png')
playerX = 268
playerY = 472
playerDeltaX = 0

# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 535)
enemyY = random.randint(64, 100)
enemyDeltaX = 2
enemyDeltaY = 40

# bullet
bulletImg = pygame.image.load('laser.png')
bulletY = playerY
bulletState = 'ready'  # ready - can't see; fire - laser is moving


def createPlayer(x, y):
    # draw player image on screen
    screen.blit(playerImg, (x, y))


def createEnemy(x, y):
    screen.blit(enemyImg, (x, y))


def shoot(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImg, (x, y))


running = True  # variable to hold the status of the game; if it's running or not

# infinite loop to keep the game running
while running:
    # background colour RGB
    screen.fill((12, 18, 26))
    screen.blit(background, (0, 0))

    # check if any events in PyGame have been triggered
    for event in pygame.event.get():
        # check if the user exited the game
        if event.type == pygame.QUIT:
            running = False

        # check for keyboard input
        if event.type == pygame.KEYDOWN:  # press
            if event.key == pygame.K_LEFT:
                playerDeltaX = -2
            elif event.key == pygame.K_RIGHT:
                playerDeltaX = 2

        if event.type == pygame.KEYUP:  # lift
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerDeltaX = 0

            if event.key == pygame.K_SPACE and bulletState == 'ready':
                # get x position then fire bullet
                bulletX = playerX + 16
                shoot(bulletX, bulletY)

    playerX += playerDeltaX  # update position of player

    enemyX += enemyDeltaX  # move enemy horizontally

    # bullet movement
    if bulletY <= -32:
        bulletY = playerY
        bulletState = 'ready'

    if bulletState == 'fire':
        shoot(bulletX, bulletY)
        bulletY -= 4

    # set boundaries
    if playerX >= 536:
        playerX = 536
    elif playerX <= 0:
        playerX = 0

    # enemy boundaries
    if enemyX >= 536:
        enemyDeltaX = -2  # change direction of enemy
        enemyY += enemyDeltaY  # shift enemy downwards
    elif enemyX <= 0:
        enemyDeltaX = 2  # change direction of enemy
        enemyY += enemyDeltaY  # shift enemy downwards

    # call createPlayer method to draw onto screen
    createPlayer(playerX, playerY)
    createEnemy(enemyX, enemyY)

    pygame.display.update()
