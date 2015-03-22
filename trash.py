from files import *
from image import *
import pygame
from pygame.locals import *

class Trash():
    def __init__(self, map, background, surface, menu, exit_button):        
        self.surface = surface
        self.background = background
        self.map = map
        self.menu = menu        
        self.exit_button = exit_button

        #BUTTONS
        self.back_button = Image(surface, back_button, False, (67,653))
        self.info_button = Image(surface, info_button, False, (165,653))
        self.question_button = Image(surface, question_button, False, (260,653))

        #SELECTION
        self.minor_selection_selected_back = Image(surface, minor_selection_selected, False, (67,653))
        self.minor_selection_selected_info = Image(surface, minor_selection_selected, False, (165,653))
        self.minor_selection_selected_question = Image(surface, minor_selection_selected, False, (260,653))

    def back_main_menu(self, xy, event, image = main_right_box):
        if xy[0] > 67 and xy[0] < 147 and xy[1] > 653 and xy[1] < 734:
            self.minor_selection_selected_back.status = True
            self.minor_selection_selected_back.show()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.background.switch_image(background)
                    self.menu.status = True
                    self.map.status = True
                    self.menu.switch_image(image)
                    self.exit_button.status = True
                    self.back_button.status = False
                    return True

    def info_painel(self, xy, event):
        if xy[0] > 165 and xy[0] < 245 and xy[1] > 653 and xy[1] < 734:
            self.minor_selection_selected_info.status = True
            self.minor_selection_selected_info.show()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass

    def question_painel(self, xy, event):
        if xy[0] > 260 and xy[0] < 342 and xy[1] > 653 and xy[1] < 734:
            self.minor_selection_selected_question.status = True
            self.minor_selection_selected_question.show()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass

    def open_scene(self):
        self.menu.status = False
        self.map.status = False
        self.exit_button.status = False
        self.background.switch_image(trash_menu_background)
        self.back_button.status = True
        self.info_button.status = True
        self.question_button.status = True

    def show_scene(self):
        self.back_button.show()
        self.info_button.show()
        self.question_button.show()