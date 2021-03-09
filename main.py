import pygame
import random
import time
import sys
pygame.init()

# Variables
word = ""
chances = 6

# Word arrays
fiveLetters = ["BLOWN", "CADET", "CANES", "BREAD", "ANGRY", "ADDED", "BURNT", "BRUTE", "AMONG", "AGING"]

# Selects a random word from the array to use
word = fiveLetters[random.randint(0, len(fiveLetters) - 1)]
printArray = [""] * len(word)
# print(word)  # Prints the word to test if the program works. Uncomment if you want to test the program

# Setting up screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("HungBloke")
hangManIcon = pygame.image.load("imgs/hangManIcon.png")
background = pygame.image.load("imgs/hungBlokeBack800.png")
pygame.display.set_icon(hangManIcon)

# Hang man images
hangEmpty = hangManIcon = pygame.image.load("imgs/hangNone352.png")
hangFull = pygame.image.load("imgs/hangFull352.png")
hangH = pygame.image.load("imgs/hangHead352.png")
hangH_B = pygame.image.load("imgs/hangHeadBody352.png")
hangH_B_Ra = pygame.image.load("imgs/hangHeadBodyRArm352.png")
hangH_B_Ra_La = pygame.image.load("imgs/hangHeadBodyRArmLArm352.png")
hangH_B_Ra_La_Rl = pygame.image.load("imgs/hangHeadBodyRArmLArmRLeg352.png")

# Function to draw the hang man image on the screen
def hangMan(image):
    screen.blit(image, (0, 25))

# Text
gameFont = pygame.font.Font("freesansbold.ttf", 32)
textRendered = gameFont.render("", True, (255, 255, 255))

# Underlines
def underlines():
    pygame.draw.rect(screen, (0, 0, 0), (400, 100, 50, 10))
    pygame.draw.rect(screen, (0, 0, 0), (470, 100, 50, 10))
    pygame.draw.rect(screen, (0, 0, 0), (540, 100, 50, 10))
    pygame.draw.rect(screen, (0, 0, 0), (610, 100, 50, 10))
    pygame.draw.rect(screen, (0, 0, 0), (680, 100, 50, 10))

# Loop for the game
running = True
while running:
    # Checks if the player has run out of chances
    if chances == 0:
        running = False

    # Paints over the previous frame
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Updates the the screen
    underlines()
    hangMan(hangEmpty)

    # Print any letters entered that are correct
    xPlace = 400
    for x in range(0, len(printArray)):
        textRendered = gameFont.render(printArray[x], True, (255, 255, 255))
        screen.blit(textRendered, (xPlace, 75))
        xPlace += 70
    textRendered = gameFont.render("", True, (255, 255, 255))
    xPlace = 400

    # Sets variables for the loop
    char = ""

    # Updates the screen
    pygame.display.update()

    # Checks if the player has run out of chances
    if chances == 0:
        # Display "YOU LOSE"
        screen.fill((0, 0, 0))
        textRendered = gameFont.render("YOU LOSE", True, (255, 255, 255))
        screen.blit(textRendered, (0, 200))
        pygame.display.update()
        time.sleep(2)
        sys.exit(0)

    # Checks if the player has filled in all the letter and tells them they have won if they have
    winCheck = ""
    for i in range(0, len(printArray)):
        winCheck += printArray[i]
        if winCheck == word:
            screen.fill((0, 0, 0))
            textRendered = gameFont.render("YOU WIN", True, (255, 255, 255))
            screen.blit(textRendered, (0, 200))
            pygame.display.update()
            time.sleep(2)
            sys.exit(0)

    # Detect events
    accept = True
    while accept:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                accept = False
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_RETURN:
                    char = ""
                    char += str(chr(event.key))
                if event.key == pygame.K_RETURN:
                    chances -= 1
                    accept = False

    # Check if the character entered matches a letter in the word
    for i in range(0, len(word)):
        if char.upper() == word[i]:
            printArray[i] = char.upper()
        # else:
