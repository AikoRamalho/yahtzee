__all__ = ["Cria_Novo_Jogador", "Pega_Jogadores", "Destroi_Jogadores"]

jogadores = []

def Cria_Novo_Jogador(name):
    qtdJogadores = len(jogadores)
    if(qtdJogadores == 2):
        return 1
    if(name != None):
        nomeJogador = name
    else:
        nomeJogador = input('insira o nome do jogador: ')
    if(len(nomeJogador) == 0):
        return 2
    novoJogador = {qtdJogadores+1: nomeJogador}
    jogadores.append(novoJogador)
    return 0

def Pega_Jogadores():
    qtdJogadores = len(jogadores)
    if(qtdJogadores == 2):
        return {0: jogadores}
    elif(qtdJogadores == 1):
        return {1: []}
    return {2: []}

def Destroi_Jogadores():
    qtdJogadores = len(jogadores)
    if(qtdJogadores == 0):
        return 1
    jogadores.clear()
