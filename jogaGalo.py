from Coordenada import *
from Tabuleiro import *
import random
import time

class jogaGalo(object):
    '''play: Coordenada, ultima jogada do adversario. Se for a coordenada (0,0)
       e porque sou o primeiro a jogar
       retorna: Coordenada, jogada a tomar'''
    
    def __init__(self, tab):
        '''tab: Tabuleiro'''
    
        self.tab = tab
        if len(self.tab.emptyPositions()) > 7:
            self.jog = 0
            self.adj = {Coordenada(1,1):(Coordenada(2,1),Coordenada(2,2),Coordenada(1,2)),\
                        Coordenada(1,2):(Coordenada(1,1),Coordenada(2,2),Coordenada(1,3)),\
                        Coordenada(1,3):(Coordenada(1,2),Coordenada(2,2),Coordenada(2,3)),\
                        Coordenada(2,1):(Coordenada(1,1),Coordenada(2,2),Coordenada(3,1)),\
                        Coordenada(2,3):(Coordenada(1,3),Coordenada(2,2),Coordenada(3,3)),\
                        Coordenada(3,1):(Coordenada(2,1),Coordenada(2,2),Coordenada(3,2)),\
                        Coordenada(3,2):(Coordenada(3,1),Coordenada(2,2),Coordenada(3,3)),\
                        Coordenada(3,3):(Coordenada(3,2),Coordenada(2,2),Coordenada(2,3)),\
                        Coordenada(2,2):(Coordenada(1,1),Coordenada(1,2),Coordenada(1,3),\
                                         Coordenada(1,2),Coordenada(1,2),Coordenada(1,2),\
                                         Coordenada(1,2),Coordenada(1,2))}
        
            if len(self.tab.emptyPositions()) == 9:
                self.me = 'X'
                self.them = 'O'
            
            elif len(self.tab.emptyPositions()) == 8:
                self.me = 'O'
                self.them = 'X'
                
            self.terminado = False
            self.posVazias = self.tab.emptyPositions()
            
        else:
            raise ValueError('argumentos invalidos: nao e um tabuleiro inicial')
        
    def setPosition(self, coord, marcador):
        '''coord: Coordenada
           marcador: str, 'X' ou 'O' '''
        self.tab.setPosition(coord, marcador)
        
    def getTab(self):
        return self.tab
    
    def getMarcador(self):
        return self.me
    
    def getEmptyPositions(self):
        return self.tab.emptyPositions()
    
    def isFinished(self):
        return self.tab.isFinished()
    
    def canWin(self, marcador):
        '''marcador: str, 'X' ou 'O'
           return: tuple de dois elementos. O primerio e bool, True caso o
           o marcador tenha hipotese de ganhar e False caso contrario. O
           segundo elemento, caso o primeiro seja True retorna a coordenada
           necessariapara o marcador ganhar e caso seja False retorna None'''
        
        Lcol = []
        nDiag1 = 0
        nDiag2 = 0
        if self.me == marcador:
            notMarcador = self.them
        else:
            notMarcador = self.me
        
        for lin in range(1,4):
            Lcol = [self.tab.getPosition(Coordenada(1,lin)),\
                    self.tab.getPosition(Coordenada(2,lin)),\
                    self.tab.getPosition(Coordenada(3,lin))]
            n = 0
            for i in range(3):                  
                
                if Lcol[i] == notMarcador:
                    break
                elif Lcol[i] == marcador:
                    n += 1
                else:
                    jogada = Coordenada(i+1, lin)
                if n == 2 and i == 2:
                    return True, jogada
            
            n = 0
            
            for col in range(1,4):
                pos = Coordenada(lin, col)
                valor = self.tab.getPosition(pos)
                
                #if destinado a diagonal    
                if pos in (Coordenada(1,1), Coordenada(2,2), Coordenada(3,3))\
                   and nDiag1 != -1:
                    
                    if valor == notMarcador:
                        nDiag1 = -1
                    elif valor == marcador:
                        nDiag1 += 1
                    else:
                        jogada1 = pos
                    if lin == 3 and nDiag1 == 2:
                        return True, jogada1
                                                
                #destinado a anti-diagonal       
                if pos in (Coordenada(3,1), Coordenada(2,2), Coordenada(1,3))\
                   and nDiag2 != -1:
                    if valor == notMarcador:
                        nDiag2 = -1
                    elif valor == marcador:
                        nDiag2 += 1
                    else:
                        jogada2 = pos
                                                    
                    if lin == 3 and nDiag2 == 2:
                        return True, jogada2
                
                #destinado as linhas 
                if n != -1:
                    if valor == notMarcador: 
                        n = -1
                    elif valor == marcador:
                        n += 1
                    else:
                        jogada = pos
                
                    if n == 2 and col == 3:
                        return True, jogada
                
        return False, None
    
   
    def nextPlay(self, play):
        '''play: Coordenada, ultima jogada do adversario. Caso nao tenha havido
           nenhuma jogada anterior, play devera ser None'''
        
        flag = True
        if self.posVazias == []:
            self.terminado = True
        elif not (play in self.posVazias) and play:
            flag = False
        elif play:
            self.tab.setPosition(play, self.them)
            self.posVazias = self.tab.emptyPositions()
            if self.posVazias == []:
                self.terminado = True
        
        
        if (isinstance(play, Coordenada) or play == None)\
           and not self.terminado and flag:
        
            # Defesa - segundo a jogar
            if self.me == 'O':
                #se for primeira jogada
                if self.jog == 0:
                    play = self.tab.occupiedPos()[0]
                    
                    self.jog += 1
                    #se jogou no meio
                    if play == Coordenada(2,2):
                        self.jog = 10
                        jogada = random.choice((Coordenada(1,1), Coordenada(1,\
                                                                            3),\
                                              Coordenada(3,1), Coordenada(3,3)))
                        
                    #se nao jogou no meio
                    else:
                        jogada = Coordenada(2,2)
                # segunda jogada - se jogou no meio na primeira jogada    
                elif self.jog == 10:
                    self.jog = 11
                    
                    decision = self.canWin(self.them)
                    if decision[0]:
                        jogada = decision[1]
                    
                    else:
                        for ele in self.posVazias:
                            if (ele.getLin() == 1 or ele.getLin() == 3) and\
                               (ele.getCol() == 1 or ele.getCol() == 3):
                                
                                jogada = ele
                #resto do jogo            
                else:
                    decision1 = self.canWin(self.me)
                    
                    #se poder ganhar jogo la
                    if decision1[0]:
                        jogada = decision1[1]
                        self.terminado = True
                        
                    
                    #se nao puder ganhar
                    else:
                        decision2 = self.canWin(self.them)
                        #se adversario pode ganhar jogo la
                        if decision2[0]:
                            jogada = decision2[1]
                        
                        #se nao jogo adjacente
                        else:
                            jogada = random.choice(self.adj[play])
                            while not jogada in self.posVazias:
                                jogada = random.choice(self.adj[play])
                        
                self.tab.setPosition(jogada, self.me)
                return jogada                
            
            #se for o primeiro a jogar            
            else:
                #se for a primeira jogada
                if self.jog == 0:
                    #vinte por cento das vezes jogo nos cantos e nas 
                    #restantes jogo no centro
                    jogada = random.choice((Coordenada(2,2), Coordenada(2,2),\
                                            Coordenada(2,2), Coordenada(2,2),\
                                            random.choice((Coordenada(1,1),\
                                                           Coordenada(1,3),\
                                                           Coordenada(3,1),\
                                                           Coordenada(3,3)))))
                    
                    if jogada ==  Coordenada(2,2):
                        self.jog = 2
                    else:
                        self.jog += 1
                        self.PrimMe = jogada
                        
                #se segunda jogada:
                elif self.jog == 1 or self.jog == 2:
                    #se joguei no centro
                    if self.jog == 2:
                        #se jogou nos cantos
                        if (play.getLin() == 1 or play.getLin() == 3) and\
                           (play.getCol() == 1 or play.getCol() == 3):
                            #jogar espelho
                            jogada = self.tab.getEspelho(play)
    
                            #definir self.jog diferente 1
                            self.jog = 10
                            
                        #else
                        else:
                            #jogar num dos cantos opostos
                            jogada = random.choice(self.tab.getCantosOpostos\
                                                   (play))
                            self.jog = 3
                                
                    #se nao joguei centro
                    else:
                        #se jogou centro
                        if play == Coordenada(2,2):
                            #jogar espelho da jogada anterior minha
                            jogada = self.tab.getEspelho(self.PrimMe)
                            self.jog = 3
                        #se nao jogou centro
                        else:
                            #jogar centro
                            jogada = Coordenada(2,2)
                            #definir slf.jog diferente 2
                            self.jog = 11
                            self.PrimThem = play
                
                #se self.jog diferente
                elif self.jog == 10 or self.jog == 11:
                    #se adversario puder ganhar jogar la
                    decision1 = self.canWin(self.me)
                    decision2 = self.canWin(self.them)
                    if decision1[0]:
                        jogada = decision1[1]
                    
                    elif decision2[0]:
                        jogada = decision2[1]
                    #else
                    else:
                        #se self.jog == diferente 2
                        if self.jog == 11 and\
                           play == self.tab.getEspelho(self.PrimMe):
                            #play = encontrar ultima jogada
                            play = self.PrimThem
                    
                        opcoes = self.tab.getCantosOpostos(play)
                        #jogar num canto do lado oposto de play
                        for ele in opcoes:
                            if ele in self.posVazias:
                                jogada = ele
                            
                    self.jog = 3
                #resto do jogo
                else:
                    decision1 = self.canWin(self.me)
                    decision2 = self.canWin(self.them)
                    #ver se podemos ganhar
                    if decision1[0]:
                        self.terminado = True
                        jogada = decision1[1]
                        #ver se adv pode ganhar
                    elif decision2[0]:
                        jogada = decision2[1]
                        #else jogar adj
                    elif len(self.posVazias) == 1:
                        jogada = self.posVazias[0]
                    else:
                        jogada = random.choice(self.adj[play])
                        while not jogada in self.posVazias:
                            jogada = random.choice(self.adj[play])
                    
                self.tab.setPosition(jogada, self.me)
                self.posVazias = self.tab.emptyPositions()
                return jogada
                
        elif self.terminado:
            return ('Jogo terminado.')
        else:        
            raise ValueError('argumentos invalidos: tem de ser uma posicao\
            vazia')
            
            
