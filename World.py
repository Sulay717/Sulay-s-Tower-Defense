import pygame

class World():

    def __init__(self,data,world_image):
        self.image = pygame.image.load(world_image).convert_alpha()
        self.data = data
        self.waypoints=[]
        
    #iterates through the level.tmj to find the polyline which contains the coordinates for the waypoint
    def process_data(self):
        for layer in self.data['layers']:
            if layer['name']=='waypoints':
                for obj in layer['objects']:
                    waypoint_data=obj['polyline']
                    self.process_coords(waypoint_data)
                        
    #takes in the polyline table and iterates through, creates (x,y) sets and appends it to the waypoints table.
    def process_coords(self,data):
        for point in data:
            temp_x = point.get('x')
            temp_y= point.get('y')
            self.waypoints.append((temp_x,temp_y))

    #draws the world map
    def draw(self,surface):
        surface.blit(self.image,(0,0))