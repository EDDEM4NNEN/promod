import pygame
import sys
from entities import PhysicsEntity
from utils import load_image, load_images
from tilemap import Tilemap


pygame.init()

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280,720))

        self.display = pygame.Surface((640, 360))
        self.clock = pygame.time.Clock()
        self.movement = [0,0]

        self.assets = { #bruker load image og load images som ble definert i utils
            'grass' : load_images('tiles/grass'),
            'stone' : load_images('tiles/stone'),
            'player' : load_image('player/Geralt.png'),
            'background' : load_image('background/Witcher.png') #lagde feteste bakgrunn med GPT
        }

    
        self.player = PhysicsEntity(self, 'player', (50,50), (8,15)) #hvor spillerrektangelen spawner og hvor stor den er (den er 8 pikseler bred og 15 høy)
        self.tilemap = Tilemap(self, tile_size=16) #størrelsen på tilesa. jeg lagde de selv som 16x16
        self.tilemap.load('spillprosjekt/andre forsøk/map.json')
        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, -10)) #legger til bakgrunn og setter litt offset i høyden på bildet
            
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 5 #tok disse kamera funskjonene fra youtuberen DaFluffyPotato
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 10 #hva det siste er delt på er hvor smooth det er :)
            render_scroll = (int(self.scroll[0]), int(self.scroll[1])) # gjør som at spilleren ikke hakker på bakken, gjør de til integers s¨nn at det er mer smooth, de eneste som har desimaler som posisjon er spiller, bakker og tiles har ikke desimaler

            self.tilemap.render(self.display, offset = render_scroll) #lager blokkene før spilleren sånn at spilleren er over blokkene, offset = scroll er hvordan man beveger på tilesa
           


            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset = render_scroll)
            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                
                self.player.update #adda momentum fra entities samt hopping og gravitajson og også kun hopping på bakken
                    
                
    

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
           
            pygame.display.update()
            self.clock.tick(60)

Game().run()