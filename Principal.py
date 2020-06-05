from tkinter import *
from PIL import ImageTk,Image
import Tabuleiro,Pontuacao,Dados,Jogador,Rodada

__all__ = ["Tela_Inicial", "Desenha_Tab"]

root = Tk()
root.title("Principal")
root.config(bg="green")

imgDado1 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-1.png"))
imgDado2 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-2E.png"))
imgDado3 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-3E.png"))
imgDado4 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-4.png"))
imgDado5 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-5.png"))
imgDado6 = ImageTk.PhotoImage(Image.open("Assets/dados/Dice-6E.png"))

button_Ones = Button(root, text="Ones",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Twos = Button(root, text="Twos",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Threes = Button(root, text="Threes",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Fours = Button(root, text="Fours",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Fives = Button(root, text="Fives",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Sixes = Button(root, text="Sixes",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_FullHouse = Button(root, text="Full House",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_SmallStraight = Button(root, text="Small Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_LargeStraight = Button(root, text="Large Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Chance = Button(root, text="Chance",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
button_Yahtzee = Button(root, text="Yahtzee",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)


def Tela_Inicial():
    

    
    return {None}

def Insere(dados,nomePontuacao,idJogador):
    global button_Ones
    global button_Twos
    global button_Threes
    global button_Fours
    global button_Fives
    global button_Sixes
    global button_ThreeOfAKind
    global button_FourOfAKind
    global button_FullHouse
    global button_SmallStraight
    global button_LargeStraight
    global button_Chance
    global button_Yahtzee
    pontuacao_atual = Pontuacao.Calcula_Pontuacao(dados,nomePontuacao, idJogador)[0]
    Tabuleiro.InserirPontuacao(pontuacao_atual, idJogador, nomePontuacao)
    i=1

    #Para nao aparecer novamente disponivel apos insercao de pontuacao
    button_Ones.grid_forget()
    button_Ones = Button(root, text="Ones",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Ones.grid(row=2,column=0,sticky=W+E)

    button_Twos.grid_forget()
    button_Twos = Button(root, text="Twos",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Twos.grid(row=3,column=0,sticky=W+E)

    button_Threes.grid_forget()
    button_Threes = Button(root, text="Threes",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Threes.grid(row=4,column=0,sticky=W+E)

    button_Fours.grid_forget()
    button_Fours = Button(root, text="Fours",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fours.grid(row=5,column=0,sticky=W+E)

    button_Fives.grid_forget()
    button_Fives = Button(root, text="Fives",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fives.grid(row=6,column=0,sticky=W+E)

    button_Sixes.grid_forget()
    button_Sixes = Button(root, text="Sixes",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Sixes.grid(row=7,column=0,sticky=W+E)

    button_ThreeOfAKind.grid_forget()
    button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    
    button_FourOfAKind.grid_forget()
    button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_FourOfAKind.grid(row=9,column=0,sticky=W+E)

    button_FullHouse.grid_forget()
    button_FullHouse = Button(root, text="Full House",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_FullHouse.grid(row=10,column=0,sticky=W+E)

    button_SmallStraight.grid_forget()
    button_SmallStraight = Button(root, text="Small Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_SmallStraight.grid(row=11,column=0,sticky=W+E)

    button_LargeStraight.grid_forget()
    button_LargeStraight = Button(root, text="Large Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_LargeStraight.grid(row=12,column=0,sticky=W+E)

    button_Chance.grid_forget()
    button_Chance = Button(root, text="Chance",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Chance.grid(row=13,column=0,sticky=W+E)

    button_Yahtzee.grid_forget()
    button_Yahtzee = Button(root, text="Yahtzee",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Yahtzee.grid(row=14,column=0,sticky=W+E)

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
    global button_ThreeOfAKind
    global button_FourOfAKind
    global button_FullHouse
    global button_SmallStraight
    global button_LargeStraight
    global button_Chance
    global button_Yahtzee
    listaPont = Pontuacao.Tipo_Pontuacao(dados,idJogadorAtual)[0]
    
    #Para nao aparecer novamente caso nao escolha nenhuma pontuacao
    button_Ones.grid_forget()
    button_Ones = Button(root, text="Ones",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Ones.grid(row=2,column=0,sticky=W+E)

    button_Twos.grid_forget()
    button_Twos = Button(root, text="Twos",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Twos.grid(row=3,column=0,sticky=W+E)

    button_Threes.grid_forget()
    button_Threes = Button(root, text="Threes",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Threes.grid(row=4,column=0,sticky=W+E)

    button_Fours.grid_forget()
    button_Fours = Button(root, text="Fours",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fours.grid(row=5,column=0,sticky=W+E)

    button_Fives.grid_forget()
    button_Fives = Button(root, text="Fives",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Fives.grid(row=6,column=0,sticky=W+E)

    button_Sixes.grid_forget()
    button_Sixes = Button(root, text="Sixes",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Sixes.grid(row=7,column=0,sticky=W+E)

    button_ThreeOfAKind.grid_forget()
    button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    
    button_FourOfAKind.grid_forget()
    button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_FourOfAKind.grid(row=9,column=0,sticky=W+E)

    button_FullHouse.grid_forget()
    button_FullHouse = Button(root, text="Full House",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_FullHouse.grid(row=10,column=0,sticky=W+E)

    button_SmallStraight.grid_forget()
    button_SmallStraight = Button(root, text="Small Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_SmallStraight.grid(row=11,column=0,sticky=W+E)

    button_LargeStraight.grid_forget()
    button_LargeStraight = Button(root, text="Large Straight",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_LargeStraight.grid(row=12,column=0,sticky=W+E)

    button_Chance.grid_forget()
    button_Chance = Button(root, text="Chance",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Chance.grid(row=13,column=0,sticky=W+E)

    button_Yahtzee.grid_forget()
    button_Yahtzee = Button(root, text="Yahtzee",bg="green",disabledforeground="black",padx = 20,pady =10, command=Tabuleiro.InserirPontuacao, state=DISABLED)
    button_Yahtzee.grid(row=14,column=0,sticky=W+E)

        #i[idJogadorAtual-1]
        #print(i[idJogadorAtual-1])
    
    if tabuleiro[0][idJogadorAtual-1] == None:
        button_Ones = Button(root, text="Ones",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Ones",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Ones", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Ones1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Ones1.grid(row=2,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Ones2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Ones2.grid(row=2,column=2,sticky=N+S+E+W)
        
        button_Ones.grid(row=2,column=0,sticky=W+E)
    if tabuleiro[1][idJogadorAtual-1] == None:
        button_Twos = Button(root, text="Twos",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Twos",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Twos", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Twos1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Twos1.grid(row=3,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Twos2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Twos2.grid(row=3,column=2,sticky=N+S+E+W)
        
        button_Twos.grid(row=3,column=0,sticky=W+E)
    if tabuleiro[2][idJogadorAtual-1] == None:
        button_Threes = Button(root, text="Threes",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Threes",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Threes", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Threes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Threes1.grid(row=4,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Threes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Threes2.grid(row=4,column=2,sticky=N+S+E+W)
        
        button_Threes.grid(row=4,column=0,sticky=W+E)
    if tabuleiro[3][idJogadorAtual-1] == None:
        button_Fours = Button(root, text="Fours",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Fours",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Fours", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Fours1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fours1.grid(row=5,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Fours2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fours2.grid(row=5,column=2,sticky=N+S+E+W)
        
        button_Fours.grid(row=5,column=0,sticky=W+E)
    if tabuleiro[4][idJogadorAtual-1] == None:
        button_Fives = Button(root, text="Fives",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Fives",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Fives", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Fives1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fives1.grid(row=6,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Fives2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Fives2.grid(row=6,column=2,sticky=N+S+E+W)
        
        button_Fives.grid(row=6,column=0,sticky=W+E)
    if tabuleiro[5][idJogadorAtual-1] == None:
        button_Sixes = Button(root, text="Sixes",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Sixes",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Sixes", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Sixes1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Sixes1.grid(row=7,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Sixes2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Sixes2.grid(row=7,column=2,sticky=N+S+E+W)
        
        button_Sixes.grid(row=7,column=0,sticky=W+E)
    if tabuleiro[6][idJogadorAtual-1] == None:
        button_ThreeOfAKind = Button(root, text="Three of a Kind",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Three of a Kind",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Three of a Kind", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_ThreeOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_ThreeOfAKind1.grid(row=8,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_ThreeOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_ThreeOfAKind2.grid(row=8,column=2,sticky=N+S+E+W)
        
        button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    if tabuleiro[7][idJogadorAtual-1] == None:
        button_FourOfAKind = Button(root, text="Four of a Kind",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Four of a Kind",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Four of a Kind", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_FourOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FourOfAKind1.grid(row=9,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_FourOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FourOfAKind2.grid(row=9,column=2,sticky=N+S+E+W)
        
        button_FourOfAKind.grid(row=9,column=0,sticky=W+E)
    if tabuleiro[8][idJogadorAtual-1] == None:
        button_FullHouse = Button(root, text="Full House",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Full House",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Full House", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_FullHouse1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FullHouse1.grid(row=10,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_FullHouse2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_FullHouse2.grid(row=10,column=2,sticky=N+S+E+W)
        
        button_FullHouse.grid(row=10,column=0,sticky=W+E)
    if tabuleiro[9][idJogadorAtual-1] == None:
        button_SmallStraight = Button(root, text="Small Straight",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Small Straight",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Small Straight", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_SmallStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_SmallStraight1.grid(row=11,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_SmallStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_SmallStraight2.grid(row=11,column=2,sticky=N+S+E+W)
        
        button_SmallStraight.grid(row=11,column=0,sticky=W+E)   
    if tabuleiro[10][idJogadorAtual-1] == None:
        button_LargeStraight = Button(root, text="Large Straight",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Large Straight",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Large Straight", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_LargeStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_LargeStraight1.grid(row=12,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_LargeStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_LargeStraight2.grid(row=12,column=2,sticky=N+S+E+W)
        
        button_LargeStraight.grid(row=12,column=0,sticky=W+E)
    if tabuleiro[11][idJogadorAtual-1] == None:
        button_Chance = Button(root, text="Chance",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Chance",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Chance", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Chance1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Chance1.grid(row=13,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Chance2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Chance2.grid(row=13,column=2,sticky=N+S+E+W)
        
        button_Chance.grid(row=13,column=0,sticky=W+E)
    if tabuleiro[12][idJogadorAtual-1] == None:
        button_Yahtzee = Button(root, text="Yahtzee",bg="green",fg="white",padx = 20,pady =10, command=lambda: Insere(dados,"Yahtzee",idJogadorAtual))

        pontuacao = Pontuacao.Calcula_Pontuacao(dados,"Yahtzee", idJogadorAtual)[0]
        if idJogadorAtual == 1:
            label_Yahtzee1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Yahtzee1.grid(row=14,column=1,sticky=N+S+E+W)
        elif idJogadorAtual == 2:
            label_Yahtzee2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white",fg="red")
            label_Yahtzee2.grid(row=14,column=2,sticky=N+S+E+W)
        
        button_Yahtzee.grid(row=14,column=0,sticky=W+E)
    return


def Dado_clicado(dados,butao,numDado):
    
    if dados[numDado-1][numDado]['congelado'] == False: 
        butao['bg'] = 'gray'
    else:
        butao['bg'] = 'green'


    Dados.Muda_Status(numDado)

    return

def Desenha_Dados(dados,idJogadorAtual):
    global button_Ones
    global button_Twos
    global button_Threes
    global button_Fours
    global button_Fives
    global button_Sixes
    global button_ThreeOfAKind
    global button_FourOfAKind
    global button_FullHouse
    global button_SmallStraight
    global button_LargeStraight
    global button_Chance
    global button_Yahtzee
    Dados.Jogar_Dados()
    dados = Dados.Mostra_Dados()[0]
    Pontuacoes_Disponiveis(dados,idJogadorAtual)
    listaFaces = Pontuacao.Pega_Faces(dados)

    if listaFaces[0] == 1:
        button_Dado1 = Button(root,image = imgDado1,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado1,1))
    elif listaFaces[0] == 2:
        button_Dado1 = Button(root,image = imgDado2,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado1,1))
    elif listaFaces[0] == 3:
        button_Dado1 = Button(root,image = imgDado3,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado1,1))
    elif listaFaces[0] == 4:
        button_Dado1 = Button(root,image = imgDado4,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado1,1))
    elif listaFaces[0] == 5:
        button_Dado1 = Button(root,image = imgDado5,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado1,1))
    elif listaFaces[0] == 6:
        button_Dado1 = Button(root,image = imgDado6,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado1,1))

    if listaFaces[1] == 1:
        button_Dado2 = Button(root,image = imgDado1,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado2,2))
    elif listaFaces[1] == 2:
        button_Dado2 = Button(root,image = imgDado2,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado2,2))
    elif listaFaces[1] == 3:
        button_Dado2 = Button(root,image = imgDado3,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado2,2))
    elif listaFaces[1] == 4:
        button_Dado2 = Button(root,image = imgDado4,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado2,2))
    elif listaFaces[1] == 5:
        button_Dado2 = Button(root,image = imgDado5,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado2,2))
    elif listaFaces[1] == 6:
        button_Dado2 = Button(root,image = imgDado6,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado2,2))

    if listaFaces[2] == 1:
        button_Dado3 = Button(root,image = imgDado1,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado3,3))
    elif listaFaces[2] == 2:
        button_Dado3 = Button(root,image = imgDado2,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado3,3))
    elif listaFaces[2] == 3:
        button_Dado3 = Button(root,image = imgDado3,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado3,3))
    elif listaFaces[2] == 4:
        button_Dado3 = Button(root,image = imgDado4,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado3,3))
    elif listaFaces[2] == 5:
        button_Dado3 = Button(root,image = imgDado5,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado3,3))
    elif listaFaces[2] == 6:
        button_Dado3 = Button(root,image = imgDado6,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado3,3))

    if listaFaces[3] == 1:
        button_Dado4 = Button(root,image = imgDado1,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado4,4))
    elif listaFaces[3] == 2:
        button_Dado4 = Button(root,image = imgDado2,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado4,4))
    elif listaFaces[3] == 3:
        button_Dado4 = Button(root,image = imgDado3,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado4,4))
    elif listaFaces[3] == 4:
        button_Dado4 = Button(root,image = imgDado4,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado4,4))
    elif listaFaces[3] == 5:
        button_Dado4 = Button(root,image = imgDado5,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado4,4))
    elif listaFaces[3] == 6:
        button_Dado4 = Button(root,image = imgDado6,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado4,4))

    if listaFaces[4] == 1:
        button_Dado5 = Button(root,image = imgDado1,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado5,5))
    elif listaFaces[4] == 2:
        button_Dado5 = Button(root,image = imgDado2,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado5,5))
    elif listaFaces[4] == 3:
        button_Dado5 = Button(root,image = imgDado3,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado5,5))
    elif listaFaces[4] == 4:
        button_Dado5 = Button(root,image = imgDado4,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado5,5))
    elif listaFaces[4] == 5:
        button_Dado5 = Button(root,image = imgDado5,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado5,5))
    elif listaFaces[4] == 6:
        button_Dado5 = Button(root,image = imgDado6,bg = 'green',activebackground='red',command=lambda: Dado_clicado(dados,button_Dado5,5))
        
    button_Dado1.grid(row=16,column=0,columnspan=2,sticky=W)
    button_Dado2.grid(row=16,column=0,columnspan=2,sticky=N)
    button_Dado3.grid(row=16,column=1,columnspan=2,sticky=W)
    button_Dado4.grid(row=16,column=1,columnspan=2,sticky=N)
    button_Dado5.grid(row=16,column=2,sticky=E)

    #Desenha_Tab(dados)

    return

def Desenha_Tab(dados,idJogadorAtual):
    #pontuacao_atual = Pontuacao.Calcula_Pontuacao(dados,nomePontuacao, idJogadorAtual)[0]
    jogadores = Jogador.Pega_Jogadores()[0]    

    button_JogarDados = Button(root, text="Jogar Dados",padx = 60,pady =10, command=lambda: Desenha_Dados(dados,idJogadorAtual))

    jogador1 = jogadores[0][1]
    jogador2 = jogadores[1][2]

    labelJogador1 = Label(root,text=jogador1, bg = "green",fg="white")
    labelJogador2 = Label(root,text=jogador2, bg = "green",fg="white")

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
    pontuacao = tabuleiro[6][0]
    label_ThreeOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[6][1]
    label_ThreeOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[7][0]
    label_FourOfAKind1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[7][1]
    label_FourOfAKind2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[8][0]
    label_FullHouse1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[8][1]
    label_FullHouse2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[9][0]
    label_SmallStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[9][1]
    label_SmallStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[10][0]
    label_LargeStraight1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[10][1]
    label_LargeStraight2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[11][0]
    label_Chance1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[11][1]
    label_Chance2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[12][0]
    label_Yahtzee1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[12][1]
    label_Yahtzee2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")

    label_Total = Label(root, text="Total",bg="green",fg="black",relief="raised",padx = 20,pady =10)
    
    pontuacao = tabuleiro[13][0]
    label_Total1 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    pontuacao = tabuleiro[13][1]
    label_Total2 = Label(root, text=pontuacao,borderwidth=2,relief="groove",padx=20,pady=10, bg = "white")
    
    labelJogador1.grid(row=1,column=1)
    labelJogador2.grid(row=1,column=2)

    labelJogador1.configure(font="Arial 12 bold")
    labelJogador2.configure(font="Arial 12 bold")

    if idJogadorAtual == 1:
        labelJogador1.configure(font="Arial 12 bold underline")
    elif idJogadorAtual == 2:
        labelJogador2.configure(font="Arial 12 bold underline")

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

    button_ThreeOfAKind.grid(row=8,column=0,sticky=W+E)
    label_ThreeOfAKind1.grid(row=8,column=1,sticky=N+S+E+W)
    label_ThreeOfAKind2.grid(row=8,column=2,sticky=N+S+E+W)

    button_FourOfAKind.grid(row=9,column=0,sticky=W+E)
    label_FourOfAKind1.grid(row=9,column=1,sticky=N+S+E+W)
    label_FourOfAKind2.grid(row=9,column=2,sticky=N+S+E+W)

    button_FullHouse.grid(row=10,column=0,sticky=W+E)
    label_FullHouse1.grid(row=10,column=1,sticky=N+S+E+W)
    label_FullHouse2.grid(row=10,column=2,sticky=N+S+E+W)

    button_SmallStraight.grid(row=11,column=0,sticky=W+E)
    label_SmallStraight1.grid(row=11,column=1,sticky=N+S+E+W)
    label_SmallStraight2.grid(row=11,column=2,sticky=N+S+E+W)

    button_LargeStraight.grid(row=12,column=0,sticky=W+E)
    label_LargeStraight1.grid(row=12,column=1,sticky=N+S+E+W)
    label_LargeStraight2.grid(row=12,column=2,sticky=N+S+E+W)

    button_Chance.grid(row=13,column=0,sticky=W+E)
    label_Chance1.grid(row=13,column=1,sticky=N+S+E+W)
    label_Chance2.grid(row=13,column=2,sticky=N+S+E+W)

    button_Yahtzee.grid(row=14,column=0,sticky=W+E)
    label_Yahtzee1.grid(row=14,column=1,sticky=N+S+E+W)
    label_Yahtzee2.grid(row=14,column=2,sticky=N+S+E+W)

    label_Total.grid(row=15,column=0,sticky=W+E)
    label_Total1.grid(row=15,column=1,sticky=W+E)
    label_Total2.grid(row=15,column=2,sticky=W+E)

    #Desenha_Dados(dados)

    button_JogarDados.grid(row=17,column=0,columnspan=3,sticky=W+E)
    
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

