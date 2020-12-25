import pygame
from pygame.time import Clock

LARGURA = 400
ALTURA = 700
SPEED = -5
GRAVITY = 0.1
GAME_SPEED = 1

GROUND_WIDTH = 2 * LARGURA
GROUND_HEIGTH = 100

pygame.init() #Iniciar o pygame
screen = pygame.display.set_mode((LARGURA, ALTURA)) # Setar a tela com altura e largura

BACKGROUND = pygame.image.load('background-day.png') 
BACKGROUND = pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA)) 

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, xpos):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('base.png')
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGTH))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = ALTURA - GROUND_HEIGTH
# testando
    def update(self):
        self.rect[0] -= GAME_SPEED

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('bluebird-upflap.png').convert_alpha(),
                       pygame.image.load('bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('bluebird-downflap.png').convert_alpha()]

        self.current_image = 0
        self.speed = SPEED

        self.image = pygame.image.load('bluebird-upflap.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA / 2
        self.rect[1] = ALTURA / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        self.speed += GRAVITY
       
        # Update heigth
        self.rect [1] += self.speed
    
    def bump(self):
        self.speed = -3

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()

for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

#Clock = pygame.time.Clock()

while True:
    for event in pygame.event.get(): #verificar se não que sair
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    screen.blit(BACKGROUND, (0, 0)) # Setar inicio da tela

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        new_ground = Ground(GROUND_WIDTH)
        ground_group.add(new_ground)

    bird_group.update()
    ground_group.update()

    bird_group.draw(screen)
    ground_group.draw(screen)

    pygame.display.update() # Atualizar tela