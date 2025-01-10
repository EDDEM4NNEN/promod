import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]
        self.collisions = {"up": False, "down" : False, 'right': False, 'left': False}
        self.flip = False

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]) #posisjon er forresten ikke midten men top venstre
        

    def update(self, tilemap, movement = (0,0)):
        self.collisions = {"up": False, "down" : False, 'right': False, 'left': False}
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]                
        entity_rect = self.rect()                               #kollisjoner er kompliserte
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:  #hvis man beveger seg til høyre
                    entity_rect.right = rect.left 
                    self.collisions['right'] = True
                if frame_movement[0] < 0: #hvis man beveger seg til venstre
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x #oppdaterer spiller bildet til spiller rektangelet. hittil er alt dette i x posisjon.
                
        self.pos[1] += frame_movement[1]               
        entity_rect = self.rect()                               #kollisjoner er kompliserte
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:  #hvis man beveger seg til høyre
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0: #hvis man beveger seg til venstre
                    entity_rect.top = rect.bottom 
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y


#lager movement til player, prøver å få momentum, så legger jeg det inn spillprosjektet med self.player.update
        keys = pygame.key.get_pressed()
          #lager gravitasjon, der maks er 5 pikseler nedover på en frame
        if self.velocity[0] < -0.1:
            self.velocity[0] += 0.22
        elif self.velocity[0] > 0.1:
            self.velocity[0] -= 0.22
        else:
            self.velocity[0] = 0
        if keys[pygame.K_a]:  # left
            self.velocity[0] = max(-3, self.velocity[0] - 0.5)
            self.flip = True
        if keys[pygame.K_d]:  # right
            self.velocity[0] = min(3, self.velocity[0] + 0.5)
            self.flip = False

        if keys[pygame.K_w] and self.velocity[1] == 0 or keys[pygame.K_SPACE] and self.velocity[1] == 0:
             #hopper med enten W eller space
            self.velocity[1] = -5 #hopping blir mye lettere med dett
        self.velocity[1] = min(5, self.velocity[1] + 0.2)

#Collisions
        if self.collisions['down']: #gjør dette for å slutte å aksellerere når man er på bakken
            self.velocity[1] = 0
        if self.collisions['up']:
            self.velocity[1] = 0.1 #tar dette ikke på null sånn at man ikke kan hoppe evig når man er nær tak

        if self.collisions['right'] or self.collisions['left']:
             self.velocity[0] = 0



    def render(self, surf, offset = (0, 0)):
        surf.blit(pygame.transform.flip(self.game.assets['player'], self.flip, False),(self.pos[0] - offset[0], self.pos[1] - offset[1]))
     #   surf.blit(self.game.assets['player'], (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        #self.flip = False
