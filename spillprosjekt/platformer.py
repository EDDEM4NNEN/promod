import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, bredde, høyde):
        super().__init__()
        self.image = pygame.Surface((bredde, høyde))
        #self.image.fill("dark green")  # Grønn yeah buddy
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
