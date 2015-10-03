from JogoLabirinto import *

class FinalJogo:
    def __init__(self):

        self.fonte = pygame.font.SysFont("comicsansms",80)
        self.textoTempo = self.fonte.render("TIME: ",1,(255,255,255))

        '''self.botaojogar = pygame.Rect(230,360,100,60) # paralelepipedo do tamanho do botao
        self.file_jogar=os.path.join("imagens","novapartida.png") #file recebe o local da imagem que sera utilizada
        self.jogarImage = pygame.image.load(self.file_jogar)
        self.jogarImagem = pygame.transform.scale(self.jogarImage,(150,60)) #se quiser redimensionar

        self.botaocreditos = pygame.Rect(230,430,100,60) # paralelepipedo do tamanho do botao
        self.file_creditos=os.path.join("imagens","creditos.png") #file recebe o local da imagem que sera utilizada
        self.creditosImage = pygame.image.load(self.file_creditos)
        self.creditosImagem = pygame.transform.scale(self.creditosImage,(150,60)) #se quiser redimensionar'''

        self.botaosair = pygame.Rect(230,500,100,60) # paralelepipedo do tamanho do botao
        self.file_sair=os.path.join("imagens","sair.png") #file recebe o local da imagem que sera utilizada
        self.sairImage = pygame.image.load(self.file_sair)
        self.sairImagem = pygame.transform.scale(self.sairImage,(150,60)) #se quiser redimensionar

        self.botaocursor =pygame.Rect(190,500,300,40) # tamanho do botao e localizacao
        self.file_cursor=os.path.join("imagens","cursor.png") #file recebe o local da imagem que sera utilizada
        self.cursorImage = pygame.image.load(self.file_cursor)
        self.cursorImagem = pygame.transform.scale(self.cursorImage,(30,40)) #se quiser redimensionar

        self.back = (0,0) # paralelepipedo do tamanho do botao
        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.backImagem = pygame.image.load(self.file_back)


        pygame.display.update()
        return

    def mostraMenuFinalJogo(self, controle):

        '''if controle.keys[0]: #se pressionar para cima
            if self.botaocursor[1] > 430:
                self.botaocursor[1]-=70

        if controle.keys[1]: #se pressionar para baixo
            if self.botaocursor[1] < 500:
                self.botaocursor[1]+=70'''

        if controle.keys[6]:#chama o jogo, creditos ou sair do jogo
            '''if self.botaocursor[1]==360:  # Implementar "Jogar Novamente"
                controle.opcao = 2'''

            '''if self.botaocursor[1]==430:
                controle.opcao = 4  # entrar nos creditos'''

            if self.botaocursor[1]==500:
                controle.opcao = 3 # sair do jogo

        if controle.keys[4]: # se pressionar esc
            controle.opcao = 3  # sair do jogo


        controle.screen.blit(self.backImagem,self.back) # printar background
        #controle.screen.blit(self.creditosImagem,self.botaocreditos) # printar botao de creditos
        #controle.screen.blit(self.jogarImagem,self.botaojogar) # printar a tela
        controle.screen.blit(self.sairImagem,self.botaosair) # printar botao sair
        #controle.screen.blit(self.jogarselecionadoImagem,self.botaojogarselecionado) # printar a tela
        controle.screen.blit(self.cursorImagem,self.botaocursor) # printar setinha

        tempo_ = format("Tempo: %d seg" %(controle.tempoTotal))
        JogoLabirinto.textoTempo = self.fonte.render(tempo_,1,(0,0,0))
        controle.screen.blit(JogoLabirinto.textoTempo,(60,90))

        pygame.display.update()
