import pygame

class World():

    def __init__(self,data,world_image):
        self.image = pygame.image.load(world_image).convert_alpha()
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
            temp_x = point.get('x')
            temp_y= point.get('y')
            print((temp_x,temp_y))
            self.waypoints.append((temp_x,temp_y))
            #print(self.waypoints)

    def draw(self,surface):
        surface.blit(self.image,(0,0))