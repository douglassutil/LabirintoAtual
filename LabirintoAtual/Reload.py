import pygame,sys,os,time,math,random


class Reload:
    def __init__(self):
        self.botaojogar = pygame.Rect(230,200,100,60) # paralelepipedo do tamanho do botao
        self.file_jogar=os.path.join("imagens","jogarnovamente.png") #file recebe o local da imagem que sera utilizada
        self.jogarImage = pygame.image.load(self.file_jogar)
        self.jogarImagem = pygame.transform.scale(self.jogarImage,(150,60)) #se quiser redimensionar

        self.botaosair = pygame.Rect(230,400,100,60) # paralelepipedo do tamanho do botao
        self.file_sair=os.path.join("imagens","sair.png") #file recebe o local da imagem que sera utilizada
        self.sairImage = pygame.image.load(self.file_sair)
        self.sairImagem = pygame.transform.scale(self.sairImage,(150,60)) #se quiser redimensionar

        self.botaocursor = pygame.Rect(100,400,100,60) # paralelepipedo do tamanho do botao
        self.file_cursor=os.path.join("imagens","cursor.png") #file recebe o local da imagem que sera utilizada
        self.cursorImage = pygame.image.load(self.file_cursor)
        self.cursorImagem = pygame.transform.scale(self.cursorImage,(80,40)) #se quiser redimensionar

        self.back = (0,0) # paralelepipedo do tamanho do botao
        self.file_back=os.path.join("imagens","back.png") #file recebe o local da imagem que sera utilizada
        self.backImagem = pygame.image.load(self.file_back)
        return

    def mostraMenuReload(self, controle):
        if controle.keys[0]:
            self.botaocursor[1]=200

        if controle.keys[1]:
            self.botaocursor[1]=400

        if controle.keys[6]:#chama o jogo ou sai do jogo
            if self.botaocursor[1]==200:
                controle.opcao = 2

            if self.botaocursor[1]==400:
                controle.opcao = 3

        if controle.keys[4]:
            controle.opcao = 3

        controle.screen.blit(self.backImagem,self.back) # printar backgroud
        controle.screen.blit(self.jogarImagem,self.botaojogar) # printar botao jogar
        controle.screen.blit(self.sairImagem,self.botaosair) # printar botao sair
        controle.screen.blit(self.cursorImagem,self.botaocursor) # printar cursor

        pygame.display.update()

