#Versao 1.0
#Autor: Ana Carolina Coscarella
import Dados
import Rodada
import Jogador
__all__ = ["Cria_Novo_Jogo", "Verifica_Rodada", "Atualiza_JogadorAtual"]
jogo=[]

#Descrição: Cria um novo objeto jogo. Retorna 0 se conseguiu criar o objeto Jogo corretamente, caso já tenha objeto Jogo criado, retorna 1.
#Parâmetros: Null
#Retorno: 
#0 - Caso o jogo seja criado corretamente
#1 - Caso já tenha um jogo criado.

def Cria_Novo_Jogo():
    numero_jogo=len(jogo)
    retorno_pega_jogadores=Jogador.Pega_Jogadores()
    if(jogo == []):
        novo_jogo = {numero_jogo+1: {"jogador atual": retorno_pega_jogadores, "dados_atuais": []}}
        jogo.append(novo_jogo)
        return 0
    return 1

#Descrição: Verifica se o número de tentativas já chegou no seu limite. 
#Retorna zero caso o número de tentativas já tenha se esgotado, retorna 1 caso contrário, retorna 2 caso não haja rodada com aquele ID, e retorna 3 caso o ID passado não seja do tipo inteiro. 
#Parâmetros: Recebe o ID da rodada.
#Retorno: 
#0 - Número de tentativas nessa rodada acabou.
#1 - Ainda restam tentativas nessa rodada.
#2 - Não há rodada com esse ID.
#3 - Parâmetro ID passado incorretamente.

def Verifica_Rodada(id):
    retorno_verifica_tentativa=Rodada.Verifica_Tentativa()
    print("TENTATIVAS",retorno_verifica_tentativa)
    print("IDDDD",id)
    if(id not in range(0,26)):
        return 2
    if(type(id)!= int):
        return 3
    if(retorno_verifica_tentativa==0):
        return 0
    if(retorno_verifica_tentativa!=0):
        return 1


#Descrição: Função que recebe a lista dos dois jogadores e o jogador_atual.
#Como são só dois jogadores no jogo, ele simplesmente atualiza o valor jogador_atual para o outro jogador. 
#Parâmetros:
#-Jogadores(A lista de Jogadores do jogo)
#-JogadorAtual(O valor de jogador_atual do objeto jogo)
#Retorno: 
#{0: Jogador_Atual} - Caso tenha sucesso ao atualizar o jogador,retorna dicionário com 0 e o novo jogador da vez
#{1: []} - Caso o parâmetro Jogadores não sejam uma lista de dois jogadores.
#{2: []} - Caso JogadorAtual não seja um objeto Jogador.
#{3: []} - Caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo

def Atualiza_JogadorAtual(jogadorAtual,jogadores):
    retorno_pega_jogadores=Jogador.Pega_Jogadores()
    print(retorno_pega_jogadores)
    if(jogadorAtual == jogadores[0]):
        jogadorAtual=jogadores[1]
        return {0:jogadorAtual}
    if(jogadorAtual == jogadores[0]):
        jogadorAtual=jogadores[1]
        return {0:jogadorAtual}
    if(type(jogadores)!= list and len(jogadores)!=2):
        print("TO AQUI", type(jogadores), len(jogadores), jogadores)
        return {1:[]}
    if(jogadorAtual not in retorno_pega_jogadores):
        return {2:[]}
    if(jogadorAtual not in jogadores):
        return {3:[]}

