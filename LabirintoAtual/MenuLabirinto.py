__author__ = 'Douglas'

import pygame,sys,os,time,math,random


class MenuLabirinto:
    def __init__(self):
        self.botaojogar = pygame.Rect(230,150,100,60) # paralelepipedo do tamanho do botao
        self.file_jogar=os.path.join("imagens","jogar.png") #file recebe o local da imagem que sera utilizada
        self.jogarImage = pygame.image.load(self.file_jogar)
        self.jogarImagem = pygame.transform.scale(self.jogarImage,(150,60)) #se quiser redimensionar

        self.botaocreditos = pygame.Rect(230,250,100,60) # paralelepipedo do tamanho do botao
        self.file_creditos=os.path.join("imagens","creditos.png") #file recebe o local da imagem que sera utilizada
        self.creditosImage = pygame.image.load(self.file_creditos)
        self.creditosImagem = pygame.transform.scale(self.creditosImage,(150,60)) #se quiser redimensionar

        self.botaosair = pygame.Rect(230,350,100,60) # paralelepipedo do tamanho do botao
        self.file_sair=os.path.join("imagens","sair.png") #file recebe o local da imagem que sera utilizada
        self.sairImage = pygame.image.load(self.file_sair)
        self.sairImagem = pygame.transform.scale(self.sairImage,(150,60)) #se quiser redimensionar

        self.botaojogarselecionado = pygame.Rect(230,200,100,60) # paralelepipedo do tamanho do botao
        self.file_jogarselecionado=os.path.join("imagens","jogarselecionado.png") #file recebe o local da imagem que sera utilizada
        self.jogarselecionadoImage = pygame.image.load(self.file_jogarselecionado)
        self.jogarselecionadoImagem = pygame.transform.scale(self.jogarselecionadoImage,(150,60)) #se quiser redimensionar

        self.botaocursor =pygame.Rect(190,161,300,40) # tamanho do botao e localizacao
        self.file_cursor=os.path.join("imagens","cursor.png") #file recebe o local da imagem que sera utilizada
        self.cursorImage = pygame.image.load(self.file_cursor)
        self.cursorImagem = pygame.transform.scale(self.cursorImage,(30,40)) #se quiser redimensionar

        self.back = (0,0) # paralelepipedo do tamanho do botao
        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.backImagem = pygame.image.load(self.file_back)
        return

    def mostraMenu(self, controle):

        if controle.keys[0]:
            if self.botaocursor[1] > 161:
                self.botaocursor[1]-=100

        if controle.keys[1]:
            if self.botaocursor[1] < 361:
                self.botaocursor[1]+=100

        if controle.keys[6]:#chama o jogo ou sai do jogo
            if self.botaocursor[1]==161:
                controle.opcao = 2

            if self.botaocursor[1]==261:
                controle.opcao = 4

            if self.botaocursor[1]==361:
                controle.opcao = 3

        if controle.keys[4]:
            controle.opcao = 3


        controle.screen.blit(self.backImagem,self.back) # printar a tela
        controle.screen.blit(self.creditosImagem,self.botaocreditos) # printar a tela
        controle.screen.blit(self.jogarImagem,self.botaojogar) # printar a tela
        controle.screen.blit(self.sairImagem,self.botaosair) # printar a tela
        #controle.screen.blit(self.jogarselecionadoImagem,self.botaojogarselecionado) # printar a tela
        controle.screen.blit(self.cursorImagem,self.botaocursor) # printar a tela

        pygame.display.update()

