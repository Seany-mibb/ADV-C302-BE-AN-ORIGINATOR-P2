import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((10, 25, 60))

    #Head
    skinColor = (255,219,172)
    headRect = pygame.Rect(320, 50, 120, 120)
    pygame.draw.rect(screen, skinColor, headRect)
    
    #eyes
    black = (0, 0, 0)
    pygame.draw.circle(screen, black, (350, 80), 15)
    pygame.draw.circle(screen, black, (410, 80), 15)

    #mouth
    white = (255, 255, 255)
    tooth1 = pygame.Rect(345, 110, 30, 40)
    pygame.draw.rect(screen, white, tooth1)
    
    tooth2 = pygame.Rect(380, 110, 30, 40)
    pygame.draw.rect(screen, white, tooth2)

    #Hat
    mainHat = pygame.Rect(315, 0, 130, 50)
    pygame.draw.rect(screen, white, mainHat)

    branchHat = pygame.Rect(445, 30, 70, 20)
    pygame.draw.rect(screen, white, branchHat)

    #Shirt
    mainShirt = pygame.Rect(280, 170, 200, 300)
    pygame.draw.rect(screen, black, mainShirt)

    leftShirt = pygame.Rect(210, 170, 70, 80)
    pygame.draw.rect(screen, black, leftShirt)

    rightShirt = pygame.Rect(480, 170, 70, 80)
    pygame.draw.rect(screen, black, rightShirt)

    #Pants
    brown = (131, 105, 83)
    top = pygame.Rect(280, 470, 200, 50)
    pygame.draw.rect(screen, brown, top)
    leftPants = pygame.Rect(280, 520, 90, 200)
    pygame.draw.rect(screen, brown, leftPants)
    rightPants = pygame.Rect(390, 520, 90, 200)
    pygame.draw.rect(screen, brown, rightPants)

    #Shoes
    darkBrown = (92, 64, 51)
    leftShoe = pygame.Rect(280, 720, 100, 50)
    pygame.draw.rect(screen, darkBrown, leftShoe)

    rightShoe = pygame.Rect(390, 720, 100, 50)
    pygame.draw.rect(screen, darkBrown, rightShoe)

    #Arms
    leftArm = pygame.Rect(225, 250, 40, 150)
    pygame.draw.rect(screen, skinColor, leftArm)

    rightArm = pygame.Rect(495, 250, 40, 150)
    pygame.draw.rect(screen, skinColor, rightArm)

    #Hands
    pygame.draw.circle(screen, skinColor, (245, 420), 30)
    pygame.draw.circle(screen, skinColor, (515, 420), 30)

    pygame.display.flip()

pygame.quit()