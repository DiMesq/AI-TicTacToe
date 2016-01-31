from Coordenada import *

# TAD Tabuleiro    
class Tabuleiro(object):
    '''Tabuleiro 3x3 representado internamente por uma lista, iniciado vazio.'''
    
    def __init__(self):
        self.tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
        self.espelho = {Coordenada(1,1): Coordenada(3,3),\
                        Coordenada(1,3): Coordenada(3,1),\
                        Coordenada(3,3): Coordenada(1,1),\
                        Coordenada(3,1): Coordenada(1,3)}
        
        self.cantosOpostos = {Coordenada(1,2): (Coordenada(3,1), Coordenada(3,3)),\
                              Coordenada(2,1): (Coordenada(1,3), Coordenada(3,3)),\
                              Coordenada(2,3): (Coordenada(1,1), Coordenada(3,1)),\
                              Coordenada(3,2): (Coordenada(1,1), Coordenada(1,3))}
            
    def setPosition(self, coord, letter):
        '''coord: coord, de um tabuleiro 3x3
           letter: str, X or O
           Modifies self'''
        
        self.tabuleiro[coord.getLin()-1][coord.getCol()-1] = letter
        
    def getPosition(self, coord):
        
        return self.tabuleiro[coord.getLin()-1][coord.getCol()-1]
    
    def occupiedPos(self):
        lst = [] 
        for l in range(1,4):
            for c in range(1,4):
                coord = Coordenada(l, c)
                if self.getPosition(coord) != '':
                    lst.append(coord)
                                  
        return lst        
        
    def getEspelho(self, coord):
        '''coord:Coordenada, tem de ser um canto do tabuleiro
           retorna:Coordenada, o canto oposto''' 
        try:
            return self.espelho[coord]
        except:
            raise ValueError('arg invalidos: coord tem de ser um canto do\
            tabuleiro')
        
    def getCantosOpostos(self, coord):
        '''coord: Coordenada, tem ser uma das posicoes laterais do tabuleiro
           retorna: tuple, os cantos do lado oposto'''
        try:
            return self.cantosOpostos[coord]
        except:
            raise ValueError('arg invalidos: coord tem de ser uma posicao\
            lateral do tabuleiro sem ser canto')

    def emptyPositions(self):
        '''returns: list, of coordinates of places still to play'''
        lst = []
        for l in range(1,4):
            for c in range(1,4):
                coord = Coordenada(l, c)
                if self.getPosition(coord) == '':
                    lst.append(coord)
                          
        return lst
    
    def __str__(self):
        
        s = ''
        for l in range(1,4):
            for c in range(1,4):
                end = ' '
                if c == 3:
                    end += '\n'
                
                s = s + '[ ' + self.getPosition(Coordenada(l,c)) + ' ]' + end
                    
        return s
    
    def isFinished(self):
        '''returns: bool, True if self is over or False otherwise'''
        
        if self.emptyPositions() == []:
            return True
        
        coluna = []
        
        
        for col in range(1, 4):
            for lin in range(1,4):
                if col == 1:
                    if self.getPosition(Coordenada(lin, 1)) != '' and\
                       self.getPosition(Coordenada(lin, 1)) ==\
                       self.getPosition(Coordenada(lin, 2)) ==\
                       self.getPosition(Coordenada(lin, 3)):
                        return True
            
                coluna.append(self.getPosition(Coordenada(lin, col)))
                
                if lin == 3:
                    if coluna[0] == coluna[1] == coluna[2] and coluna[0] != '':
                        return True
                    
                    coluna = []
             
        return (self.getPosition(Coordenada(1,1)) ==\
               self.getPosition(Coordenada(2,2)) ==\
               self.getPosition(Coordenada(3,3)) or\
               self.getPosition(Coordenada(3,1)) ==\
               self.getPosition(Coordenada(2,2)) ==\
               self.getPosition(Coordenada(1,3))) and\
               self.getPosition(Coordenada(2,2)) != ''
               
               
