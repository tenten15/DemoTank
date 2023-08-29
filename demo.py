import pygame
       


pygame.init()

scrn = pygame.display.set_mode((800,600))
pygame.display.set_caption("TankGame")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

dongho = pygame.time.Clock()

x=100
y=120
r=60
c=40
a = 5

run =True

while run:
    dongho.tick(60)

    scrn.fill('deepskyblue')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    phim = pygame.key.get_pressed()
    if phim[pygame.K_LEFT] and x >= a:
        x -= a
    if phim[pygame.K_RIGHT] and x <= 600 - r:
        x += a
    if phim[pygame.K_UP] and y >= a:
        y -= a
    if phim[pygame.K_DOWN] and y <= 800-c:
        y += a


    pygame.draw.rect(scrn,(0,0,0),(x,y,r,c))
    pygame.display.update()

pygame.quit()

