from files import *
from image import *
import pygame
from pygame.locals import *

class Credits():
    def __init__(self, map, transform_background, surface, menu, exit_button):        
        self.transform_background = transform_background
        self.surface = surface
        self.map = map
        self.menu = menu        
        self.exit_button = exit_button
        self.button = []
        self.minor_selection_selected = []
        self.button.append( Image(surface, back_button, False, (67,653)) )
        self.minor_selection_selected.append( Image(surface, minor_selection_selected, False, (67,653)) )

    def open_scene(self):
        self.menu.status = False
        self.map.status = False
        self.exit_button.status = False
        self.button[0].status = True
        self.transform_background.switch_image(credits_box)

    def show_scene(self):
        self.transform_background.show()
        self.button[0].show()

    def buttons_general_show(self):
        for button in self.button:
            button.show()

    def back_main_menu(self, xy, event, image = main_right_box):
        if xy[0] > 67 and xy[0] < 147 and xy[1] > 653 and xy[1] < 734:
            self.minor_selection_selected[0].status = True
            self.minor_selection_selected[0].show()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.transform_background.switch_image(background)
                    self.menu.status = True
                    self.map.status = True
                    self.menu.switch_image(image)
                    self.exit_button.status = True
                    self.button[0].status = False
                    return True