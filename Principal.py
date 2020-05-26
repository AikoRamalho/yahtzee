from tkinter import *
from PIL import ImageTk,Image
import Tabuleiro,Pontuacao,Dados,Jogador,Rodada

__all__ = ["Tela_Inicial", "Desenha_Tab"]

root = Tk()
root.title("Principal")
root.config(bg="green")

imgDado1 = ImageTk.PhotoImage(Image.open("C:/Users/carlo/Desktop/ProgMod/Tkinter(GUI)/imagens/dados/Dice-1.png"))
imgDado2 = ImageTk.PhotoImage(Image.open("C:/Users/carlo/Desktop/ProgMod/Tkinter(GUI)/imagens/dados/Dice-2E.png"))
imgDado3 = ImageTk.PhotoImage(Image.open("C:/Users/carlo/Desktop/ProgMod/Tkinter(GUI)/imagens/dados/Dice-3E.png"))
imgDado4 = ImageTk.PhotoImage(Image.open("C:/Users/carlo/Desktop/ProgMod/Tkinter(GUI)/imagens/dados/Dice-4.png"))
imgDado5 = ImageTk.PhotoImage(Image.open("C:/Users/carlo/Desktop/ProgMod/Tkinter(GUI)/imagens/dados/Dice-5.png"))
imgDado6 = ImageTk.PhotoImage(Image.open("C:/Users/carlo/Desktop/ProgMod/Tkinter(GUI)/imagens/dados/Dice-6E.png"))

