import pygame,sys,os,time,math,random
from pygame.locals import *
from Labirinto import Labirinto

class JogoLabirinto:
    timer = 0

    def __init__(self):
        timer = 0
        self.i=0
        self.fonte = pygame.font.SysFont("comicsansms",25)
        self.textoTempo = self.fonte.render("TIME: ",1,(255,255,255))

        self.labirinto=Labirinto(10,10)
        self.lst=self.labirinto.desenhaLabirinto(0,0)

        # Objetos iniciais+player
        self.player = pygame.Rect(self.lst[2][0],self.lst[2][1],16,28) # paralelepipedo do tamanho do player
        self.file_player=os.path.join("imagens","mario.png") #file recebe o local da imagem que sera utilizada
        self.playerImagem = pygame.image.load(self.file_player)
        #self.playerImagem = pygame.transform.scale(playerImage,(16,28)) #se quiser redimensionar

        self.file_bloco=os.path.join("imagens","mato.png")
        self.blocoimage=pygame.image.load(self.file_bloco)
        self.blocoimagem = pygame.transform.scale(self.blocoimage,(30,30)) # para redimensionar
        self.blocos=self.lst[1]

        self.file_moita=os.path.join("imagens","bloco.png")
        self.moitaimage = pygame.image.load(self.file_moita)
        self.moitaimagem = pygame.transform.scale(self.moitaimage,(30,30)) #para redimensionar
        self.moitas = self.lst[0]

        self.file_saida=os.path.join("imagens","saida.png")
        self.saidaimage = pygame.image.load(self.file_saida)
        self.saidaimagem = pygame.transform.scale(self.saidaimage,(30,30)) #para redimensionar
        self.saida = pygame.Rect(self.lst[3][0],self.lst[3][1],30,30) #localizacao saida

        self.file_ganhou=os.path.join("imagens","ganhou.png")
        self.ganhouimage = pygame.image.load(self.file_ganhou)
        self.ganhou = (15,130)

        return

    def atualizaTempo(self, controle):
        self.i+=1
        if self.i>=15:
            controle.tempoTotal +=1
            self.i=0
        return


    def mostraJogo(self, controle):

        self.atualizaTempo(controle)

        speed = 10
        if controle.keys[0]:
            if self.player.top>=0 :
                dx=self.player[0]
                dy=self.player[1]
                self.player[1]-=speed
                for moita in self.moitas[:]:
                    if self.player.colliderect(moita):
                        self.player[0]=dx
                        self.player[1]=dy
        if controle.keys[1]:
            if self.player.bottom<=931 :
                dx=self.player[0]
                dy=self.player[1]
                self.player[1]+=speed
                for moita in self.moitas[:]:
                    if self.player.colliderect(moita):
                        self.player[0]=dx
                        self.player[1]=dy
        if controle.keys[2]:
            if self.player.left>=0:
                dx=self.player[0]
                dy=self.player[1]
                self.player[0]-=speed
                for moita in self.moitas[:]:
                    if self.player.colliderect(moita):
                        self.player[0]=dx
                        self.player[1]=dy
        if controle.keys[3]:
            if self.player.right<=931 :
                dx=self.player[0]
                dy=self.player[1]
                self.player[0]+=speed
                for moita in self.moitas[:]:
                    if self.player.colliderect(moita):
                        self.player[0]=dx
                        self.player[1]=dy

        if self.player.colliderect(self.saida):
            controle.screen.fill(0)
            '''controle.screen.blit(self.ganhouimage,self.ganhou)
            tempo_ = format("Seu tempo foi de %d segundos" %(self.timer))
            self.textoTempo = self.fonte.render(tempo_,1,(255,255,255))
            controle.screen.blit(self.textoTempo,(130,-2))
            pygame.display.update()
            #pygame.mixer.music.play(-1)
            #pygame.display.update()
            time.sleep(3)'''
            controle.opcao=5

        for moita in self.moitas: # printando as moitas
            controle.screen.blit(self.moitaimagem,moita)

        for bloco in self.blocos:
            controle.screen.blit(self.blocoimagem,bloco)

        controle.screen.blit(self.playerImagem,self.player) # printar a tela (com player)

        controle.screen.blit(self.saidaimagem,self.saida)
        tempo_ = format("TIME: %d" % controle.tempoTotal )
        self.textoTempo = self.fonte.render(tempo_,1,(255,255,255))
        controle.screen.blit(self.textoTempo,(250,-2))

        pygame.display.update()

        return

