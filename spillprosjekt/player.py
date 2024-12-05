import pygame
import numpy as np

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 35))  #(bredde, høyde) Create a basic player rectangle
        self.image.fill((0,0,0))           # rød farge
        self.rect = self.image.get_rect()      # Get the rectangle of the surface
        self.rect.topleft = (x, y)            # Set the player's initial position

        # Movement attributes
        self.speed = 2  # Movement speed
        self.velocity_x = 0
        self.velocity_y = 0

    def input(self, platforms):
        #fart vannrett
        if self.velocity_x < 0:
            self.velocity_x += 0.5
        elif self.velocity_x > 0:
            self.velocity_x -= 0.5
        self.velocity_x = np.clip(self.velocity_x,-10,10) #setter maksimal og minimal verdi

        self.velocity_y += 0.7
        self.velocity_y = np.clip(self.velocity_y,-1000, 20) #maksimal og minimal verdi
        self.on_ground = pygame.sprite.spritecollide(self, platforms, False)

        keys = pygame.key.get_pressed() # definerer keys
        if keys[pygame.K_a]:  # left
            self.velocity_x -= self.speed
        if keys[pygame.K_d]:  # right
            self.velocity_x += self.speed

        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.on_ground: 
            self.velocity_y -= 20
            
    def update(self): #oppdaterer posisjonen til player
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

