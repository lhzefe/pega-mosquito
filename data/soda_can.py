from files import *
from image import *
import pygame
from general import General
from pygame.locals import *

class SodaCan():
    def __init__(self, map, transform_background, surface, menu, exit_button):        
        self.transform_background = transform_background
        self.surface = surface
        self.map = map
        self.menu = menu        
        self.exit_button = exit_button
        self.selected_movie = soda_can_movie
        self.general = General(self.map, self.transform_background, self.surface, self.menu, self.exit_button, self.selected_movie)
        
        #GENERAL OBJECTS OF GAME
        self.test_click = [False, False, False]
        self.count = [False, False, False]
        self.block = [False, False, False]

        self.soda_can_can = pygame.image.load(soda_can_can)
        self.soda_can_can_spot = Image(surface, soda_can_can_spot, False, (473,337))

        self.soda_can_recycle_metal = pygame.image.load(soda_can_recycle_metal)
        self.soda_can_recycle_metal_spot = Image(surface, soda_can_recycle_metal_spot, False, (480,515))

        self.soda_can_bag = pygame.image.load(soda_can_bag)
        self.soda_can_bag_spot = Image(surface, soda_can_bag_spot, False, (473,180))

        #NEED SOLVE THE SOUNDS PROBLEM
        #pygame.mixer.quit()

    def open_scene(self):
        self.general.buttons_general()
        self.transform_background.switch_image(soda_can_menu_background)
        self.soda_can_can_spot.status = True
        self.soda_can_recycle_metal_spot.status = True
        self.soda_can_bag_spot.status = True

    def show_scene(self):
        self.transform_background.show()
        self.general.buttons_general_show()
        #SPOTS
        self.soda_can_can_spot.show()
        self.soda_can_recycle_metal_spot.show()
        self.soda_can_bag_spot.show()
        #soda_can_can
        if self.test_click[0] == False:
            self.surface.blit(self.soda_can_can, (120,180))
        else:
            if self.count[0] == True:
                self.surface.blit(self.soda_can_can, (478,342))
        #soda_can_recycle_metal
        if self.test_click[1] == False:
            self.surface.blit(self.soda_can_recycle_metal, (127,356))
        else:
            if self.count[1] == True:
                self.surface.blit(self.soda_can_recycle_metal, (484,519))
        #soda_can_bag
        if self.test_click[2] == False:
            self.surface.blit(self.soda_can_bag, (116,510))
        else:
            if self.count[2] == True:
                self.surface.blit(self.soda_can_bag, (476,184))
        self.general.movie_background.show()
        if self.general.movie_background.status:
            self.surface.blit(self.general.movie_screen,(98,210))
        for movie_status in self.general.movie_status:
            movie_status.show()
        #BALLOONS
        for balloon in self.general.balloon:
            balloon.show()
        for text in self.general.soda_can_text:
            text.show()

    def test_move(self, xy, event):
        if self.count != [True, True, True]:
            if self.count[0] == False:
                if pygame.mouse.get_pressed()[0]:
                    if xy[0] > 120 and xy[0] < 201 and xy[1] > 180 and xy[1] < 290 and \
                    self.block[1] == False and self.block[2] == False:
                        self.test_click[0] = True
                        self.block[0] = True
                    if self.test_click[0] == True:
                        if xy[0] > 77 and xy[0] < 605 and xy[1] > 154 and xy[1] < 630:
                            self.surface.blit(self.soda_can_can, (xy[0]-45,xy[1]-55))
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.block[0] = False
                                    if xy[0] > 473 and xy[0] < 568 and xy[1] > 337 and xy[1] < 455:
                                        self.count[0] = True
                                    else:
                                        self.test_click[0] = False
                                        self.count[0] = False
                        else:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.test_click[0] = False
                                    self.count[0] = False

            if self.count[1] == False:
                if pygame.mouse.get_pressed()[0]:
                    if xy[0] > 127 and xy[0] < 200 and xy[1] > 356 and xy[1] < 447 and \
                    self.block[0] == False and self.block[2] == False:
                        self.test_click[1] = True
                        self.block[1] = True
                    if self.test_click[1] == True:
                        if xy[0] > 77 and xy[0] < 605 and xy[1] > 154 and xy[1] < 630:
                            self.surface.blit(self.soda_can_recycle_metal, (xy[0]-45,xy[1]-55))
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.block[1] = False
                                    if xy[0] > 480 and xy[0] < 560 and xy[1] > 515 and xy[1] < 600:
                                        self.count[1] = True
                                    else:
                                        self.test_click[1] = False
                                        self.count[1] = False
                        else:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.test_click[1] = False
                                    self.count[1] = False

            if self.count[2] == False:
                if pygame.mouse.get_pressed()[0]:
                    if xy[0] > 118 and xy[0] < 206 and xy[1] > 501 and xy[1] < 596 and \
                    self.block[0] == False and self.block[1] == False:
                        self.test_click[2] = True
                        self.block[2] = True
                    if self.test_click[2] == True:
                        if xy[0] > 77 and xy[0] < 605 and xy[1] > 154 and xy[1] < 630:
                            self.surface.blit(self.soda_can_bag, (xy[0]-45,xy[1]-55))
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.block[2] = False
                                    if xy[0] > 473 and xy[0] < 572 and xy[1] > 180 and xy[1] < 278:
                                        self.count[2] = True
                                    else:
                                        self.test_click[2] = False
                                        self.count[2] = False
                        else:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                    self.test_click[2] = False
                                    self.count[2] = False

            if  self.count == [True, True, True]:
                return True