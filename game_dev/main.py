import pygame

pygame.init()  # initialize PyGame

# create screen
screen = pygame.display.set_mode((600, 600))  # width, height - notice this is a tuple

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('spaceship.png')
playerX = 268
playerY = 472
playerDeltaX = 0


def createPlayer(x, y):
    # draw player image on screen
    screen.blit(playerImg, (x, y))


running = True  # variable to hold the status of the game; if it's running or not

# infinite loop to keep the game running
while running:
    # background colour RGB
    screen.fill((12, 18, 26))

    # check if any events in PyGame have been triggered
    for event in pygame.event.get():
        # check if the user exited the game
        if event.type == pygame.QUIT:
            running = False

        # check for keyboard input
        if event.type == pygame.KEYDOWN:  # press
            if event.key == pygame.K_LEFT:
                playerDeltaX = -0.2
            elif event.key == pygame.K_RIGHT:
                playerDeltaX = 0.2

        if event.type == pygame.KEYUP:  # lift
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerDeltaX = 0

    playerX += playerDeltaX  # update position of player

    # set boundaries
    if playerX >= 536:
        playerX = 536
    elif playerX <= 0:
        playerX = 0

    # call createPlayer method to draw onto screen
    createPlayer(playerX, playerY)

    pygame.display.update()
