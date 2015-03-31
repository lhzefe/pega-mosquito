from files import *
from image import *
import pygame
from pygame.locals import *

class Trash():
    def __init__(self, map, transform_background, surface, menu, exit_button):        
        self.transform_background = transform_background
        self.surface = surface
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

        #GENERAL OBJECTS OF GAME
        self.test_click = []
        self.count = [False, False, False]
        self.test_click.append(False)

        #TRASH CAN OBJECT
        self.trash_can = pygame.image.load(trash_can)
        self.test_click[0] = False

        self.trash_can_spot = Image(surface, trash_can_spot, False, (473,337))

    def back_main_menu(self, xy, event, image = main_right_box):
        if xy[0] > 67 and xy[0] < 147 and xy[1] > 653 and xy[1] < 734:
            self.minor_selection_selected_back.status = True
            self.minor_selection_selected_back.show()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.transform_background.switch_image(background)
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
        self.transform_background.switch_image(trash_menu_background)
        self.back_button.status = True
        self.info_button.status = True
        self.question_button.status = True
        self.trash_can_spot.status = True

    def show_scene(self):
        self.transform_background.show()
        self.back_button.show()
        self.info_button.show()
        self.question_button.show()
        #TRASH_CAN
        self.trash_can_spot.show()
        if self.test_click[0] == False:
            self.surface.blit(self.trash_can, (120,180))
        elif self.test_click[0] == True and self.count[0] == True:
            self.surface.blit(self.trash_can, (478,343))
        

    def test_move(self, xy, event):
        if self.count[0] == False:
            if pygame.mouse.get_pressed()[0]:
                if xy[0] > 120 and xy[0] < 201 and xy[1] > 180 and xy[1] < 290:
                    self.test_click[0] = True
                if self.test_click[0] == True and xy[0] > 100 and xy[0] < 600 and xy[1] > 173 and xy[1] < 630:
                    self.surface.blit(self.trash_can, (xy[0]-45,xy[1]-55))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            if xy[0] > 473 and xy[0] < 568 and xy[1] > 337 and xy[1] < 455:
                                self.count[0] = True
                            else:
                                self.test_click[0] = False
                                self.count[0] = False