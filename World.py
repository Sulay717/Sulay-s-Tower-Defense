import pygame

class World(pygame.sprite.Sprite):
    def __init__(self,data,world_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(world_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.data = data

    def process_data(self):
        for row in self.data:
            if row == 'layers':
                print('found row')
                for layer in self.data[row]:
                    #print(layer)
                    if layer['name']=='waypoints':
                        print('found objects')
                        for objects in layer['objects']:
                            for coords in objects['polyline']:
                                print("x="+str(coords['x'])+'y'+str(coords['y']))

    def draw(self,surface):
        surface.blit(self.image,(0,0))