import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x,y, bredde, høyde):
        super().__init__()
        self.image = pygame.Surface((bredde, høyde))
        #self.image.fill("dark green")  # Grønn yeah buddy
        self.rect = self.image.get_rect(topleft = (x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
'''
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, bredde, høyde):
        super().__init__()
        self.image = pygame.Surface((bredde, høyde))  # Eksempelstørrelse
        self.rect = self.image.get_rect(topleft=(x,y))
        # En spesifikk gruppe tilknyttet denne plattformen
        self.subgroup = pygame.sprite.Group()
    def add_to_group(self, sprite):
        self.subgroup.add(sprite)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        '''
