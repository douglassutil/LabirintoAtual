import pygame,sys,os,time,random
from random import *


class Labirinto(object):

    def __init__(self,larg,alt):
        self.largura=larg
        self.altura=alt
        self.lstComponentes=[]# representa uma lista de Componentes
        Labirinto.make_maze(self)

    def walk(self,x,y,vis,ver,hor):# cria labirinto
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            Labirinto.walk(self,xx,yy,vis,ver,hor)

    def make_maze(self): # cria o labirinto aleatorio
        vis = [[0] * self.largura + [1] for _ in range(self.altura)] + [[1] * (self.altura + 1)]
        ver = [["|  "] * self.largura + ['|'] for _ in range(self.altura)] + [[]]
        hor = [["+--"] * self.largura + ['+'] for _ in range(self.altura + 1)]

        Labirinto.walk(self,randrange(self.largura), randrange(self.altura),vis,ver,hor)
        lab=Labirinto.juntaLista(self,ver,hor)
        maze=[]
        maze=Labirinto.converteLab(self,lab)
        self.lstComponentes = maze
        self.escolheFimInicio()


    def juntaLista(self,ver,hor):# junta duas listas intercaladas
        lab = [hor[0],ver[0]]
        for i in range(1,len(hor)):
            lab.append(hor[i])
            lab.append(ver[i])
        return lab

    def converteLab(self,lab):
        labirinto=[]
        for i in range(len(lab)):
            linha=[]
            for j in range(len(lab[i])):
                if(lab[i][j] == '+' or lab[i][j]=="|"):
                    linha.append("B")
                elif(lab[i][j]=="+--"):
                    linha.append("B")
                    linha.append("B")
                elif(lab[i][j]=="   "):
                     linha.append("M")
                     linha.append("M")
                elif(lab[i][j] == "|  " or lab[i][j]=="+  "):
                    linha.append("B")
                    linha.append("M")
            labirinto.append(linha)

        return(labirinto)


    def desenhaLabirinto(self,locx,locy):
       inicio=locx
       lstBlocos=[]
       lstMatos=[]
       lstinicioFim=[]
       for i in range(len(self.lstComponentes)):
          for j in range(len(self.lstComponentes[i])):
              if (self.lstComponentes[i][j]=="B"):
                 lstBlocos.append([locx,locy,30,30])
              elif(self.lstComponentes[i][j]=="M"):
                 lstMatos.append([locx,locy,30,30])
              elif(self.lstComponentes[i][j]=="I"):
                  coordInicio=[locx,locy,30,30]
                  lstMatos.append(coordInicio)
              elif(self.lstComponentes[i][j]=="F"):
                  coordFim=[locx,locy,30,30]
              locx+=30
          locx=inicio
          locy+=30
       lstCoordenadas=[lstBlocos,lstMatos,coordInicio,coordFim]
       return lstCoordenadas


    def geraCoordenada(self):
        linha=randint(0,len(self.lstComponentes)-2)
        coluna=randint(0,len(self.lstComponentes[0])-2)
        return(linha,coluna)

    def escolheFimInicio(self):
        linhaInicio,colunaInicio=Labirinto.geraCoordenada(self)
        while(self.lstComponentes[linhaInicio][colunaInicio]=="B"):
            linhaInicio,colunaInicio=Labirinto.geraCoordenada(self)
        self.lstComponentes[linhaInicio][colunaInicio]='I'


        linhaFinal,colunaFinal=Labirinto.geraCoordenada(self)

        while(self.lstComponentes[linhaFinal][colunaFinal]=="B" and colunaFinal==colunaInicio and linhaFinal==linhaInicio ):
            linhaFinal,colunaFinal=Labirinto.geraCoordenada(self)
        self.lstComponentes[linhaFinal][colunaFinal]='F'







