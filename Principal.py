from Jogador import Cria_Novo_Jogador, Destroi_Jogadores, Pega_Jogadores
from Dados import Cria_Dados, Muda_Status, Mostra_Dados, Destroi_Dados, Jogar_Dados, Muda_Face
from Rodada import Cria_Rodada, Verifica_Tentativa, Atualiza_Tentativas, Modifica_Dados_Rodada, Deleta_Rodadas, Pega_Rodada
from Jogo import Cria_Novo_Jogo, Verifica_Rodada, Atualiza_JogadorAtual, Destruir_Jogo
from Pontuacao import Calcula_Pontuacao, Tipo_Pontuacao,Pega_Faces
from Tabuleiro import Cria_Tab, Destruir_Tab, InserirPontuacao, Verifica_Vencedor, Pega_Tabuleiro
from Principal import Desenha_Tab, Tela_Inicial

#pra criarmos um jogo precisamo

#criar dados
Cria_Dados()
#criar Rodada
Cria_Rodada()
#Criar Jogadores
Cria_Novo_Jogador('Aiko')
Cria_Novo_Jogador('Ana')
#Criar jogo
Cria_Novo_Jogo()
