#Versao 1.1.0
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
    cont = 0
    contRep = 0
    listaAux = []
    facesDados = []
    facesDadosR = []
    
    for i in dados:
        achado = 0
        k=k+1
        face = i[k]['face']

        #Os simples:
        if face == 1:
            pont = "Ones"
        elif face == 2:
            pont = "Twos"
        elif face == 3:
            pont = "Threes"
        elif face == 4:
            pont = "Fours"
        elif face == 5:
            pont = "Fives"
        elif face == 6:
            pont = "Sixes"

        
        #Para verificar que a lista nao vai ter elemento repetido
        for x in listaPont:
            if pont == x:
                achado = 1           

        #Para verificar que a casa nao esta preenchida
        ver = Verifica_Pont_Preenchida(pont,idJogadorAtual)
        if ver == 1:
            achado = 2
                
        if achado == 0:
            listaPont.append(pont)
            listaAux.append(pont)
        elif achado == 1:
            listaAux.append(pont)
        
        print(face)

    Atribui_Repetidos(listaAux)
    qtdRepetidos = len(repetidos)
    if qtdRepetidos == 1:     #Caso so tenha um repetido
        achado = 0
        for i in repetidos:
            qtdRepeticoes = len(repetidos[i])
            if qtdRepeticoes == 2:
                n = 0
                soma = 0
                for l in dados:
                    n=n+1
                    face = l[n]['face']
                    if (face in facesDadosR) == False:
                        facesDadosR.append(face)
                ordenadosR = sorted(facesDadosR)
                numLista = len(ordenadosR)
                for i in ordenadosR:
                    print("Num: ",i)
                x=1
                while(x<numLista):
                    
                    elemAtual = ordenadosR[x]
                    elemPass = ordenadosR[x-1]
                    sub = elemAtual-elemPass
                    if sub == 1:
                        cont=cont+1
                    print("x: ",x)
                    x=x+1
                if cont == 3:
                    pont = "Small Straight"
            elif qtdRepeticoes == 3:
                pont = "Three of a Kind"
            elif qtdRepeticoes == 4:
                pont = "Four of a Kind"
            elif qtdRepeticoes == 5:
                pont = "Yahtzee"

            #Para verificar que a lista nao vai ter elemento repetido
            for o in listaPont:
                if pont == o:
                    achado = 1
            #Para verificar que a casa nao esta preenchida  
            ver = Verifica_Pont_Preenchida(pont, idJogadorAtual)
            if ver == 1:
                achado = 2
                
            if achado == 0:
                listaPont.append(pont)
                   
    elif qtdRepetidos == 2:     #Caso tenham dois repetidos
        #Unico jeito de dar full house
        for i in repetidos:
            qtdRepeticoes = len(repetidos[i])
            if qtdRepeticoes == 3:
                contRep = contRep + 3
            elif qtdRepeticoes == 2:
                contRep = contRep + 2
        if contRep == 5:
            pont = "Full House"
            
            #Para verificar que a lista nao vai ter elemento repetido
            for x in listaPont:
                if pont == x:
                    achado = 1
            #Para verificar que a casa nao esta preenchida
            ver = Verifica_Pont_Preenchida(pont, idJogadorAtual)
            if ver == 1:
                achado = 2
            
            if achado == 0:
                listaPont.append(pont)
                
    elif qtdRepetidos == 0:     #Caso nao tenha nenhum repetido
        #Unico jeito de dar Large Straight
        #Tambem pode dar Small Straight
        achado = 0
        n=0
        soma=0
        for j in dados:
            n=n+1
            face = j[n]['face']
            facesDados.append(face)
        ordenados = sorted(facesDados)
        numLista = len(ordenados)
        print("NumLista: ",numLista)
        x=1
        while(x<numLista):
            elemAtual = ordenados[x]
            elemPass = ordenados[x-1]
            print("elemAtual: ",elemAtual)
            print("elemPass: ",elemPass)
            sub = elemAtual-elemPass
            print("sub: ",sub)
            if sub == 1:
                cont=cont+1
            if cont == 3:
                pont = "Small Straight"
            elif cont == 4:
                pont = "Large Straight"
            x=x+1
        print("cont: ",cont)
        #Para verificar que a casa nao esta preenchida
        ver = Verifica_Pont_Preenchida(pont, idJogadorAtual)
        if ver == 1:
            achado = 2

        #Para verificar que a lista nao vai ter elemento repetido
        for x in listaPont:
            if pont == x:
                achado = 1
        if achado == 0:
            if pont == "Large Straight":
                ver = Verifica_Pont_Preenchida("Small Straight", idJogadorAtual)
                if ver != 1:
                    if ("Small Straight" in listaPont) == False:
                        listaPont.append("Small Straight")
            listaPont.append(pont)
    
    
    
    return {None}

def Verifica_Pont_Preenchida(tipoPontuacao,idJogadorAtual):
    pontuacao_AUX = Tabuleiro.Pega_PontuacaoAux()
    tabuleiro = Tabuleiro.Pega_Tabuleiro()[0]
    for i in pontuacao_AUX:
        if tipoPontuacao == i:
            linha = pontuacao_AUX[i]
            pontuacao = tabuleiro[linha]
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
x = Dados.Mostra_Dados()
dados = x[0]
Tipo_Pontuacao(dados,1)
for i in listaPont:
    print(i)