button_Ones = Button(root, text="Ones",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Twos = Button(root, text="Twos",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Threes = Button(root, text="Threes",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Fours = Button(root, text="Fours",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Fives = Button(root, text="Fives",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Sixes = Button(root, text="Sixes",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)

def Tela_Inicial():
    

    
    return {None}

def Insere(dados,nomePontuacao,idJogador):
    global button_Ones
    global button_Twos
    global button_Threes
    global button_Fours
    global button_Fives
    global button_Sixes
    pontuacao_atual = Pontuacao.Calcula_Pontuacao(dados,nomePontuacao, idJogador)[0]
    Tabuleiro.InserirPontuacao(pontuacao_atual, idJogador, nomePontuacao)
    i=1

    #Para nao aparecer novamente disponivel apos insercao de pontuacao
    button_Ones.grid_forget()
    button_Ones = Button(root, text="Ones",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Ones.grid(row=2,column=0,sticky=W+E)

    button_Twos.grid_forget()
    button_Twos = Button(root, text="Twos",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Twos.grid(row=3,column=0,sticky=W+E)

    button_Threes.grid_forget()
    button_Threes = Button(root, text="Threes",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Threes.grid(row=4,column=0,sticky=W+E)

    button_Fours.grid_forget()
    button_Fours = Button(root, text="Fours",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fours.grid(row=5,column=0,sticky=W+E)

    button_Fives.grid_forget()
    button_Fives = Button(root, text="Fives",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fives.grid(row=6,column=0,sticky=W+E)

    button_Sixes.grid_forget()
    button_Sixes = Button(root, text="Sixes",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Sixes.grid(row=7,column=0,sticky=W+E)

    if idJogador == 1:
        idJogador = 2
    elif idJogador == 2:
        idJogador = 1
    
    Desenha_Tab(dados,idJogador)
    
    for dado in dados: #loop para mudar o status dos dados congelados apos insercao de pontuacao
        if dado[i]["congelado"] == True:
            Dados.Muda_Status(i)
        i=i+1

    

    return

def Pontuacoes_Disponiveis(dados,idJogadorAtual):
    global button_Ones
    global button_Twos
    global button_Threes
    global button_Fours
    global button_Fives
    global button_Sixes
    listaPont = Pontuacao.Tipo_Pontuacao(dados,idJogadorAtual)[0]
    
    #Para nao aparecer novamente caso nao escolha nenhuma pontuacao
    button_Ones.grid_forget()
    button_Ones = Button(root, text="Ones",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Ones.grid(row=2,column=0,sticky=W+E)

    button_Twos.grid_forget()
    button_Twos = Button(root, text="Twos",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Twos.grid(row=3,column=0,sticky=W+E)

    button_Threes.grid_forget()
    button_Threes = Button(root, text="Threes",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Threes.grid(row=4,column=0,sticky=W+E)

    button_Fours.grid_forget()
    button_Fours = Button(root, text="Fours",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fours.grid(row=5,column=0,sticky=W+E)

    button_Fives.grid_forget()
    button_Fives = Button(root, text="Fives",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fives.grid(row=6,column=0,sticky=W+E)

    button_Sixes.grid_forget()
    button_Sixes = Button(root, text="Sixes",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Sixes.grid(row=7,column=0,sticky=W+E)

        #i[idJogadorAtual-1]
        #print(i[idJogadorAtual-1])
    
    if tabuleiro[0][idJogadorAtual-1] == None:
        button_Ones = Button(root, text="Ones",padx = 20,pady =10, command=lambda: Insere(dados,"Ones",idJogadorAtual))
        button_Ones.grid(row=2,column=0,sticky=W+E)
    if tabuleiro[1][idJogadorAtual-1] == None:
        button_Twos = Button(root, text="Twos",padx = 20,pady =10, command=lambda: Insere(dados,"Twos",idJogadorAtual))
        button_Twos.grid(row=3,column=0,sticky=W+E)
    if tabuleiro[2][idJogadorAtual-1] == None:
        button_Threes = Button(root, text="Threes",padx = 20,pady =10, command=lambda: Insere(dados,"Threes",idJogadorAtual))
        button_Threes.grid(row=4,column=0,sticky=W+E)
    if tabuleiro[3][idJogadorAtual-1] == None:
        button_Fours = Button(root, text="Fours",padx = 20,pady =10, command=lambda: Insere(dados,"Fours",idJogadorAtual))
        button_Fours.grid(row=5,column=0,sticky=W+E)
    if tabuleiro[4][idJogadorAtual-1] == None:
        button_Fives = Button(root, text="Fives",padx = 20,pady =10, command=lambda: Insere(dados,"Fives",idJogadorAtual))
        button_Fives.grid(row=6,column=0,sticky=W+E)
    if tabuleiro[5][idJogadorAtual-1] == None:
        button_Sixes = Button(root, text="Sixes",padx = 20,pady =10, command=lambda: Insere(dados,"Sixes",idJogadorAtual))
        button_Sixes.grid(row=7,column=0,sticky=W+E)

    return

def Desenha_Dados(dados,idJogadorAtual):
    global button_Ones
    global button_Twos
    global button_Threes
    global button_Fours
    global button_Fives
    global button_Sixes
    Dados.Jogar_Dados()
    dados = Dados.Mostra_Dados()[0]
    Pontuacoes_Disponiveis(dados,idJogadorAtual)
    listaFaces = Pontuacao.Pega_Faces(dados)

    if listaFaces[0] == 1:
        button_Dado1 = Button(root,image = imgDado1,command=lambda: Dados.Muda_Status(1))
    elif listaFaces[0] == 2:
        button_Dado1 = Button(root,image = imgDado2,command=lambda: Dados.Muda_Status(1))
    elif listaFaces[0] == 3:
        button_Dado1 = Button(root,image = imgDado3,command=lambda: Dados.Muda_Status(1))
    elif listaFaces[0] == 4:
        button_Dado1 = Button(root,image = imgDado4,command=lambda: Dados.Muda_Status(1))
    elif listaFaces[0] == 5:
        button_Dado1 = Button(root,image = imgDado5,command=lambda: Dados.Muda_Status(1))
    elif listaFaces[0] == 6:
        button_Dado1 = Button(root,image = imgDado6,command=lambda: Dados.Muda_Status(1))

    if listaFaces[1] == 1:
        button_Dado2 = Button(root,image = imgDado1,command=lambda: Dados.Muda_Status(2))
    elif listaFaces[1] == 2:
        button_Dado2 = Button(root,image = imgDado2,command=lambda: Dados.Muda_Status(2))
    elif listaFaces[1] == 3:
        button_Dado2 = Button(root,image = imgDado3,command=lambda: Dados.Muda_Status(2))
    elif listaFaces[1] == 4:
        button_Dado2 = Button(root,image = imgDado4,command=lambda: Dados.Muda_Status(2))
    elif listaFaces[1] == 5:
        button_Dado2 = Button(root,image = imgDado5,command=lambda: Dados.Muda_Status(2))
    elif listaFaces[1] == 6:
        button_Dado2 = Button(root,image = imgDado6,command=lambda: Dados.Muda_Status(2))

    if listaFaces[2] == 1:
        button_Dado3 = Button(root,image = imgDado1,command=lambda: Dados.Muda_Status(3))
    elif listaFaces[2] == 2:
        button_Dado3 = Button(root,image = imgDado2,command=lambda: Dados.Muda_Status(3))
    elif listaFaces[2] == 3:
        button_Dado3 = Button(root,image = imgDado3,command=lambda: Dados.Muda_Status(3))
    elif listaFaces[2] == 4:
        button_Dado3 = Button(root,image = imgDado4,command=lambda: Dados.Muda_Status(3))
    elif listaFaces[2] == 5:
        button_Dado3 = Button(root,image = imgDado5,command=lambda: Dados.Muda_Status(3))
    elif listaFaces[2] == 6:
        button_Dado3 = Button(root,image = imgDado6,command=lambda: Dados.Muda_Status(3))

    if listaFaces[3] == 1:
        button_Dado4 = Button(root,image = imgDado1,command=lambda: Dados.Muda_Status(4))
    elif listaFaces[3] == 2:
        button_Dado4 = Button(root,image = imgDado2,command=lambda: Dados.Muda_Status(4))
    elif listaFaces[3] == 3:
        button_Dado4 = Button(root,image = imgDado3,command=lambda: Dados.Muda_Status(4))
    elif listaFaces[3] == 4:
        button_Dado4 = Button(root,image = imgDado4,command=lambda: Dados.Muda_Status(4))
    elif listaFaces[3] == 5:
        button_Dado4 = Button(root,image = imgDado5,command=lambda: Dados.Muda_Status(4))
    elif listaFaces[3] == 6:
        button_Dado4 = Button(root,image = imgDado6,command=lambda: Dados.Muda_Status(4))

    if listaFaces[4] == 1:
        button_Dado5 = Button(root,image = imgDado1,command=lambda: Dados.Muda_Status(5))
    elif listaFaces[4] == 2:
        button_Dado5 = Button(root,image = imgDado2,command=lambda: Dados.Muda_Status(5))
    elif listaFaces[4] == 3:
        button_Dado5 = Button(root,image = imgDado3,command=lambda: Dados.Muda_Status(5))
    elif listaFaces[4] == 4:
        button_Dado5 = Button(root,image = imgDado4,command=lambda: Dados.Muda_Status(5))
    elif listaFaces[4] == 5:
        button_Dado5 = Button(root,image = imgDado5,command=lambda: Dados.Muda_Status(5))
    elif listaFaces[4] == 6:
        button_Dado5 = Button(root,image = imgDado6,command=lambda: Dados.Muda_Status(5))
        
    button_Dado1.grid(row=8,column=0,columnspan=2,sticky=W)
    button_Dado2.grid(row=8,column=0,columnspan=2,sticky=N)
    button_Dado3.grid(row=8,column=1,columnspan=2,sticky=W)
    button_Dado4.grid(row=8,column=1,columnspan=2,sticky=N)
    button_Dado5.grid(row=8,column=2,sticky=E)

    #Desenha_Tab(dados)

    return

def Desenha_Tab(dados,idJogadorAtual):
    #pontuacao_atual = Pontuacao.Calcula_Pontuacao(dados,nomePontuacao, idJogadorAtual)[0]
    jogadores = Jogador.Pega_Jogadores()[0]    

    button_JogarDados = Button(root, text="Jogar Dados",padx = 60,pady =10, command=lambda: Desenha_Dados(dados,idJogadorAtual))

    jogador1 = jogadores[0][1]
    jogador2 = jogadores[1][2]
    
    labelJogador1 = Label(root,text=jogador1,bg = "gray")
    labelJogador2 = Label(root,text=jogador2,bg = "gray")

    pontuacao = tabuleiro[0][0]
    label_Ones1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[0][1]
    label_Ones2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[1][0]
    label_Twos1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[1][1]
    label_Twos2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[2][0]
    label_Threes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[2][1]
    label_Threes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[3][0]
    label_Fours1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[3][1]
    label_Fours2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[4][0]
    label_Fives1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[4][1]
    label_Fives2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[5][0]
    label_Sixes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[5][1]
    label_Sixes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")

    labelJogador1.grid(row=1,column=1)
    labelJogador2.grid(row=1,column=2)

    button_Ones.grid(row=2,column=0,sticky=W+E)
    label_Ones1.grid(row=2,column=1,sticky=N+S+E+W)
    label_Ones2.grid(row=2,column=2,sticky=N+S+E+W)

    button_Twos.grid(row=3,column=0,sticky=W+E)
    label_Twos1.grid(row=3,column=1,sticky=N+S+E+W)
    label_Twos2.grid(row=3,column=2,sticky=N+S+E+W)

    button_Threes.grid(row=4,column=0,sticky=W+E)
    label_Threes1.grid(row=4,column=1,sticky=N+S+E+W)
    label_Threes2.grid(row=4,column=2,sticky=N+S+E+W)

    button_Fours.grid(row=5,column=0,sticky=W+E)
    label_Fours1.grid(row=5,column=1,sticky=N+S+E+W)
    label_Fours2.grid(row=5,column=2,sticky=N+S+E+W)

    button_Fives.grid(row=6,column=0,sticky=W+E)
    label_Fives1.grid(row=6,column=1,sticky=N+S+E+W)
    label_Fives2.grid(row=6,column=2,sticky=N+S+E+W)

    button_Sixes.grid(row=7,column=0,sticky=W+E)
    label_Sixes1.grid(row=7,column=1,sticky=N+S+E+W)
    label_Sixes2.grid(row=7,column=2,sticky=N+S+E+W)

    #Desenha_Dados(dados)

    button_JogarDados.grid(row=9,column=0,columnspan=3)
    
    return {None}

Rodada.Cria_Rodada()
Tabuleiro.Cria_Tab()
Dados.Cria_Dados()
Jogador.Cria_Novo_Jogador("Aiko")
Jogador.Cria_Novo_Jogador("Carol")
Dados.Jogar_Dados()
tabuleiro = Tabuleiro.Pega_Tabuleiro()[0]
for i in tabuleiro:
    print(i)
dados = Dados.Mostra_Dados()[0]
for i in dados:
    print(i)
listaPont=Pontuacao.Tipo_Pontuacao(dados,1)[0]
for i in listaPont:
    print(i)
Desenha_Tab(dados,1)

root.mainloop()

