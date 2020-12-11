import sys, pygame
pygame.init()

tela = 300, 600
speed = [0, 0]
screen = pygame.display.set_mode(tela)
black = 0, 0, 0

ball = pygame.image.load('BirdGif.gif')

ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > 300:
        speed [0] = -speed[0]
    
    if ballrect.top < 0 or ballrect.bottom > 600:
        speed [1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()