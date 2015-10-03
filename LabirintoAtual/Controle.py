import pygame,sys,os,time,math,random
from pygame.locals import *
from MenuLabirinto import MenuLabirinto
from JogoLabirinto import JogoLabirinto
from Creditos import Creditos
from FinalJogo import FinalJogo

class Controle:

    def __init__(self):
        self.opcao = 1
        self.mainClock = pygame.time.Clock()
        self.tempoTotal = 0
        return
    def controla(self):
        pygame.init()
        width,height = 632,632
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption('Labirinto do Capeta')
        self.menu = MenuLabirinto()
        self.jogo = JogoLabirinto()
        self.creditos = Creditos()
        self.finaljogo = FinalJogo()
                     #cima  #baixo #esqu  #dire  #esc         #espaco
        self.keys = [False, False, False, False, False, False,False]

        while self.opcao != 3:
            self.capturaEventos()

            if self.opcao == 1:
                self.menu.mostraMenu(self)

            elif self.opcao == 2:
                self.jogo.mostraJogo(self)

            elif self.opcao == 4:
                self.creditos.mostraCreditos(self)

            elif self.opcao == 5:
                self.finaljogo.mostraMenuFinalJogo(self)

            self.mainClock.tick(15)

        pygame.quit()
        sys.exit() # para sair de uma forma mais suave

    def capturaEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.opcao = 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.keys[0] = True
                if event.key == pygame.K_DOWN:
                    self.keys[1] = True
                if event.key == pygame.K_LEFT:
                    self.keys[2] = True
                if event.key == pygame.K_RIGHT:
                    self.keys[3] = True
                if event.key == pygame.K_ESCAPE:
                    self.keys[4] = True
                if event.key == pygame.K_SPACE:
                    self.keys[6] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.keys[0] = False
                if event.key == pygame.K_DOWN:
                    self.keys[1] = False
                if event.key == pygame.K_LEFT:
                    self.keys[2] = False
                if event.key == pygame.K_RIGHT:
                    self.keys[3] = False
                if event.key == pygame.K_ESCAPE:
                    self.keys[4] = False
                if event.key == pygame.K_SPACE:
                    self.keys[6] = False