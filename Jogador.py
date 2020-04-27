#Versao 1.0.3
#Ultima modificacao: Aiko Ramalho
__all__ = ["Cria_Novo_Jogador", "Pega_Jogadores", "Destroi_Jogadores"]

jogadores = []
#Modulo que diz respeito aos jogadores do Yahtzee.Nele cadastramos e pegamos
#o nome dos jogadores.
#Dentro deste modulo existe uma lista de objetos jogadores.
#A lista pode ter tamanho maximo 2. O objeto jogador tem um dicionario
#com ID(int) e Nome(string),
#exemplo: {01: Aiko}, {02: Carol}, {03: Carlos}.


#Cadastra um jogador do jogo, criando um input e atribui a ele um ID
#e Nome (fornecido no input dentro da funcao)
#retorna 0 caso o jogador tenha sido criado corretamente
#retorna 1 caso ja existam 2 jogadores(limite maximo)
#retorna 3 caso o nome nao tenha sido passado corretamente
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


#Funcao que retorna a lista dos jogadores.
#Retorna um dicionario com um codigo 0 caso sucesso e um objeto jogador caso obtido sucesso
#Retorna com codigo 1 caso falte um jogador a ser cadastrado
#retorna 3 caso faltem dois jogadores para serem cadastrados
def Pega_Jogadores():
    qtdJogadores = len(jogadores)
    if(qtdJogadores == 2):
        return {0: jogadores}
    elif(qtdJogadores == 1):
        return {1: []}
    return {2: []}

#funcao que esvazia a lista de jogadores
#retorna 0 caso sucesso
#retorna 1 caso a lista ja esteja vazia
def Destroi_Jogadores():
    qtdJogadores = len(jogadores)
    if(qtdJogadores == 0):
        return 1
    jogadores.clear()
