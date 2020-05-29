from Jogador import Cria_Novo_Jogador, Destroi_Jogadores, Pega_Jogadores
from Dados import Cria_Dados, Muda_Status, Mostra_Dados, Destroi_Dados, Jogar_Dados, Muda_Face
from Rodada import Cria_Rodada, Verifica_Tentativa, Atualiza_Tentativas, Modifica_Dados_Rodada, Deleta_Rodadas, Pega_Rodada
from Jogo import Cria_Novo_Jogo, Atualiza_JogadorAtual, Destruir_Jogo
from Pontuacao import Calcula_Pontuacao, Tipo_Pontuacao,Pega_Faces
from Tabuleiro import Cria_Tab, Destruir_Tab, InserirPontuacao, Verifica_Vencedor, Pega_Tabuleiro
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

def formata_saida(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


#pra criarmos um jogo precisamos

#Criar Jogadores
Cria_Novo_Jogador('Aiko')
Cria_Novo_Jogador('Ana')

jog1, jog2 = Pega_Jogadores()[0]
print('jog1 ', jog1)
print('jog2 ', jog2)

#Cria_Rodada
Cria_Rodada()

#Criar Dados
Cria_Dados()

#Criar tabuleiro
Cria_Tab()

#Cria jogo
Cria_Novo_Jogo(jog1)

#modifiquei a funcao joga_dados pra que sempre o primeiro dado dê 1, para poder pontuar em ones
Jogar_Dados()
#atualiza as tentativas (jogou o dado 1 vez, ainda tem 2 restando)
Atualiza_Tentativas(2)
dados = Mostra_Dados()[0]

InserirPontuacao(dados, 1, 'Ones')
#destruo o dados (jog1 ja pontuou)
Destroi_Dados()

#atualizo o jogo para que o jogador_atual seja o jog2
Atualiza_JogadorAtual(jog2)
#Criar Dados dnv
Cria_Dados()
#crio uma nova rodada (hora do segundo jogador jogar)
Cria_Rodada()
#Rodo os dados novamente
Jogar_Dados()
#atualiza as tentativas (jogou o dado 1 vez, ainda tem 2 restando)
Atualiza_Tentativas(2)
dados = Mostra_Dados()[0]
InserirPontuacao(dados, 2, 'Twos')

jogadores = Element('jogadores')
comment = Comment('Dados dos jogadores e suas pontuacoes')
jogadores.append(comment)
jogador = SubElement(jogadores, 'jogador')
id_ = SubElement(jogador, 'id')
id_.text = str(list(jog1.keys())[0])
nome = SubElement(jogador, 'nome')
nome.text = jog1[1]
nome_arquivo = 'jogadores.xml'
with open(nome_arquivo, 'w') as file_object:
	file_object.write(formata_saida(jogadores))

print(Pega_Tabuleiro()[0])
print('dados ', dados)
retorno = Tipo_Pontuacao(dados, 1)
print('tipo pontuacao: ', retorno)
