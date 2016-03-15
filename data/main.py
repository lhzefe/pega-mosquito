#!/usr/bin/python
#-*- coding: utf-8 -*-
try:
    import pygame, pygame.mixer
    from pygame.locals import *
    from files import *
    from image import *
    from trash import Trash
    from plant_pot import PlantPot
    from water_box import WaterBox
    from tire import Tire
    from soda_can import SodaCan
    from bottle import Bottle
    from credits import Credits    
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
        self.background = Image(self.surface, background)
        self.transform_background = Image(self.surface, background)
        self.main_exit_button= Image(self.surface, main_exit_button)
        self.map = Image(self.surface, map)
        self.main_right_box = Image(self.surface, main_right_box)
        self.lock = []
        self.lock.append( Image(self.surface, lock, True, (324, 460)) )
        self.lock.append( Image(self.surface, lock, True, (450, 430)) )
        self.lock.append( Image(self.surface, lock, True, (535, 570)) )
        self.lock.append( Image(self.surface, lock, True, (225, 590)) )
        self.lock.append( Image(self.surface, lock, True, (390, 590)) )
        self.game_music = pygame.mixer.Sound(game_music)
        self.game_music.play(-1)
        self.selection = []
        self.selection.append( Image(self.surface, trash_selected) )
        self.selection.append( Image(self.surface, plant_pot_selected) )
        self.selection.append( Image(self.surface, water_box_selected) )
        self.selection.append( Image(self.surface, tire_selected) )
        self.selection.append( Image(self.surface, soda_can_selected) )
        self.selection.append( Image(self.surface, bottle_selected) )
        self.credits_exit_button_selected = Image(self.surface, credits_exit_button_selected)
        self.mouse = pygame.image.load(ball)

    def menu_credits_and_exit(self, event):
        if self.current[1] == 0:
            if self.xy[1] > 654 and self.xy[1] < 742:
                if self.xy[0] > 842 and self.xy[0] < 982:
                    self.credits_exit_button_selected.show((842, 654))
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                try:
                                    self.run = False
                                except:
                                    pass
                elif self.xy[0] > 689 and self.xy[0] < 828:
                    self.credits_exit_button_selected.show((689, 654))
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                self.credits = Credits(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                                self.current[1] = 7

    def score_text(self):
        font=pygame.font.SysFont("Comic Sans MS", 28)
        scoretext=font.render("Pontos: "+str(self.score), 1,(255,255,255))
        self.surface.blit(scoretext, (708, 57))

    def scenes_active(self, event):
        if self.current[1] == 1:
            active = self.trash
        elif self.current[1] == 2:
            active = self.plant_pot
        elif self.current[1] == 3:
            active = self.water_box
        elif self.current[1] == 4:
            active = self.tire
        elif self.current[1] == 5:
            active = self.soda_can
        elif self.current[1] == 6:
            active = self.bottle
        elif self.current[1] == 7:
            active = self.credits
        if (self.current[1] >= 1 and self.current[1] < 7):
            active.open_scene()
            active.show_scene()
            if active.general.back_main_menu(self.xy, event):
                self.current[1] = 0
                self.level_completed[self.current[1] - 1] = False
                active.general.movie.stop()
            active.general.info_painel(self.xy, event, self.current)
            active.general.question_painel(self.xy, event, self.current)
            if active.test_move(self.xy, event):
                self.score+= 100
                self.level_completed[self.current[1] - 1] = True
                self.lock[self.current[1] - 1].status = False
            if self.level_completed[self.current[1] - 1]:
                active.general.congratulations_movie(self.xy, event)
        elif self.current[1] == 7:
            active.open_scene()
            active.show_scene()
            if active.back_main_menu(self.xy, event):
                self.current[1] = 0

    def scene_selection(self, event):
        if self.current[0] == 0 and self.current[1] == 0 and \
        self.xy[0] > 77 and self.xy[0] < 210 and self.xy[1] > 431 and self.xy[1] < 572:
            self.selection[0].show((78, 432))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.trash = Trash(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 1
                    
        if self.current[0] == 0 and self.current[1] == 0 and self.lock[0].status == False and \
        self.xy[0] > 309 and self.xy[0] < 375 and self.xy[1] > 425 and self.xy[1] < 548:
            self.selection[1].show((294, 425))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.plant_pot = PlantPot(self.map, self.transform_background, self.surface, self.main_right_box, self.main_exit_button)
                        self.current[1] = 2

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
            self.scene_selection(event)
            self.menu_credits_and_exit(event)
            if self.current[1] != 0:
                self.scenes_active(event)
            if (event.type == KEYDOWN and event.key == K_F4):
                self.surface = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
            elif (event.type == KEYDOWN and event.key == K_F3):
                self.surface = pygame.display.set_mode((1024, 768))
            pygame.display.update()