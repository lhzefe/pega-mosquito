#!/usr/bin/python
#-*- coding: utf-8 -*-

try:
    import sys
    from data.main import Game
    import pygame
except:
    print 'Error importing modules required.'
    exit(0)

if __name__ == '__main__':
    game = Game()
    game.loop()
    pygame.quit()
    sys.exit()
