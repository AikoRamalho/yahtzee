#Versao 1.2.0
#Ultima modificacao: Carlos Ribeiro

from collections import defaultdict
import Dados, Tabuleiro

__all__ = ["Calcula_Pontuacao", "Tipo_Pontuacao"]



#Modulo no qual computamos a pontuacao de cada jogador a partir dos
#dados gerados e fazemos o calculo baseado na sua pontuacao

#Calcula a pontuacao baseada no nome da pontuacao escolhida pelo jogador
#Parametro: dados, nomePontuacao, idJogadorAtual
#retorna {0: pont} Caso tenha sucesso ao calcular a pontuacao
#retorna {1: None} Caso nomePontuacao nao seja string
#retorna {2: None} Caso o nomePontuacao nao esteja presente
#na lista de pontuacoes possiveis
def Calcula_Pontuacao(dados, nomePontuacao, idJogadorAtual):
    listaPont = Tipo_Pontuacao(dados,idJogadorAtual)[0]
    faces = Pega_Faces(dados)
    pont = 0 #pontuacao a ser calculada

    if type(nomePontuacao) != str:
        return {1: None}

    if nomePontuacao in listaPont == False:
        return {2: None}

    
    if nomePontuacao == "Ones":
        for i in faces:
            if i == 1:
                pont = pont + 1 #A cada dado com valor 1, soma-se 1.
    elif nomePontuacao == "Twos":
        for i in faces:
            if i == 2:
                pont = pont + 2 #A cada dado com valor 2, soma-se 2.
    elif nomePontuacao == "Threes":
        for i in faces:
            if i == 3:
                pont = pont + 3 #A cada dado com valor 3, soma-se 3.
    elif nomePontuacao == "Fours":
        for i in faces:
            if i == 4:
                pont = pont + 4 #A cada dado com valor 4, soma-se 4.
    elif nomePontuacao == "Five":
        for i in faces:
            if i == 5:
                pont = pont + 5 #A cada dado com valor 5, soma-se 5.
    elif nomePontuacao == "Sixes":
        for i in faces:
            if i == 6:
                pont = pont + 6 #A cada dado com valor 6, soma-se 6.
    elif nomePontuacao == "Three of a Kind":
        for i in faces:
            pont = pont + i #Caso 3 dados tenham valores iguais, soma-se todos os dados.
    elif nomePontuacao == "Four of a Kind":
        for i in faces:
            pont = pont + i #Caso 4 dados tenham valores iguais, soma-se todos os dados.
    elif nomePontuacao == "Full House":
        pont = 25 #Caso 3 dados tenham valores iguais e os outros 2 tenham outros valores iguais, pontua 25.
    elif nomePontuacao == "Small Straight":
        pont = 30 #Caso 4 dados formem um sequencia numerica, pontua 30.
    elif nomePontuacao == "Large Straight":
        pont = 40 #Caso 5 dados formem uma sequencia numerica, pontua 40.
    elif nomePontuacao == "Chance":
        for i in faces:
            pont = pont + i #Pode se usar a qualquer momento, soma-se todos os dados.
    elif nomePontuacao == "Yahtzee":
        pont = 50 #Caso 6 dados tenham valores iguais, pontua 50.   
    
    return {0: pont}

#Pelos dados gerados, diz que tipo de pontuacao pode ser feita
#Parametros: dados, idJogadorAtual
#retorna {0: listaPont} Caso tenha sucesso ao dizer que tipo de pontuacao
#pode ser feita, retorna um dicionario com 0 e uma lista de pontuacoes
#possiveis
#retorna {1: []} - Caso o Dado nao seja um objeto Dado.
#retorna {2: []} - Caso idJogadorAtual nao seja um int.
#retorna {3: []} - Caso o parametro idJogadorAtual nao corresponda
#com nenhum dos jogadores presentes no jogo
def Tipo_Pontuacao(dados, idJogadorAtual):
    k=0
    pont = ""
    cont = 0
    contRep = 0
    listaAux = []
    facesDados = []
    facesDadosR = []
    listaPont = []
    repetidos = {}

    if Dados.Mostra_Dados()[0] != dados:
        return {1: []}
    if type(idJogadorAtual) != int:
        return {2: []}
    if idJogadorAtual != 1 and idJogadorAtual != 2:
        return {3: []}
    
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
        elif achado == 1:   #Para poder verificar os repetidos
            listaAux.append(pont)
        
        #print(face)

    Atribui_Repetidos(listaAux,repetidos)
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
                #for i in ordenadosR:
                    #print("Num: ",i)
                x=1
                while(x<numLista):
                    
                    elemAtual = ordenadosR[x]
                    elemPass = ordenadosR[x-1]
                    sub = elemAtual-elemPass
                    if sub == 1:
                        cont=cont+1
                    #print("x: ",x)
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
        achado = 0
        #Unico jeito de dar full house
        for i in repetidos:
            qtdRepeticoes = len(repetidos[i])
            if qtdRepeticoes == 3:
                contRep = contRep + 3
            elif qtdRepeticoes == 2:
                contRep = contRep + 2
        if contRep == 5:
            pont = "Full House"

            #Um full house tbm pode conter um three of a kind
            #Para verificar que a lista nao vai ter elemento repetido
            for x in listaPont:
                if x == "Three of a Kind":
                    achado = 3

            ver = Verifica_Pont_Preenchida("Three of a Kind", idJogadorAtual)
            if ver == 1:
                achado = 4

            if achado == 0:
                listaPont.append("Three of a Kind")

            achado = 0
            
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
        #print("NumLista: ",numLista)
        x=1
        while(x<numLista):
            elemAtual = ordenados[x]
            elemPass = ordenados[x-1]
            #print("elemAtual: ",elemAtual)
            #print("elemPass: ",elemPass)
            sub = elemAtual-elemPass
            #print("sub: ",sub)
            if sub == 1:
                cont=cont+1
            if cont == 1 and sub == 2:
                break
            if cont == 3:
                pont = "Small Straight"
            elif cont == 4:
                pont = "Large Straight"
            x=x+1
        #print("cont: ",cont)
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
            
    #Para verificar que a casa nao esta preenchida
    #Chance sera sempre uma jogada possivel, a nao ser que ja esteja preenchida
    ver = Verifica_Pont_Preenchida("Chance",idJogadorAtual)
    if ver == 0:
        listaPont.append("Chance")

    #for j in listaPont:
    #    print(j)
    
    return {0: listaPont}

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

def Atribui_Repetidos(lista, repetidos):

    keys = defaultdict(list)
    for key,value in enumerate(lista):
        keys[value].append(key)

    for value in keys:
        if len(keys[value])>1:
            repetidos[value] = keys[value]

    return 0

def Pega_Faces(dados):
    listFaces = []
    k=0
    for i in dados:
        k=k+1
        listFaces.append(i[k]['face'])

    return listFaces

Dados.Cria_Dados()
Tabuleiro.Cria_Tab()
Dados.Jogar_Dados()
Dados.Muda_Face(1,1)
Dados.Muda_Face(2,1)
Dados.Muda_Face(3,1)
Dados.Muda_Face(4,2)
Dados.Muda_Face(5,2)
x = Dados.Mostra_Dados()
dados = x[0]
listaPont=Tipo_Pontuacao(dados,1)[0]
for i in listaPont:
    print(i)
#Calcula_Pontuacao(dados,"Three of a Kind", 1)

