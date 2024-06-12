import pygame

class World(pygame.sprite.Sprite):

    def __init__(self,data,world_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(world_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.data = data
        self.waypoints=[]
        

    def process_data(self):
        for layer in self.data['layers']:
            if layer['name']=='waypoints':
                for obj in layer['objects']:
                    waypoint_data=obj['polyline']
                    self.process_coords(waypoint_data)
                        

    def process_coords(self,data):
        for point in data:
            #print("x="+str(coords['x'])+'y'+str(coords['y']))
            print((point.get('x'),point.get('y')))
            self.waypoints.append((point.get('x'),point.get('y')))
            #print(self.waypoints)

    def draw(self,surface):
        surface.blit(self.image,(0,0))