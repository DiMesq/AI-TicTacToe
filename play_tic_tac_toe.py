# Funcoes de jogo 
from Tabuleiro import *
from Coordenada import *
from jogaGalo import *
def validPlay(play):
    s = play
            
    if len(s) != 5:
        return False
            
    try:
        col = int(s[3])
        lin = int(s[1])
        if not (0 < col < 4 and 0 < lin < 4):
            return False
            
    except ValueError:
        return False
                    
    return s[0] == '(' and s[2] == ',' and s[4] == ')'
                
        
def askForPlay():
            
    play = input("Introduza uma jogada do tipo '(lin, col)': ")
    play = play.replace(' ', '')
            
    while not validPlay(play):
        print('Jogada invalida!\n')
        play = input("Introduza uma jogada do tipo '(lin, col)': ")
        play = play.replace(' ', '')
            
    jogada = play_Coordenada(play)    
    return jogada
        
def play_Coordenada(s):
    lin = int(s[1])
    col = int(s[3])
            
    return Coordenada(lin, col)
            
def jogo_do_galo():
            
    print('Vamos jogar ao jogo do galo!')
    primeiro = input("Se pretender que o computador seja o primeiro a jogar\
    introduza 'p': ")
    
    
    tab = Tabuleiro()
    if primeiro == 'p':
        PCplay = jogaGalo(tab)
        flag = True
        
    else:
        flag = False
        
    k = 0
    
    while not tab.isFinished():
        if k % 2 == 0:
            valor = 'X'
                    
        else:
            valor = 'O'
        
        if (k % 2 == 0 and not flag) or (k%2 != 0 and flag): 
            time.sleep(2)
            coord = askForPlay()
                
            while not (coord in tab.emptyPositions()):
                print('Jogada invalida.')
                coord = askForPlay() 
                
        else:
            time.sleep(2)
            print('O computador joga: ')
            if (k == 0 and flag) or (k == 1 and not flag):
                coord = PCplay.nextPlay(None)
            else:
                coord = PCplay.nextPlay(coord)
                
        tab.setPosition(coord, valor)
        
        if k == 0 and not flag:
            PCplay = jogaGalo(tab)        
                                
        print(tab)
                 
            
        k += 1
            
    return None
