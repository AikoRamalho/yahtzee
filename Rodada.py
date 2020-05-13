#Versao 1.0.7
#Ultimo modificacao: Aiko Ramalho
import Dados

MAX_RODADAS = 26 #define o numero maximo de rodadas (numero padrao de um jogo yahtzee)

__all__ = ["Cria_Rodada", "Verifica_Tentativa", "Atualiza_Tentativas", "Modifica_Dados_Rodada", "Deleta_Rodadas", "Pega_Rodada"]

rodadas = []

#funcao responsavel por criar o objeto rodada com 3 tentativas e dar append nele na lista
#Parametros: None
#retorna 0 no sucesso
#retorna 1 caso numero de rodadas maxima tenha sido atingida
#retorna 2 caso os dados da rodada anterior n tenham sido deletados
def Cria_Rodada():
    numero_rodada = len(rodadas)
    retorno_mostra_dados = Dados.Mostra_Dados()
    if(numero_rodada > MAX_RODADAS):
        return 1
    if(list(retorno_mostra_dados.values())[0] == []):
        nova_rodada = {numero_rodada+1: {"tentativas": 3, "dados_rodada": []}}
        rodadas.append(nova_rodada)
        return 0
    return 2

#funcao responsavel por verificar se ainda restam tentativas na ultima rodada criada
#retorna 0 caso tenham tentativas
#retorna 1 caso nao tenham tentativas
#retorna 2 caso nao tenham rodadas
def Verifica_Tentativa():
    numero_rodada = len(rodadas)
    if(numero_rodada == 0):
        return 2
    num_tentativas = rodadas[numero_rodada-1][numero_rodada]["tentativas"]
    if(num_tentativas == 0):
        return 1
    return 0

#funcao responsavel por atualizar o numero de tentativas da ultima rodada
#retorna 0 caso sucesso
#retorn 1 caso o numero de tentativas do parametro n seja num_tentativas-1 ou zero
#retorna 2 caso o numero passado n esteja no range de tentativas
#retorn 3 caso o numero passado n seja int
#retorna 4 caso nao tenham rodadas
def Atualiza_Tentativas(num):
    numero_rodada = len(rodadas)
    if(type(num) != type(0)):
        return 3
    if(num not in range(0, 4)): #range no python eh aberto no extremo da direita
        return 2
    if(numero_rodada == 0):
        return 4
    num_tentativas = rodadas[numero_rodada-1][numero_rodada]["tentativas"]
    if(num != 0 and num != num_tentativas-1):
        return 1
    rodadas[numero_rodada-1][numero_rodada]["tentativas"] = num
    return 0

#funcao responsavel por atualizar os dados da ultima rodada
#retorna 0 caso sucesso
#retorn 1 caso nao restam tentativas na rodada
#retorna 2 caso todos os dados estejam congelados
#retorn 3 caso nao hajam dados
#retorna 4 caso nao tenham rodadas
def Modifica_Dados_Rodada():
    numero_rodada = len(rodadas)
    if(numero_rodada == 0):
        return 4
    num_tentativas = rodadas[numero_rodada-1][numero_rodada]["tentativas"]
    if(num_tentativas == 0): 
        return 1
    retorno_dados = Dados.Jogar_Dados()
    if(retorno_dados == 1):
        return 3
    if(retorno_dados == 2):
        return 2
    dados = Dados.Mostra_Dados()
    rodadas[numero_rodada-1][numero_rodada]["dados_rodada"] = list(dados.values())[0]
    return 0

#funcao que esvazia a lista de rodadas
#Parametros: None
#retorna 0 caso sucesso
#retorna 1 caso a lista ja esteja vazia
def Deleta_Rodadas():
    qtdRodadas = len(rodadas)
    if(qtdRodadas == 0):
        return 1
    rodadas.clear()
    return 0

#funcao que retorna a ultima rodada
#retorna {1: None} caso nao hajam rodadsa
#retorna {0: Rodada} caso haja rodada
def Pega_Rodada():
    numero_rodada = len(rodadas)
    if(numero_rodada == 0):
        return {1: None}
    return{0: rodadas[numero_rodada-1]}