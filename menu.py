import pygame, sys
import random
import time
from pygame.locals import *
from pygame import mixer
mainClock = pygame.time.Clock()
pygame.init()
WIDTH = 1000
HEIGHT = 500
screen =  pygame.display.set_mode((1000,500),0,32)
font = pygame.font.SysFont(None, 20)


# verso = pygame.image.load(back_card)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect) 
def main_menu():
    while True:
        
        fonte = pygame.font.SysFont(None, 40)
        fonte2  = pygame.font.SysFont("Algerian", 110)
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        #tela_fundo = pygame.image.load('Pygame/table_top.png')
        tela_fundo = screen.fill(0,0,0)
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))
        '''if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()'''
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)
main_menu()


    