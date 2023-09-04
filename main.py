import pygame
import random
import math
import time


#Init game:
pygame.init()

#screen:
screen = pygame.display.set_mode((800, 600))


#Caption and icon
pygame.display.set_caption("TANK FAKE")
icon = pygame.image.load('tank.png') 
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.jpg') #64x64
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Brick
brickImg = []
brickX = []
brickY = []
brickX_change = []
brickY_change = []
all_bricks = 10

for i in range(all_bricks):
    brickImg.append(pygame.image.load('brick.png')) #32x32
    brickX.append(random.randint(0, 736))
    brickY.append(random.randint(50, 150))
    brickX_change.append(0.1)
    brickY_change.append(15)


#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)


#game over text
over_font = pygame.font.Font('freesansbold.ttf', 56)

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))

def game_win():
    over_text = over_font.render("WINNER", True, (0, 0, 0))
    screen.blit(over_text, (250, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def brick(x, y, i):
    screen.blit(brickImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 20, y + 10))

def bullet_hit(brickX, brickY, bulletX, bulletY):
    distance = math.sqrt(math.pow(brickX - bulletX, 2) + (math.pow(brickY - bulletY, 2))) #cong thuc tinh khoang cach giua 2 diem 
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((225, 225, 225))
    #Win
    if score_value>=15:
        game_win()
        brickX=[]
        brickY=[]
        all_bricks=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #playermove and hit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #brickmove
    for i in range(all_bricks):

        #game over
        if brickY[i] > 200:
            for j in range(all_bricks):
                brickY[j] = 3000
            game_over_text()
            break
        
        #brickmove
        brickX[i] += brickX_change[i]
        if brickX[i] <= 0:
            brickX_change[i] = 0.1
            brickY[i] += brickY_change[i]
        elif brickX[i] >= 736:
            brickX_change[i] = -0.1
            brickY[i] += brickY_change[i]
        #Bullethit
        bullethit = bullet_hit(brickX[i], brickY[i], bulletX, bulletY)
        if bullethit:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            #create a new brick
            brickX[i] = random.randint(0, 735) 
            brickY[i] = random.randint(50, 180)
            
        brick(brickX[i], brickY[i], i)

#Bulletmove
    #miss
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(10,10)
    pygame.display.update()
