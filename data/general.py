try:
    from files import *
    from image import *
    import pygame
    from pygame.locals import *
except:
    print 'Error importing modules required.'
    exit(0)

class General():
    def __init__(self, map, transform_background, surface, menu, exit_button):        
        self.transform_background = transform_background
        self.surface = surface
        self.map = map
        self.menu = menu        
        self.exit_button = exit_button
        self.minor_selection_selected = []
        self.balloon = []
        self.button = []

        self.button.append( Image(surface, back_button, False, (67,653)) )
        self.button.append( Image(surface, info_button, False, (165,653)) )
        self.button.append( Image(surface, question_button, False, (260,653)) )
        self.minor_selection_selected.append( Image(surface, minor_selection_selected, False, (67,653)) )
        self.minor_selection_selected.append( Image(surface, minor_selection_selected, False, (165,653)) )
        self.minor_selection_selected.append( Image(surface, minor_selection_selected, False, (260,653)) )
        self.balloon.append( Image(surface, info_balloon, False, (167,328)) )
        self.balloon.append( Image(surface, question_balloon, False, (265, 328)) )

        #TRASH TEXTS
        self.trash_text = []
        self.trash_text.append( Image(surface, info_trash, False, (177, 413)) )
        self.trash_text.append( Image(surface, question_trash, False, (277, 430)) )

    def buttons_general(self):
        self.menu.status = False
        self.map.status = False
        self.exit_button.status = False
        for button in self.button:
            button.status = True

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

    def info_painel(self, xy, event, current):
        if xy[0] > 165 and xy[0] < 245 and xy[1] > 653 and xy[1] < 734:
            self.minor_selection_selected[1].status = True
            self.minor_selection_selected[1].show()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.balloon[0].status == True:
                            self.balloon[0].status = False
                            if current[1] > 0 and current[1] < 7:
                                self.trash_text[0].status = False
                        else:
                            self.balloon[0].status = True
                            self.balloon[1].status = False
                            if current[1] == 1:
                                self.trash_text[0].status = True
                                self.trash_text[1].status = False

    def question_painel(self, xy, event, current):
        if xy[0] > 260 and xy[0] < 342 and xy[1] > 653 and xy[1] < 734:
            self.minor_selection_selected[2].status = True
            self.minor_selection_selected[2].show()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.balloon[1].status == True:
                            self.balloon[1].status = False
                            if current[1] > 0 and current[1] < 7:
                                self.trash_text[1].status = False
                        else:
                            self.balloon[1].status = True
                            self.balloon[0].status = False
                            if current[1] == 1:
                                self.trash_text[1].status = True
                                self.trash_text[0].status = False