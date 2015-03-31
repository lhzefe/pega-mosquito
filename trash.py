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
        self.test_click = [False, False, False]
        self.count = [False, False, False]
        self.block = [False, False, False]

        #TRASH CAN OBJECT
        self.trash_can = pygame.image.load(trash_can)
        self.trash_can_spot = Image(surface, trash_can_spot, False, (473,337))

        #TRASH COVER OBJECT
        self.trash_cover = pygame.image.load(trash_cover)
        self.trash_cover_spot = Image(surface, trash_cover_spot, False, (480,515))

        #TRASH BAG OBJECT
        self.trash_bag = pygame.image.load(trash_bag)
        self.trash_bag_spot = Image(surface, trash_bag_spot, False, (473,180))

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
        self.trash_cover_spot.status = True
        self.trash_bag_spot.status = True

    def show_scene(self):
        self.transform_background.show()
        self.back_button.show()
        self.info_button.show()
        self.question_button.show()
        #SPOTS
        self.trash_can_spot.show()
        self.trash_cover_spot.show()
        self.trash_bag_spot.show()
        
        #TRASH_CAN
        if self.test_click[0] == False:
            self.surface.blit(self.trash_can, (120,180))
        else:
            if self.count[0] == True:
                self.surface.blit(self.trash_can, (478,342))
        #TRASH_COVER
        if self.test_click[1] == False:
            self.surface.blit(self.trash_cover, (127,356))
        else:
            if self.count[1] == True:
                self.surface.blit(self.trash_cover, (484,519))
        #TRASH_BAG
        if self.test_click[2] == False:
            self.surface.blit(self.trash_bag, (116,510))
        else:
            if self.count[2] == True:
                self.surface.blit(self.trash_bag, (476,184))

    def test_move(self, xy, event):
        if self.count[0] == False:
            if pygame.mouse.get_pressed()[0]:
                if xy[0] > 120 and xy[0] < 201 and xy[1] > 180 and xy[1] < 290 and \
                self.block[1] == False and self.block[2] == False:
                    self.test_click[0] = True
                    self.block[0] = True
                if self.test_click[0] == True and xy[0] > 100 and xy[0] < 600 and xy[1] > 173 and xy[1] < 630:
                    self.surface.blit(self.trash_can, (xy[0]-45,xy[1]-55))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.block[0] = False
                            if xy[0] > 473 and xy[0] < 568 and xy[1] > 337 and xy[1] < 455:
                                self.count[0] = True
                            else:
                                self.test_click[0] = False
                                self.count[0] = False

        if self.count[1] == False:
            if pygame.mouse.get_pressed()[0]:
                if xy[0] > 127 and xy[0] < 200 and xy[1] > 356 and xy[1] < 447 and \
                self.block[0] == False and self.block[2] == False:
                    self.test_click[1] = True
                    self.block[1] = True
                if self.test_click[1] == True and xy[0] > 100 and xy[0] < 600 and xy[1] > 173 and xy[1] < 630:
                    self.surface.blit(self.trash_cover, (xy[0]-45,xy[1]-55))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.block[1] = False
                            if xy[0] > 480 and xy[0] < 560 and xy[1] > 515 and xy[1] < 600:
                                self.count[1] = True
                            else:
                                self.test_click[1] = False
                                self.count[1] = False

        if self.count[2] == False:
            if pygame.mouse.get_pressed()[0]:
                if xy[0] > 118 and xy[0] < 206 and xy[1] > 501 and xy[1] < 596 and \
                self.block[0] == False and self.block[1] == False:
                    self.test_click[2] = True
                    self.block[2] = True
                if self.test_click[2] == True and xy[0] > 100 and xy[0] < 600 and xy[1] > 173 and xy[1] < 630:
                    self.surface.blit(self.trash_bag, (xy[0]-45,xy[1]-55))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.block[2] = False
                            if xy[0] > 473 and xy[0] < 572 and xy[1] > 180 and xy[1] < 278:
                                self.count[2] = True
                            else:
                                self.test_click[2] = False
                                self.count[2] = False