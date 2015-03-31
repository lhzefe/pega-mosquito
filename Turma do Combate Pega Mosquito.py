#!/usr/bin/python
#-*- coding: utf-8 -*-

try:
    import pygame
    from pygame.locals import *
    from files import *
    from image import *
    from trash import Trash
except:
    print 'Error importing modules required.'
    exit(0)



class Game():
    def __init__(self):
        pygame.init()
        self.run = True

        self.current = 0
        self.current_1 = 0
        self.current2 = 0
        self.current_2 = 0
        self.surface =  pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Turma do Combate: Pega Mosquito')

        #IMAGES
        self.background = Image(self.surface, background)
        self.transform_background = Image(self.surface, background)
        self.main_exit_button= Image(self.surface, main_exit_button)
        self.map = Image(self.surface, map)
        self.main_right_box = Image(self.surface, main_right_box)
        
        #SELECTIONS
        self.main_exit_button_selected = Image(self.surface, main_exit_button_selected)
        self.selection = Image(self.surface, trash_selected)
        self.selection_1 = Image(self.surface, plant_pot_selected)
        self.selection_2 = Image(self.surface, water_box_selected)
        self.selection_3 = Image(self.surface, tire_selected)
        self.selection_4 = Image(self.surface, soda_can_selected)
        self.selection_5 = Image(self.surface, bottle_selected)

        self.mouse = pygame.image.load(ball)

    def back_menu_and_exit(self, event):
        if self.current2 == 0:
            if self.xy[0] > 689 and self.xy[0] < 982 and self.xy[1] > 654 and self.xy[1] < 742:
                self.main_exit_button_selected.show((689, 654))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            try:
                                self.run = False
                            except:
                                pass

    def loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.run = False
            self.xy = pygame.mouse.get_pos()
            self.background.show()
            self.main_right_box.show()
            self.main_exit_button.show((689, 654))
            self.map.show()

            #TRASH
            if self.current == 0 and self.current2 == 0 and \
            self.xy[0] > 77 and self.xy[0] < 210 and self.xy[1] > 431 and self.xy[1] < 572:
                self.selection.show((78, 432))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.trash = Trash(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                            self.current2 = 1
                        
            #PLANT POT
            if self.current == 0 and self.current2 == 0 and \
            self.xy[0] > 309 and self.xy[0] < 375 and self.xy[1] > 425 and self.xy[1] < 548:
                self.selection_1.show((294, 425))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        pass

            #WATER BOX
            if self.current == 0 and self.current2 == 0 and \
            ((self.xy[0] > 386 and self.xy[0] < 586 and self.xy[1] > 425 and self.xy[1] < 486) or \
            (self.xy[0] > 390 and self.xy[0] < 555 and self.xy[1] > 484 and self.xy[1] < 509) or \
            (self.xy[0] > 433 and self.xy[0] < 600 and self.xy[1] > 384 and self.xy[1] < 425) or \
            (self.xy[0] > 390 and self.xy[0] < 474 and self.xy[1] > 503 and self.xy[1] < 543)):
                self.selection_2.show((386, 363))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        pass

            #TIRE
            if self.current == 0 and self.current2 == 0 and \
            ((self.xy[0] > 458 and self.xy[0] < 557  and self.xy[1] > 557 and self.xy[1] < 673) or \
            (self.xy[0] > 554 and self.xy[0] < 621 and self.xy[1] > 530 and self.xy[1] < 681) or \
            (self.xy[0] > 571 and self.xy[0] < 630 and self.xy[1] > 493 and self.xy[1] < 524)):
                self.selection_3.show((451, 483))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        pass

            #SODA CAN
            if self.current == 0 and self.current2 == 0 and \
            ((self.xy[0] > 204 and self.xy[0] < 301 and self.xy[1] > 598 and self.xy[1] < 653) or \
            (self.xy[0] > 257 and self.xy[0] < 274 and self.xy[1] > 572 and self.xy[1] < 598) or \
            (self.xy[0] > 247 and self.xy[0] < 301 and self.xy[1] > 653 and self.xy[1] < 694)):
                self.selection_4.show((194, 567))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        pass

            #BOTTLE
            if self.current == 0 and self.current2 == 0 and \
            self.xy[0] > 372 and self.xy[0] < 450 and self.xy[1] > 572 and self.xy[1] < 688:
                self.selection_5.show((368, 550))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        pass

            #EXIT
            self.back_menu_and_exit(event)

            #EVENTS
            if self.current2 == 1:
                self.trash.open_scene()
                self.trash.show_scene()
                if self.trash.back_main_menu(self.xy, event):
                    self.current2 = 0
                self.trash.info_painel(self.xy, event)
                self.trash.question_painel(self.xy, event)
                self.trash.test_move(self.xy, event)

            if (event.type == KEYDOWN and event.key == K_F4):
                self.surface = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
            elif (event.type == KEYDOWN and event.key == K_F3):
                self.surface = pygame.display.set_mode((1024, 768))
            pygame.display.update()

game = Game()
game.loop()
pygame.quit()
exit()