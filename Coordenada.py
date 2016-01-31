# TAD Coordenada
class Coordenada(object):
    
    def __init__(self, lin, col):
        '''lin: int
           col: int
           retorna: Coordenada, em que lin corresponde as linhas de um
           tabuleiro ou matriz e col as colunas'''
        if isinstance(lin, int) and isinstance(col, int) and 0<lin<4\
           and 0<col<4:
            self.lin = lin
            self.col = col
            
        else:
            raise ValueError('class Coordenada: argumentos invalidos.')
        
    def getCol(self):
        '''coord: Coordenada
           retorna: int, coluna de coord'''
        
        return self.col
    
    def getLin(self):
        '''coord: Coordenada
           retorna: int, linha de coord'''
        
        return self.lin
    
    def __eq__(self, other):
        try:
            return self.getLin() == other.getLin() and\
                   self.getCol() == other.getCol()
        except:
            return False

    def __repr__(self):
        return "(%d, %d)" %(self.lin, self.col)
    
    def __hash__(self):
        return hash(repr(self))
