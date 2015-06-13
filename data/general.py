try:
    from files import *
    from image import *
    import pygame, pygame.mixer
    from pygame.locals import *
except:
    print 'Error importing modules required.'
    exit(0)

class General():
    def __init__(self, map, transform_background, surface, menu, exit_button, selected_movie):        
        self.transform_background = transform_background
        self.surface = surface
        self.map = map
        self.menu = menu        
        self.exit_button = exit_button
        self.minor_selection_selected = []
        self.balloon = []
        self.button = []
        self.selected_movie = selected_movie

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

        #PLANT POT TEXT
        self.pot_text = []
        self.pot_text.append( Image(surface, info_trash, False, (177, 413)) )
        self.pot_text.append( Image(surface, question_pot, False, (277, 430)) )

        #WATER BOX TEXT
        self.water_box_text = []
        self.water_box_text.append( Image(surface, info_trash, False, (177, 413)) )
        self.water_box_text.append( Image(surface, question_water_box, False, (277, 430)) )

        #TIRE TEXT
        self.tire_text = []
        self.tire_text.append( Image(surface, info_trash, False, (177, 413)) )
        self.tire_text.append( Image(surface, question_tire, False, (277, 430)) )

        #BOTTLE TEXT
        self.bottle_text = []
        self.bottle_text.append( Image(surface, info_trash, False, (177, 413)) )
        self.bottle_text.append( Image(surface, question_bottle, False, (277, 430)) )

        #SODA CAN TEXT
        self.soda_can_text = []
        self.soda_can_text.append( Image(surface, info_trash, False, (177, 413)) )
        self.soda_can_text.append( Image(surface, question_soda_can, False, (277, 430)) )

        #MOVIES STATUS
        self.movie_status = []
        self.movie_status.append( Image(surface, stop_button, False, (98,496)) )
        self.movie_status.append( Image(surface, pause_button, False, (219,496)) )
        self.movie_status.append( Image(surface, play_button, False, (338,496)) )

        #MOVIES VIDEOS
        self.movie_background = Image(surface, movie_background, False, (56,185))
        #pygame.mixer.quit()
        self.movie = pygame.movie.Movie(self.selected_movie)
        self.movie_screen = pygame.Surface(self.movie.get_size()).convert()
        self.movie.set_display(self.movie_screen)


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
                                self.pot_text[0].status = False
                                self.water_box_text[0].status = False
                                self.tire_text[0].status = False
                                self.bottle_text[0].status = False
                                self.soda_can_text[0].status = False
                        else:
                            self.balloon[0].status = True
                            self.balloon[1].status = False
                            if current[1] == 1:
                                self.trash_text[0].status = True
                                self.trash_text[1].status = False
                            elif current[1] == 2:
                                self.pot_text[0].status = True
                                self.pot_text[1].status = False
                            elif current[1] == 3:
                                self.water_box_text[0].status = True
                                self.water_box_text[1].status = False
                            elif current[1] == 4:
                                self.tire_text[0].status = True
                                self.tire_text[1].status = False
                            elif current[1] == 5:
                                self.soda_can_text[0].status = True
                                self.soda_can_text[1].status = False
                            elif current[1] == 6:
                                self.bottle_text[0].status = True
                                self.bottle_text[1].status = False

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
                                self.pot_text[1].status = False
                                self.water_box_text[1].status = False
                                self.tire_text[1].status = False
                                self.bottle_text[1].status = False
                                self.soda_can_text[1].status = False
                        else:
                            self.balloon[1].status = True
                            self.balloon[0].status = False
                            if current[1] == 1:
                                self.trash_text[1].status = True
                                self.trash_text[0].status = False
                            elif current[1] == 2:
                                self.pot_text[1].status = True
                                self.pot_text[0].status = False
                            elif current[1] == 3:
                                self.water_box_text[1].status = True
                                self.water_box_text[0].status = False
                            elif current[1] == 4:
                                self.tire_text[1].status = True
                                self.tire_text[0].status = False
                            elif current[1] == 5:
                                self.soda_can_text[1].status = True
                                self.soda_can_text[0].status = False
                            elif current[1] == 6:
                                self.bottle_text[1].status = True
                                self.bottle_text[0].status = False

    def congratulations_movie(self, xy, event):
        self.movie_background.status = True
        for movie_status in self.movie_status:
            movie_status.status = True
        if pygame.mouse.get_pressed()[0]:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if xy[1] > 496 and xy[1] < 577:
                        if  xy[0] > 98 and xy[0] < 177:
                            self.movie.rewind()
                            self.movie.stop()
                        if  xy[0] > 218 and xy[0] < 298:
                            self.movie.pause()
                        if  xy[0] > 338 and xy[0] < 418:
                            self.movie.play()