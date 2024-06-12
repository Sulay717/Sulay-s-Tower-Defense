import pygame

class World(pygame.sprite.Sprite):

    def __init__(self,data,world_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(world_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.data = data
        self.waypoints=[]
        

    def process_data(self):
        for row in self.data:
            if row == 'layers':
                print('found row')
                for layer in self.data[row]:
                    #print(layer)
                    if layer['name']=='waypoints':
                        print('found objects')
                        self.process_coords(layer)

    def process_coords(self,layer):
        for objects in layer['objects']:
            for coords in objects['polyline']:
                #print("x="+str(coords['x'])+'y'+str(coords['y']))
                self.waypoints.append((coords['x'],coords['y']))
                print(self.waypoints)

    def draw(self,surface):
        surface.blit(self.image,(0,0))