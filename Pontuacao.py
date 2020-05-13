#Versao 1.0.0
#Ultima modificacao: Carlos Ribeiro

from collections import defaultdict
import Dados, Tabuleiro

__all__ = ["Calcula_Pontuacao", "Tipo_Pontuacao"]

listaPont = []
repetidos = {}

#Modulo no qual computamos a pontuacao de cada jogador a partir dos
#dados gerados e fazemos o calculo baseado na sua pontuacao

#Calcula a pontuacao de cada jogador para no final mostrar quem ganhou
#Parametro: None
#retorna 
def Calcula_Pontuacao():
    return {None}

#Pelos dados gerados, diz que tipo de pontuacao pode ser feita
#Parametros: dados, idJogadorAtual
#retorna {0: listaPont} Caso tenha sucesso ao dizer que tipo de pontuacao
#pode ser feita, retorna um dicionario com 0 e uma lista de pontuacoes
#possiveis
#retorna {1: []} - Caso o Dado nao seja um objeto Dado.
#retorna {2: []} - Caso JogadorAtual nao seja um objeto Jogador.
#retorna {3: []} - Caso de erro ao mostrar os tipos de pontuacao
#retorna {4: []} - Caso o parametro jogadorAtual nao corresponda
#com nenhum dos jogadores presentes no jogo
def Tipo_Pontuacao(dados, idJogadorAtual):
    k=0
    pont = ""
    achado = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    listaAux = []
    
    for i in dados:
        k=k+1
        face = i[k]['face']
        
        if face == 1:
            cont1 = cont1 + 1
            pont = "Ones"
        elif face == 2:
            cont2 = cont2 + 1
            pont = "Twos"
        elif face == 3:
            cont3 = cont3 + 1
            pont = "Threes"
        elif face == 4:
            cont4 = cont4 + 1
            pont = "Fours"
        elif face == 5:
            cont5 = cont5 + 1
            pont = "Fives"
        elif face == 6:
            cont6 = cont6 + 1
            pont = "Sixes"

        #for x in listaPont:
        #    if pont == x:
        #        achado = 1

        #if cont1 == 3:
            
        
        ver = Verifica_Pont_Preenchida(pont,idJogadorAtual)
        if ver == 1:
            achado = 2
                
        if achado == 0:
            listaAux.append(pont)
        
        print(face)

    Atribui_Repetidos(listaAux)
    
    if len(repetidos)> 0:
        for i in repetidos:
            if len(repetidos[i]) == 3:

    
    
    return {None}

def Verifica_Pont_Preenchida(tipoPontuacao,idJogadorAtual):

    for i in Tabuleiro.pontuacaoAux:
        if tipoPontuacao == i:
            linha = Tabuleiro.pontuacaoAux[i]
            pontuacao = Tabuleiro.tabuleiro[linha]
            if pontuacao[idJogadorAtual] != None:
                return 1 #Pontuacao Preenchida
        
    return 0

def Atribui_Repetidos(lista):

    keys = defaultdict(list)
    for key,value in enumerate(lista):
        keys[value].append(key)

    for value in keys:
        if len(keys[value])>1:
            repetidos[value] = keys[value]

    return 0


Dados.Cria_Dados()
Tabuleiro.Cria_Tab()
Dados.Jogar_Dados()

Tipo_Pontuacao(Dados.dados,1)

