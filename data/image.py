import pygame

class Image():
    def __init__(self, surface, image, status = True, position = (0,0)):
        self.position = position
        self.surface = surface
        self.status = status
        self.image = pygame.image.load(image)
    def show(self, new_position = False):
        if new_position == False:
            new_position = self.position
        if self.status:
            self.surface.blit(self.image,new_position)
    def switch_image(self, new_image):
        self.image = pygame.image.load(new_image)
