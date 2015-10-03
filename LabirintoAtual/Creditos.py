import pygame,sys,os,time,math,random


class Creditos:
    def __init__(self):
        self.imagemCreditos = [0,0,361,361] # paralelepipedo do tamanho do botao
        self.file_creditos=os.path.join("imagens","backcreditos.png") #file recebe o local da imagem que sera utilizada
        self.creditosImage = pygame.image.load(self.file_creditos)


        return

    def mostraCreditos(self, controle):

        if controle.keys[4]:
            controle.opcao = 1

        controle.screen.fill(0) #limpar a tela

        controle.screen.blit(self.creditosImage,self.imagemCreditos) # printar a tela
        pygame.display.update()

        pygame.display.update()
