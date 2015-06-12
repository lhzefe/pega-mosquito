#!/usr/bin/python
#-*- coding: utf-8 -*-

try:
    import pygame
    from pygame.locals import *
    from files import *
    from image import *
    from trash import Trash
    from plant_pot import PlantPot
    from water_box import WaterBox
    from tire import Tire
    from soda_can import SodaCan
    from bottle import Bottle
except:
    print 'Error importing modules required.'
    exit(0)



class Game():
    def __init__(self):
        pygame.init()
        self.run = True

        self.current = [0, 0]
        self.score = 0
        self.level_completed = [False]*6

        self.surface =  pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Turma do Combate: Pega Mosquito')

        #IMAGES
        self.background = Image(self.surface, background)
        self.transform_background = Image(self.surface, background)
        self.main_exit_button= Image(self.surface, main_exit_button)
        self.map = Image(self.surface, map)
        self.main_right_box = Image(self.surface, main_right_box)

        #LOCKS
        self.lock = []
        self.lock.append( Image(self.surface, lock, True, (324, 460)) )
        self.lock.append( Image(self.surface, lock, True, (450, 430)) )
        self.lock.append( Image(self.surface, lock, True, (535, 570)) )
        self.lock.append( Image(self.surface, lock, True, (225, 590)) )
        self.lock.append( Image(self.surface, lock, True, (390, 590)) )

        #SELECTIONS
        self.selection = []
        self.selection.append( Image(self.surface, trash_selected) )
        self.selection.append( Image(self.surface, plant_pot_selected) )
        self.selection.append( Image(self.surface, water_box_selected) )
        self.selection.append( Image(self.surface, tire_selected) )
        self.selection.append( Image(self.surface, soda_can_selected) )
        self.selection.append( Image(self.surface, bottle_selected) )
        self.main_exit_button_selected = Image(self.surface, main_exit_button_selected)
        self.mouse = pygame.image.load(ball)

    def back_menu_and_exit(self, event):
        if self.current[1] == 0:
            if self.xy[0] > 689 and self.xy[0] < 982 and self.xy[1] > 654 and self.xy[1] < 742:
                self.main_exit_button_selected.show((689, 654))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            try:
                                self.run = False
                            except:
                                pass

    def score_text(self):
        font=pygame.font.SysFont("Comic Sans MS", 28)
        scoretext=font.render("Pontos: "+str(self.score), 1,(255,255,255))
        self.surface.blit(scoretext, (708, 57))

    def scenes_active(self, event):
        if self.current[1] == 1:
            self.trash.open_scene()
            self.trash.show_scene()
            if self.trash.general.back_main_menu(self.xy, event):
                self.current[1] = 0
                self.level_completed[0] = False
                self.trash.general.movie.stop()
            self.trash.general.info_painel(self.xy, event, self.current)
            self.trash.general.question_painel(self.xy, event, self.current)
            if self.trash.test_move(self.xy, event):
                self.score+= 100
                self.level_completed[0] = True
                self.lock[0].status = False
            if self.level_completed[0]:
                self.trash.general.congratulations_movie(self.xy, event)
        elif self.current[1] == 2:
            self.plant_pot.open_scene()
            self.plant_pot.show_scene()
            if self.plant_pot.general.back_main_menu(self.xy, event):
                self.current[1] = 0
                self.level_completed[1] = False
                self.plant_pot.general.movie.stop()
            self.plant_pot.general.info_painel(self.xy, event, self.current)
            self.plant_pot.general.question_painel(self.xy, event, self.current)
            if self.plant_pot.test_move(self.xy, event):
                self.score+= 100
                self.level_completed[1] = True
                self.lock[1].status = False
            if self.level_completed[1]:
                self.plant_pot.general.congratulations_movie(self.xy, event)
        elif self.current[1] == 3:
            self.water_box.open_scene()
            self.water_box.show_scene()
            if self.water_box.general.back_main_menu(self.xy, event):
                self.current[1] = 0
                self.level_completed[2] = False
                self.water_box.general.movie.stop()
            self.water_box.general.info_painel(self.xy, event, self.current)
            self.water_box.general.question_painel(self.xy, event, self.current)
            if self.water_box.test_move(self.xy, event):
                self.score+= 100
                self.level_completed[2] = True
                self.lock[2].status = False
            if self.level_completed[2]:
                self.water_box.general.congratulations_movie(self.xy, event)
        elif self.current[1] == 4:
            self.tire.open_scene()
            self.tire.show_scene()
            if self.tire.general.back_main_menu(self.xy, event):
                self.current[1] = 0
                self.level_completed[3] = False
                self.tire.general.movie.stop()
            self.tire.general.info_painel(self.xy, event, self.current)
            self.tire.general.question_painel(self.xy, event, self.current)
            if self.tire.test_move(self.xy, event):
                self.score+= 100
                self.level_completed[3] = True
                self.lock[3].status = False
            if self.level_completed[3]:
                self.tire.general.congratulations_movie(self.xy, event)
        elif self.current[1] == 5:
            self.soda_can.open_scene()
            self.soda_can.show_scene()
            if self.soda_can.general.back_main_menu(self.xy, event):
                self.current[1] = 0
                self.level_completed[4] = False
                self.soda_can.general.movie.stop()
            self.soda_can.general.info_painel(self.xy, event, self.current)
            self.soda_can.general.question_painel(self.xy, event, self.current)
            if self.soda_can.test_move(self.xy, event):
                self.score+= 100
                self.level_completed[4] = True
                self.lock[4].status = False
            if self.level_completed[4]:
                self.soda_can.general.congratulations_movie(self.xy, event)
        elif self.current[1] == 6:
            self.bottle.open_scene()
            self.bottle.show_scene()
            if self.bottle.general.back_main_menu(self.xy, event):
                self.current[1] = 0
                self.level_completed[5] = False
                self.bottle.general.movie.stop()
            self.bottle.general.info_painel(self.xy, event, self.current)
            self.bottle.general.question_painel(self.xy, event, self.current)
            if self.bottle.test_move(self.xy, event):
                self.score+= 100
                self.level_completed[5] = True
            if self.level_completed[5]:
                self.bottle.general.congratulations_movie(self.xy, event)

    def scene_selection(self, event):
        #TRASH
        if self.current[0] == 0 and self.current[1] == 0 and \
        self.xy[0] > 77 and self.xy[0] < 210 and self.xy[1] > 431 and self.xy[1] < 572:
            self.selection[0].show((78, 432))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.trash = Trash(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 1
                    
        #PLANT POT
        if self.current[0] == 0 and self.current[1] == 0 and self.lock[0].status == False and \
        self.xy[0] > 309 and self.xy[0] < 375 and self.xy[1] > 425 and self.xy[1] < 548:
            self.selection[1].show((294, 425))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.plant_pot = PlantPot(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 2

        #WATER BOX
        if self.current[0] == 0 and self.current[1] == 0 and self.lock[1].status == False and \
        ((self.xy[0] > 386 and self.xy[0] < 586 and self.xy[1] > 425 and self.xy[1] < 486) or \
        (self.xy[0] > 390 and self.xy[0] < 555 and self.xy[1] > 484 and self.xy[1] < 509) or \
        (self.xy[0] > 433 and self.xy[0] < 600 and self.xy[1] > 384 and self.xy[1] < 425) or \
        (self.xy[0] > 390 and self.xy[0] < 474 and self.xy[1] > 503 and self.xy[1] < 543)):
            self.selection[2].show((386, 363))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.water_box = WaterBox(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 3

        #TIRE
        if self.current[0] == 0 and self.current[1] == 0 and self.lock[2].status == False and \
        ((self.xy[0] > 458 and self.xy[0] < 557  and self.xy[1] > 557 and self.xy[1] < 673) or \
        (self.xy[0] > 554 and self.xy[0] < 621 and self.xy[1] > 530 and self.xy[1] < 681) or \
        (self.xy[0] > 571 and self.xy[0] < 630 and self.xy[1] > 493 and self.xy[1] < 524)):
            self.selection[3].show((451, 483))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.tire = Tire(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 4

        #SODA CAN
        if self.current[0] == 0 and self.current[1] == 0 and self.lock[3].status == False and \
        ((self.xy[0] > 204 and self.xy[0] < 301 and self.xy[1] > 598 and self.xy[1] < 653) or \
        (self.xy[0] > 257 and self.xy[0] < 274 and self.xy[1] > 572 and self.xy[1] < 598) or \
        (self.xy[0] > 247 and self.xy[0] < 301 and self.xy[1] > 653 and self.xy[1] < 694)):
            self.selection[4].show((194, 567))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.soda_can = SodaCan(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 5

        #BOTTLE
        if self.current[0] == 0 and self.current[1] == 0 and self.lock[4].status == False and \
        self.xy[0] > 372 and self.xy[0] < 450 and self.xy[1] > 572 and self.xy[1] < 688:
            self.selection[5].show((368, 550))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.bottle = Bottle(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 6

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
            self.score_text()
            for lock in self.lock:
                lock.show()
            #CHOOSE A SCENE
            self.scene_selection(event)
            #EXIT
            self.back_menu_and_exit(event)
            #EVENTS
            if self.current[1] != 0:
                self.scenes_active(event)

            if (event.type == KEYDOWN and event.key == K_F4):
                self.surface = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
            elif (event.type == KEYDOWN and event.key == K_F3):
                self.surface = pygame.display.set_mode((1024, 768))
            pygame.display.update()