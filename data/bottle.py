from files import *
from image import *
import pygame
from general import General
from pygame.locals import *

class Bottle():
    def __init__(self, map, transform_background, surface, menu, exit_button):        
        self.transform_background = transform_background
        self.surface = surface
        self.map = map
        self.menu = menu        
        self.exit_button = exit_button
        self.selected_movie = bottle_movie
        self.general = General(self.map, self.transform_background, self.surface, self.menu, self.exit_button, self.selected_movie)
        
        #GENERAL OBJECTS OF GAME
        self.test_click = [False, False, False]
        self.count = [False, False, False]
        self.block = [False, False, False]

        self.bottle_bottle_box = pygame.image.load(bottle_bottle_box)
        self.bottle_bottle_box_spot = Image(surface, bottle_bottle_box_spot, False, (473,337))

        self.bottle_bottle = pygame.image.load(bottle_bottle)
        self.bottle_bottle_spot = Image(surface, bottle_bottle_spot, False, (480,515))

        self.bottle_recycle_glass = pygame.image.load(bottle_recycle_glass)
        self.bottle_recycle_glass_spot = Image(surface, bottle_recycle_glass_spot, False, (473,180))

        #NEED SOLVE THE SOUNDS PROBLEM
        #pygame.mixer.quit()

    def open_scene(self):
        self.general.buttons_general()
        self.transform_background.switch_image(bottle_menu_background)
        self.bottle_bottle_box_spot.status = True
        self.bottle_bottle_spot.status = True
        self.bottle_recycle_glass_spot.status = True

    def show_scene(self):
        self.transform_background.show()
        self.general.buttons_general_show()
        #SPOTS
        self.bottle_bottle_box_spot.show()
        self.bottle_bottle_spot.show()
        self.bottle_recycle_glass_spot.show()
        #bottle_bottle_box
        if self.test_click[0] == False:
            self.surface.blit(self.bottle_bottle_box, (120,180))
        else:
            if self.count[0] == True:
                self.surface.blit(self.bottle_bottle_box, (478,342))
        #bottle_bottle
        if self.test_click[1] == False:
            self.surface.blit(self.bottle_bottle, (127,356))
        else:
            if self.count[1] == True:
                self.surface.blit(self.bottle_bottle, (484,519))
        #bottle_recycle_glass
        if self.test_click[2] == False:
            self.surface.blit(self.bottle_recycle_glass, (116,510))
        else:
            if self.count[2] == True:
                self.surface.blit(self.bottle_recycle_glass, (476,184))
        self.general.movie_background.show()
        if self.general.movie_background.status:
            self.surface.blit(self.general.movie_screen,(98,210))
        for movie_status in self.general.movie_status:
            movie_status.show()
        #BALLOONS
        for balloon in self.general.balloon:
            balloon.show()
        for text in self.general.bottle_text:
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
                            self.surface.blit(self.bottle_bottle_box, (xy[0]-45,xy[1]-55))
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
                            self.surface.blit(self.bottle_bottle, (xy[0]-45,xy[1]-55))
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
                            self.surface.blit(self.bottle_recycle_glass, (xy[0]-45,xy[1]-55))
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