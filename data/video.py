import pygame

class Video():
    def __init__(self, surface, video, status = True, position = (0,0)):
        self.position = position
        self.surface = surface
        self.status = status
        self.video = pygame.movie.Movie(video)
    def show(self, new_position = False):
        if new_position == False:
            new_position = self.position
        if self.status:
            self.surface.blit(self.video,new_position)
    def switch_video(self, new_video):
        self.video = pygame.movie.Movie(new_video)
