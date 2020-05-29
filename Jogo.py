#Versao 1.5
#Autor: Ana Carolina Coscarella
#Ultima modificacao: Aiko Ramalho
import Dados
import Rodada
import Jogador
__all__ = ["Cria_Novo_Jogo",  "Atualiza_JogadorAtual"]

jogo = []

#Descrição: Cria um novo objeto jogo. Retorna 0 se conseguiu criar o objeto Jogo corretamente, caso já tenha objeto Jogo criado, retorna 1.
#Parâmetros: jogador - obj jogador
#Retorno: 
#0 - Caso o jogo seja criado corretamente
#1 - Caso já tenha um jogo criado.

def Cria_Novo_Jogo(Jogador):
    jogo.append({"jogador_atual": Jogador})
    return 0

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

def Atualiza_JogadorAtual(NovoJogadorAtual):
    jogo.clear()
    jogo.append({"jogador_atual": NovoJogadorAtual})
    return 0

#funcao que destroi o modulo jogo
#retorna 0 caso sucesso
#retorna 1 caso jogo nao exista
def Destruir_Jogo():
    if(len(jogo)==0):
        return 1
    jogo.clear()
    return 0
