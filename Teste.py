#Versao 1.6.0
#Ultima modificacao: Carlos Ribeiro

import unittest
from Jogador import Cria_Novo_Jogador, Destroi_Jogadores, Pega_Jogadores
from Dados import Cria_Dados, Muda_Status, Mostra_Dados, Destroi_Dados, Jogar_Dados
from Rodada import Cria_Rodada, Verifica_Tentativa, Atualiza_Tentativas, Modifica_Dados_Rodada, Deleta_Rodadas, Pega_Rodada
from Jogo import Cria_Novo_Jogo, Verifica_Rodada, Atualiza_JogadorAtual
from Pontuacao import Calcula_Pontuacao, Tipo_Pontuacao
from Tabuleiro import Cria_Tab, Destruir_Tab, InserirPontuacao, Verifica_Vencedor
from Principal import Desenha_Tab, Tela_Inicial

class Teste_ModuloJogador_CriaNovoJogador(unittest.TestCase):
    #Parametro:
        #nomeJogador - Um nome para o jogador passado como String
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Lista Jogadores ja esta preenchida
        #2 - Nome do jogador foi passado incorretamente

    #cria jogador ok -> retorno esperado: 0
    def testJogador_01_CriaNovoJogador_Ok_Condicao_Retorno(self):
        print("Caso de Teste Jogador 01 - Criar jogador com sucesso")
        Destroi_Jogadores()
        retorno_esperado = Cria_Novo_Jogador('aiko')
        self.assertEqual(retorno_esperado, 0)
        
    #cria jogador ja existem 2 jogadores no jogo -> retorno esperado: 1
    def testJogador_02_CriaNovoJogador_Ja_Existem_Jogadores(self): 
        print("Caso de Teste Jogador 02 - Ja existem dois jogadores cadastrados")
        Destroi_Jogadores()
        Cria_Novo_Jogador('aiko')
        Cria_Novo_Jogador('carlos')
        retorno_esperado = Cria_Novo_Jogador('aha')
        self.assertEqual(retorno_esperado, 1)

    #nome do jogador passado incorretamente -> retorno esperado: 2
    def testJogador_03_CriaNovoJogador_Nome_Passado_Incorretamente(self): 
        print("Caso de Teste Jogador 03 - Nome passado incorretamente")
        Destroi_Jogadores()
        retorno_esperado = Cria_Novo_Jogador('')
        self.assertEqual(retorno_esperado, 2)

class Teste_ModuloJogador_DestroiJogadores(unittest.TestCase):
    #Parametro:
        #None
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Lista de jogadores ja esta vazia

    #destroi jogador ok -> retorno esperado: 0
    def testJogador_04_DestroiJogadores_Ok_Condicao_Retorno(self):
        print("Caso de Teste Jogador 04 - Jogadores destruidos com sucesso")
        Cria_Novo_Jogador('aiko')
        retorno_esperado = Destroi_Jogadores()
        self.assertEqual(retorno_esperado, 0)
        
    #Lista de jogadores ja esta vazia -> retorno esperado: 1
    def testJogador_05_DestroiJogadores_ListaJaVazia(self): 
        print("Caso de Teste Jogador 05 - Lista Jogadores ja vazia")
        retorno_esperado = Destroi_Jogadores()
        self.assertEqual(retorno_esperado, 1)

class Teste_ModuloJogador_PegaJogador(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis:
        #{0: jogadores} - Sucesso
        #{1: []} - Falta um jogador para ser cadastrado
        #{2: []} - Faltam dois jogadores para serem cadastrados

    #pega jogador caso sucesso
    def testJogador_06_PegarJogadores_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogador 06 - Pegar jogadores com sucesso")
        Destroi_Jogadores()
        Cria_Novo_Jogador('aiko')
        Cria_Novo_Jogador('carol')
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{0:[{1: "aiko"}, {2: "carol"}]})

    #pega jogador caso falta um jogador p ser cadastrado
    def testJogador_07_PegarJogadores_Falta_Um_Jogador(self): 
        print("Caso de Teste Jogador 07 - Falta um jogador para ser cadastrado")
        Destroi_Jogadores()
        Cria_Novo_Jogador('eu')
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{1:[]})
        
    #pega jogador caso faltam dois jogadores p serem cadastrados
    def testJogador_08_PegarJogadores_Faltam_Dois_Jogadores(self): 
        print("Caso de Teste Jogador 08 - Faltam dois jogadores para serem cadastrados")
        Destroi_Jogadores()
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{2:[]})

class Teste_ModuloDados_CriaDados(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0,1
        #0 - Sucesso
        #1 - Ja existem dados criados (Tentativa de recriacao)

    #cria dados com sucesso
    def testDados_01_CriaDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 01 - Criar dados com sucesso")
        Destroi_Dados()
        retorno_esperado = Cria_Dados()
        self.assertEqual(retorno_esperado,0)

    #cria dados ja existem dados criados
    def testDados_02_CriaDados_Ja_Existem_Dados_Criados(self): 
        print("Caso de Teste Dados 02 - Ja existem dados criados")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Cria_Dados()
        self.assertEqual(retorno_esperado,1)

class Teste_ModuloDados_Destroi_Dados(unittest.TestCase):
    #Parametro:
        #None
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Lista de dados ja esta vazia

    #destroi dados ok -> retorno esperado: 0
    def testDados_03_DestroiDados_Ok_Condicao_Retorno(self):
        print("Caso de Teste Dados 03 - Dados destruidos com sucesso")
        Cria_Dados()
        retorno_esperado = Destroi_Dados()
        self.assertEqual(retorno_esperado, 0)
        
    #Lista de dados ja esta vazia -> retorno esperado: 1
    def testDados_04_DestroiDados_ListaJaVazia(self): 
        print("Caso de Teste dados 04 - Lista dados ja vazia")
        retorno_esperado = Destroi_Dados()
        self.assertEqual(retorno_esperado, 1)

class Teste_ModuloDados_MudaStatus(unittest.TestCase):
    #Parametro: id
        #id - ID de um dado especifico
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Nao existe dado com esse id
        #2 - Id passado nao corresponde ao tipo int
        #3 - Nao existem dados criados

    #muda status ok
    def testDados_05_MudaStatus_Ok_Condicao_Retorno_1(self): 
        print("Caso de Teste Dados 05 - Mudanca de estado do dado 1 com sucesso")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status(1)
        self.assertEqual(retorno_esperado,0)
        
    #muda status id passado incoerente (id > 6)
    def testDados_06_MudaStatus_Nao_Existe_Dado(self): 
        print("Caso de Teste Dados 06 - Esse ID nao tem dado correspondente")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status(7)
        self.assertEqual(retorno_esperado,1)

    #muda status type(id) != int
    def testDados_07_MudaStatus_Nao_Ser_Int(self): 
        print("Caso de Teste Dados 07 - Parametro passado nao corresponde ao tipo 'int'")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status("1")
        self.assertEqual(retorno_esperado,2)

    #muda status nao existe dados criados
    def testDados_08_MudaStatus_Lista_Vazia(self): 
        print("Caso de Teste Dados 08 - Lista de dados nao existente")
        Destroi_Dados()
        retorno_esperado = Muda_Status(1)
        self.assertEqual(retorno_esperado,3)

class Teste_ModuloDados_JogarDados(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0, 1, 2
        #0 - Sucesso
        #1 - Nao existem dados
        #2 - Todos os dados estao congelados

    #jogar dados ok
    def testDados_09_JogarDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 09 - Jogada feita com sucesso")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Jogar_Dados()
        self.assertEqual(retorno_esperado,0)

    #jogar dados quando nao existem dados
    def testDados_10_JogarDados_Dados_Nao_Existentes(self): 
        print("Caso de Teste Dados 10 - Dados nao existentes")
        Destroi_Dados()
        retorno_esperado = Jogar_Dados()
        self.assertEqual(retorno_esperado,1)

    #todos os dados estao congelados
    def testDados_11_JogarDados_Todos_Dados_Congelados(self): 
        print("Caso de Teste Dados 11 - Todos os dados estao congelados")
        Destroi_Dados()
        Cria_Dados()
        #Mudar o status de todos para ficarem "congelado": True
        Muda_Status(1)
        Muda_Status(2)
        Muda_Status(3)
        Muda_Status(4)
        Muda_Status(5)
        retorno_esperado = Jogar_Dados()
        self.assertEqual(retorno_esperado,2)

class Teste_ModuloDados_MostraDados(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: {0: dados}, {1: []}, {2: []}
        #{0: [ Dado, Dado, Dado, Dado, Dado ]} - Sucesso
        #{1: []} - Nao existem dados (nao foram criados)
        #{2: []} - Os dados nao foram jogados (chave face com valor zero)
        
    #mostra dados caso sucesso
    def testDados_12_MostraDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 12 - Dados foram mostrados com sucesso")
        Destroi_Dados()
        Cria_Dados()
        Jogar_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(list(retorno_esperado.keys())[0], 0)

    #mostradados nao existem dados criados
    def testDados_13_MostraDados_Dados_Nao_Existentes(self): 
        print("Caso de Teste Dados 13 - Dados nao existentes")
        Destroi_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(retorno_esperado,{1: []})

    #mostradados os dados ainda nao foram jogados
    def testDados_14_MostraDados_Dados_Nao_Jogados(self): 
        print("Caso de Teste Dados 14 - Dados nao foram jogados")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(retorno_esperado,{2: []})

class Teste_ModuloRodada_CriaRodada(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0, 1
        #0 - Sucesso
        #1 - Numero maximo de rodadas ja foi atingido
        
    #cria rodada caso sucesso    
    def testRodada_01_CriaRodada_Ok_Condicao_Retorno(self):
        print("Caso de Teste Rodada 01 - Criar dados com sucesso")
        Deleta_Rodadas()
        Destroi_Dados()
        retorno_esperado = Cria_Rodada()
        self.assertEqual(retorno_esperado,0)
        
    #cria rodada numero maximo de rodadas ja atingido
    def testRodada_02_CriaRodada_Numero_Maximo_Atingido(self): 
        print("Caso de Teste Rodada 02 - O Numero de rodadas do jogo ja foi atingido")
        Deleta_Rodadas()
        Destroi_Dados()
        for _ in range(27):
            Cria_Rodada()
        retorno_esperado = Cria_Rodada()
        self.assertEqual(retorno_esperado,1)

class Teste_ModuloRodada_DeletaRodada(unittest.TestCase):
    #Parametro:
        #None
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Lista de rodada ja esta vazia

    #deleta rodada ok -> retorno esperado: 0
    def testRodada_03_DeletaRodada_Ok_Condicao_Retorno(self):
        print("Caso de Teste Rodada 03 - Rodadas esvaziadas com sucesso")
        Cria_Rodada()
        retorno_esperado = Deleta_Rodadas()
        self.assertEqual(retorno_esperado, 0)
        
    #Lista de rodada ja esta vazia -> retorno esperado: 1
    def testRodada_04_DeletaRodada_ListaJaVazia(self): 
        print("Caso de Teste rodada 04 - Lista Rodadas ja vazia")
        retorno_esperado = Deleta_Rodadas()
        self.assertEqual(retorno_esperado, 1)

class Teste_ModuloRodada_VerificaTentativa(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0, 1, 2
        #0 - Sucesso
        #1 - Nao existe tentativa disponivel
        #2 - Nao existe rodada criada
        
    #Inicio teste para verificar tentativa com sucesso    
    def testRodada_05_Verifica_Tentativa_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 05 - Ainda existe tentativa disponivel")
        Deleta_Rodadas()
        Destroi_Dados()
        Cria_Rodada()
        retorno_esperado = Verifica_Tentativa()
        self.assertEqual(retorno_esperado,0)
        
    #Inicio teste para verificar tentativa caso nao existam tentativas disponiveis
    def testRodada_06_Verifica_Tentativa_Nao_Existem_Tentativas(self): 
        print("Caso de Teste Rodada 06 -Nao existe tentativa disponivel")
        Deleta_Rodadas()
        Destroi_Dados()
        Cria_Rodada()
        Atualiza_Tentativas(0)
        retorno_esperado = Verifica_Tentativa()
        self.assertEqual(retorno_esperado,1)
        
    #Inicio teste para verificar tentativa caso nao exista rodada criada
    def testRodada_07_Verifica_Tentativa_Nao_Existe_Rodada(self): 
        print("Caso de Teste Rodada 07 - Nao existe rodada criada")
        Deleta_Rodadas()
        retorno_esperado = Verifica_Tentativa()
        self.assertEqual(retorno_esperado,2)

class Teste_ModuloRodada_Atualiza_Tentativa(unittest.TestCase):
    #Parametro: Num
        #Num - Numero de tentativas que quer se colocar naquela rodada
    #Retornos possiveis: 0, 1, 2, 3, 4
        #0 - Sucesso
        #1 - Numero inconsistente
        #2 - numero de tentativas diferente de tentativas -1 da rodada atual
        #3 - Numero nao condiz com o range aceito (maior que a enesima tentativa atual)
        #4 - Nao existe rodada criada
        
    #Inicio teste para atualizar tentativa com sucesso
    def testRodada_08_Atualiza_Tentativa_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 08 - Suceso, tentativa atualizada")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Atualiza_Tentativas(2)
        self.assertEqual(retorno_esperado,0)

    #Inicio teste para atualizar tentativa caso o numero seja inconsistente        
    def testRodada_09_Atualiza_Tentativa_Numero_Inconsistente_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 09 - Numero inconsistente")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Atualiza_Tentativas(3)
        self.assertEqual(retorno_esperado,1)

    #Inicio teste para atualizar tentativa caso o numero de tentativas do parametro seja diferente de tentativas -1 do ultimo objeto    
    def testRodada_10_Atualiza_Tentativa_NTentativas_Diferente(self): 
        print("Caso de Teste Rodada 10 - O numero de tentativas no paramentro eh diferente de tentativas -1 do ultimo objeto")
        Deleta_Rodadas()
        retorno_esperado = Atualiza_Tentativas(10)
        self.assertEqual(retorno_esperado,2)

    #Inicio teste para atualizar tentativa caso o parametro nao seja aceito
    def testRodada_11_Atualiza_Tentativa_Parametro_NaoAceito(self): 
        print("Caso de Teste Rodada 11 - Tentativa no parametro nao condiz com o range aceito")
        Deleta_Rodadas()
        retorno_esperado = Atualiza_Tentativas("1")
        self.assertEqual(retorno_esperado,3)

    #Inicio teste para atualizar tentativa caso nao exista rodada criada
    def testRodada_12_Atualiza_Tentativa_Nao_Existe_RodadaCriada(self): 
        print("Caso de Teste Rodada 12 -Nao existe rodada criada")
        Deleta_Rodadas()
        retorno_esperado = Atualiza_Tentativas(2)
        self.assertEqual(retorno_esperado,4)

class Teste_ModuloRodada_ModificaDadosRodada(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0, 1, 2, 3, 4
        #0 - Sucesso
        #1 - Nao tem tentativas sobrando
        #2 - Os dados estao congelados
        #3 - Nao existem dados
        #4 - Nao existe rodada criada

    #Inicio teste para modificar a rodada com sucesso    
    def testRodada_13_ModificaDadosRodada_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 13 - Sucesso, objeto rodada atualizado")
        Deleta_Rodadas()
        Destroi_Dados()
        Cria_Dados()
        Cria_Rodada()
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,0)

    #Inicio teste para modificar a rodada caso nao tenham tentativas sobrando
    def testRodada_14_ModificaDadosRodada_Sem_Tentativas_Sobrando(self): 
        print("Caso de Teste Rodada 14 -Nao tem tentivas sobrando")
        Deleta_Rodadas()
        Cria_Rodada()
        Atualiza_Tentativas(0)
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,1)

    #Inicio teste para modificar a rodada caso os dados estejam congelados    
    def testRodada_15_ModificaDadosRodada_Dados_Congelados(self): 
        print("Caso de Teste Rodada 15 -Dados estao Congelados")
        Deleta_Rodadas()
        Cria_Rodada()
        Cria_Dados()
        Muda_Status(1)
        Muda_Status(2)
        Muda_Status(3)
        Muda_Status(4)
        Muda_Status(5)
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,2)
        
    #Inicio teste para modificar a rodada caso nao existam dados    
    def testRodada_16_ModificaDadosRodada_Nao_Existe_Dado(self): 
        print("Caso de Teste Rodada 16 -Nao existem dados")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,3)
        
    #Inicio teste para modificar a rodada caso nao exista rodada    
    def testRodada_17_ModificaDadosRodada_Nao_Existe_Rodada(self): 
        print("Caso de Teste Rodada 17 - Nao existe rodada criada")
        Deleta_Rodadas()
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,4)

class Teste_ModuloRodada_PegaRodada(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis:
        #{0: rodadas[numero_rodada-1]} - Sucesso
        #{1: None} - Lista de Rodadas esta vazia

    #Inicio teste para pegar rodada com sucesso    
    def testRodada_18_PegaRodada_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 18 - Sucesso")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Pega_Rodada()
        self.assertEqual(retorno_esperado,{0: { 1: {"tentativas":3 ,"dados_rodada": []} }})

    #Inicio teste para pegar rodada caso a lista de Rodadas esteja vazia    
    def testRodada_19_PegaRodada_Lista_Rodadas_Vazia(self): 
        print("Caso de Teste Rodada 19 - Lista de Rodadas Vazia")
        Deleta_Rodadas()
        retorno_esperado = Pega_Rodada()
        self.assertEqual(retorno_esperado,{1:None})

class Teste_ModuloJogo_CriaNovoJogo(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0,1
        #0 - Sucesso
        #1 - Jogo ja criado

    #Inicio teste para criar novo jogo com sucesso
    def testJogo_01_CriaNovoJogo_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogo 01 - Jogo novo criado com sucesso")
        retorno_esperado = Cria_Novo_Jogo()
        self.assertEqual(retorno_esperado,0)

    #Inicio teste para criar novo jogo caso ja haja um jogo criado
    def testJogo_02_CriaNovoJogo_Jogo_Ja_Criado(self): 
        print("Caso de Teste Jogo 02 - Jogo ja criado")
        retorno_esperado = Cria_Novo_Jogo()
        self.assertEqual(retorno_esperado,1)

class Teste_ModuloJogo_VerificaRodada(unittest.TestCase):
    #Parametro: ID
        #ID - Id da rodada
    #Retornos possiveis: 0,1,2,3
        #0 - Sucesso
        #1 - Ainda restam tentativas
        #2 - Id nao coerente com o numero de rodadas do jogo
        #3 - Id passado incorretamente

    #Inicio teste para verificar rodada com sucesso                     
    def testJogo_03_VerificaRodadaJogo_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogo 03 - Rodada Verificada corretamente")
        Atualiza_Tentativas(0)                
        retorno_esperado = Verifica_Rodada(1)
        self.assertEqual(retorno_esperado,0)

    #Inicio teste para verificar rodada caso restem tentativas
    def testJogo_04_VerificaRodada_Ainda_Restam_Tentativas(self): 
        print("Caso de Teste Jogo 04 - Ainda Restam Tentativas")
        Cria_Rodada()         
        retorno_esperado = Verifica_Rodada(2) 
        self.assertEqual(retorno_esperado,1)
        
    #Inicio teste para verificar rodada caso o id passado nao corresponda aos ids disponiveis                   
    def testJogo_05_VerificaRodadaJogo_Nao_Tem_O_ID(self): 
        print("Caso de Teste Jogo 05 - Id nao coerente com o numero de rodadas do jogo")   
        retorno_esperado = Verifica_Rodada(200) 
        self.assertEqual(retorno_esperado,2)

    #Inicio teste para verificar rodada caso o id tenha sido passado incorretamente
    def testJogo_06_VerificaRodadaJogo_ID_Passado_Incorretamente(self): 
        print("Caso de Teste Jogo 06 - ID passado incorretamente")   
        retorno_esperado = Verifica_Rodada("1") 
        self.assertEqual(retorno_esperado,3)

class Teste_ModuloJogo_Atualiza_JogadorAtual(unittest.TestCase):
    #Parametros:
        #Jogadores - A lista de Jogadores do jogo
        #JogadorAtual - O valor de jogador_atual do objeto jogo
    #Retornos possiveis:
        #{0: Jogador_Atual} - Sucesso
        #{1: []} - Caso o parametro Jogadores nao sejam uma lista de dois jogadores.
        #{2: []} - Caso JogadorAtual nao seja um objeto Jogador.
        #{3: []} - Caso o parametro jogadorAtual nao corresponda com nenhum dos jogadores presentes no jogo

    #Inicio teste para atualizar jogador atual com sucesso
    def testJogo_07_AtualizaJogadorAtual_O_Condicao_Retorno(self):
        print("Caso de Teste Jogo 07 - Sucesso ao atualizar o jogador")
        jogadorAtual = {1: "Aiko"}
        jogadores = [{1: "Aiko"}, {2: "Carol"}]
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores) #Considerando que comeca com o Aiko
        self.assertEqual(retorno_esperado,{0: {2: "Carol"}})

    #Inicio teste para atualizar jogador atual caso o parametro Jogadores nao sejam uma lista de dois jogadores
    def testJogo_08_AtualizaJogadorAtual_Jogadores_Nao_Passado_Corretamente(self): 
        print("Caso de Teste Jogo 08 - Jogadores nao passado corretamente")
        jogadorAtual = {2: "Carol"}
        jogadores = "nao lista"                 
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores)
        self.assertEqual(retorno_esperado,{1: []})

    #Inicio teste para atualizar jogador atual caso JogadorAtual nao seja um objeto Jogador    
    def testJogo_09_AtualizaJogadorAtual_JogadorAtual_Nao_Passado_Corretamente(self): 
        print("Caso de Teste Jogo 09 - JogadorAtual nao eh um objeto Jogador")
        jogadorAtual = "nao Jogador"
        jogadores = [{1: "Aiko"}, {2: "Carol"}]             
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores)
        self.assertEqual(retorno_esperado,{2: []})
        
    #Inicio teste para atualizar jogador atual caso o parametro jogadorAtual nao corresponda com nenhum dos jogadores presentes no jogo
    def testJogo_10_AtualizaJogadorAtual_JogadorAtual_Nao_Faz_Parte_De_Jogadores(self): 
        print("Caso de Teste Jogo 10 - JogadorAtual nao faz parte da lista Jogadores")
        jogadorAtual = {3: "Carlos"}
        jogadores = [{1: "Aiko"}, {2: "Carol"}]             
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores)
        self.assertEqual(retorno_esperado,{3: []})

class Teste_ModuloPontuacao_CalculaPontuacao(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: {0: PontosJogador}, {1: []}
        #{0: Jogador_Atual} - Sucesso
        #{1: []} - Caso as casas da coluna nao esteja devidamente preenchidas
        
    #Inicio teste para calcular pontuacao com sucesso 
    def testPontuacao_01_CalculaPontuacao_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Pontuacao 01 - Pontuacao calculada com sucesso")
        retorno_esperado = Calcula_Pontuacao()
        self.assertEqual(retorno_esperado,{0: pontosJogador})#Nao sei como passar pontosJogador
        
    #Inicio teste para calcular pontuacao caso as casas da coluna nao estejam devidamente preenchidas                     
    def testPontuacao_02_CalculaPontuacao_Colunas_Nao_Preenchidas(self): 
        print("Caso de Teste Pontuacao 02 - Casas da coluna nao estao devidamente preenchidas")
        #Nao sei como fazer para dar esse erro
        retorno_esperado = Calcula_Pontuacao()
        self.assertEqual(retorno_esperado,{1: []})

class Teste_ModuloPontuacao_TipoPontuacao(unittest.TestCase):
    #Parametro: Dados, JogadorAtual
        #Dados - Os dados gerados pelo jogador
        #JogadorAtual - O Jogador Atual
    #Retornos possiveis
        #{0: Jogador_Atual} - Sucesso
        #{1: []} - Caso o Dado nao seja um objeto Dado
        #{2: []} - Caso JogadorAtual nao seja um objeto Jogador
        #{3: []} - Caso de erro ao mostrar os tipos de pontuacao
        #{4: []} - Caso o parametro jogadorAtual nao corresponda com nenhum dos jogadores presentes no jogo

    #Inicio teste para tipo da pontuacao com sucesso
    def testPontuacao_03_TipoPontuacao_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Pontuacao 03 - Sucesso ao dizer que tipo de pontuacao pode ser feita")
        Dados = Jogar_Dados()
        JogadorAtual = {2: "Carol"}
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{0: ListaPontuacao})
        
    #Inicio teste para tipo da pontuacao caso o Dado nao seja um objeto Dado
    def testPontuacao_04_TipoPontuacao_Dado_Nao_Seja_Objeto_Dado(self): 
        print("Caso de Teste Pontuacao 04 - Dado nao eh um objeto Dado")
        Destroi_Dados()
        JogadorAtual = {2: "Carol"}
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{1: []})
    
    #Inicio teste para tipo da pontuacao caso JogadorAtual nao seja um objeto Jogador    
    def testPontuacao_05_TipoPontuacao_JogadorAtual_Nao_Seja_Objeto_Jogador(self): 
        print("Caso de Teste Pontuacao 05 - Dado nao eh um objeto Dado")
        Dados = Jogar_Dados()
        JogadorAtual = "nao jogador"
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{2: []})
        
    #Inicio teste para tipo da pontuacao caso de erro ao mostrar os tipos de pontuacao
    def testPontuacao_06_TipoPontuacao_Nao_eh_Possivel_Mostrar_Os_Tipos(self): 
        print("Caso de Teste Pontuacao 06 - nao eh possivel mostrar os tipos de pontuacao")
        #Nao sei como fazer para dar esse erro
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{3: []})
        
    #Inicio teste para tipo da pontuacao caso o parametro jogadorAtual nao corresponda com nenhum dos jogadores presentes no jogo   
    def testPontuacao_07_TipoPontuacao_JogadorAtual_Nao_Faz_Parte_De_Jogadores(self): 
        print("Caso de Teste Pontuacao 07 - JogadorAtual nao faz parte da lista Jogadores")
        Dados = Jogar_Dados()
        JogadorAtual = {3: "Carlos"}
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{4: []})

class Teste_ModuloTabuleiro_CriaTab(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Ja existe tabuleiro

    #Inicio teste para criacao do tabuleiro com sucesso
    def testTabuleiro_01_CriarTab_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 01- Tabuleiro inicializado com sucesso")
        retorno_esperado = Cria_Tab()
        self.assertEqual(retorno_esperado,0)

    #Inicio teste para criacao do tabuleiro caso ja exista um tabuleiro
    def testTabuleiro_02_CriarTab_Ja_Existe_Tabuleiro(self): 
        print("Caso de Teste Tabuleiro 02 - Tabuleiro ja existe")
        retorno_esperado = Cria_Tab()
        self.assertEqual(retorno_esperado,1)
        
class Teste_ModuloTabuleiro_DestruirTab(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Nao existe tabuleiro

    #Inicio teste para destruir tabuleiro com sucesso
    def testTabuleiro_03_DestruirTab_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 03 - Tabuleiro destruido com sucesso")
        retorno_esperado = Destruir_Tab()
        self.assertEqual(retorno_esperado,0)
        
    #Inicio teste para destruir tabuleiro caso nao exista tabuleiro
    def testTabuleiro_04_DestruirTab_Nao_Existe_Tab(self): 
        print("Caso de Teste Tabuleiro 04 - Tabuleiro nao existe")
        retorno_esperado = Destruir_Tab()
        self.assertEqual(retorno_esperado,1)

class Teste_ModuloTabuleiro_InserirPontuacao(unittest.TestCase):
    #Parametro:
        #pontuacao_atual - pontuacao gerada pelo conjunto de dados da rodada
        #jogadorAtual - jogador que gerou a pontuacao atual
    #Retornos possiveis:
        #0 - Sucesso
        #1 - Caso o parametro pontuacao_atual nao seja int
        #2 - Caso idJogadorAtual nao seja um int.
        #3 - Caso tipoPontucao nao seja string.
        #4 - Caso o parametro jogadorAtual nao corresponda com nenhum dos jogadores presentes no jogo
        #5 - Caso tipoPontuacao nao corresponda com nenhum tipo de pontuacao
    
    #Inicio teste para inserir pontuacao com sucesso    
    def testTabuleiro_05_InserirPontuacao_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 05 - Pontuacao Inserida com sucesso")
        Cria_Tab()
        Cria_Novo_Jogador("Carlos")
        Cria_Novo_Jogador("Aiko")
        idJogadorAtual = 2
        pontuacao_atual = 20
        tipoPontuacao = "Fours"
        retorno_esperado = InserirPontuacao(pontuacao_atual, idJogadorAtual, tipoPontuacao)
        self.assertEqual(retorno_esperado,0)
        
    #Inicio teste para inserir pontuacao caso o parametro pontuacao_atual nao seja int
    def testTabuleiro_06_InserirPontuacao_PontuacaoAtual_Nao_Int(self): 
        print("Caso de Teste Tabuleiro 06 - Pontuacao Atual nao eh INT")
        idJogadorAtual = 2
        pontuacao_atual = "Quina"
        tipoPontuacao = "Fours"
        retorno_esperado = InserirPontuacao(pontuacao_atual, idJogadorAtual, tipoPontuacao)
        self.assertEqual(retorno_esperado,1)

    #Inicio teste para inserir pontuacao caso idJogadorAtual nao seja um int
    def testTabuleiro_07_InserirPontuacao_JogadorAtual_Nao_Objeto(self): 
        print("Caso de Teste Tabuleiro 07 - Jogador Atual nao eh int")
        idJogadorAtual = "nao Jogador"
        pontuacao_atual = 20
        tipoPontuacao = "Fours"
        retorno_esperado = InserirPontuacao(pontuacao_atual, idJogadorAtual, tipoPontuacao)
        self.assertEqual(retorno_esperado,2)

    #Inicio teste para inserir pontuacao caso tipoPontuacao nao seja string
    def testTabuleiro_08_InserirPontuacao_JogadorAtual_Nao_Objeto(self): 
        print("Caso de Teste Tabuleiro 08 - TipoPontuacao nao e string")
        idJogadorAtual = 2
        pontuacao_atual = 20
        tipoPontuacao = 2
        retorno_esperado = InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        self.assertEqual(retorno_esperado,3)

    #Inicio teste para inserir pontuacao caso o parametro jogadorAtual nao corresponda com nenhum dos jogadores presentes no jogo   
    def testTabuleiro_09_InserirPontuacao_JogadorAtual_Nao_esta_Jogo(self): 
        print("Caso de Teste Tabuleiro 09 - Jogador Atual nao esta no Jogo")
        idJogadorAtual = 3
        jogadores = [{1: "Aiko"}, {2: "Carol"}]
        pontuacao_atual = 20
        tipoPontuacao = "Fours"
        retorno_esperado = InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        self.assertEqual(retorno_esperado,4)

    #Inicio teste para inserir pontuacao caso o parametro jogadorAtual nao corresponda com nenhum dos jogadores presentes no jogo   
    def testTabuleiro_10_InserirPontuacao_tipoPontuacao_Nao_esta_Jogo(self): 
        print("Caso de Teste Tabuleiro 10 - Tipo pontuacao nao corresponde a nenhum tipo de pontuacao")
        idJogadorAtual = 1
        pontuacao_atual = 20
        tipoPontuacao = "Six" #Seria 'Sixes'
        retorno_esperado = InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        self.assertEqual(retorno_esperado,5)        
        

class Teste_ModuloTabuleiro_VerificaVencedor(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis:
        #{0: ID} - Sucesso
        #{1: None} - Caso o tabuleiro esteja vazio.
        #{2: None} - Caso nao haja tabuleiro criado.
        #{3: None} - Caso o tabuleiro nao esteja completo.

    #Inicio teste para verificacao do vencedor com sucesso
    def testTabuleiro_11_VerificaVencedor_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 11 - Verificacao feita com sucesso")
        Destruir_Tab()
        Cria_Tab()
        Cria_Novo_Jogador("Carlos")
        Cria_Novo_Jogador("Aiko")
        idJogadorAtual = 1
        pontuacao_atual = 5 #5 1's
        tipoPontuacao = "Ones"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 4 #4 1's
        tipoPontuacao = "Ones"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 10 #5 2's
        tipoPontuacao = "Twos"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 10 #5 2's
        tipoPontuacao = "Twos"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 15 #5 3's
        tipoPontuacao = "Threes"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 15 #5 3's
        tipoPontuacao = "Threes"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 20 #5 4's
        tipoPontuacao = "Fours"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 20 #5 4's
        tipoPontuacao = "Fours"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 25 #5 5's
        tipoPontuacao = "Fives"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 25 #5 5's
        tipoPontuacao = "Fives"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 30 #5 6's
        tipoPontuacao = "Sixes"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 30 #5 6's
        tipoPontuacao = "Sixes"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 19 #3 iguais de 5 e 2 de 2 "Tres de um tipo"
        tipoPontuacao = "Three of a Kind"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 17 #3 iguais de 5 e 2 de 1 "Tres de um tipo"
        tipoPontuacao = "Three of a Kind"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 24 #4 iguais de 5 e 1 de 4 "Quatro de um tipo"
        tipoPontuacao = "Four of a Kind"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 23 #4 iguais de 5 e 1 de 3 "Quatro de um tipo"
        tipoPontuacao = "Four of a Kind"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 25 #Full House
        tipoPontuacao = "Full House"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 25 #Full House
        tipoPontuacao = "Full House"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 30 #Sequencia Baixa
        tipoPontuacao = "Small Straight"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 30 #Sequencia Baixa
        tipoPontuacao = "Small Straight"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 40 #Sequencia Alta
        tipoPontuacao = "Large Straight"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 40 #Sequencia Alta
        tipoPontuacao = "Large Straight"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 50 #YAHTZEE
        tipoPontuacao = "Yahtzee"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 50 #YAHTZEE
        tipoPontuacao = "Yahtzee"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 1
        pontuacao_atual = 0 #Chance
        tipoPontuacao = "Chance"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 0 #Chance
        tipoPontuacao = "Chance"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        retorno_esperado = Verifica_Vencedor()
        self.assertEqual(retorno_esperado,{0: 1})

    #Inicio teste para verificacao do vencedor caso o tabuleiro esteja vazio
    def testTabuleiro_12_VerificaVencedor_Tabuleiro_Vazio_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 12 - o tabuleiro esta vazio")
        Destruir_Tab()
        Cria_Tab()
        retorno_esperado = Verifica_Vencedor()
        self.assertEqual(retorno_esperado,{1: None})

    #Inicio teste para verificacao do vencedor caso nao haja tabuleiro criado
    def testTabuleiro_13_VerificaVencedor_Nao_Existe_Tab_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 13 - nao ha tabuleiro criado")
        Destruir_Tab()
        retorno_esperado = Verifica_Vencedor()
        self.assertEqual(retorno_esperado,{2: None})

    def testTabuleiro_14_VerificaVencedor_Tabuleiro_Nao_Completo(self): 
        print("Caso de Teste Tabuleiro 14 - tabuleiro nao esta completo")
        Cria_Tab()
        idJogadorAtual = 1
        pontuacao_atual = 15 #Chance
        tipoPontuacao = "Chance"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        idJogadorAtual = 2
        pontuacao_atual = 20 #Chance
        tipoPontuacao = "Chance"
        InserirPontuacao(pontuacao_atual, idJogadorAtual,tipoPontuacao)
        retorno_esperado = Verifica_Vencedor()
        self.assertEqual(retorno_esperado,{3: None})

class Teste_ModuloPrincipal_TelaInicial(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0, 1
        #0 - Sucesso
        #1 - Caso ja exista um jogo criado

    #Inicio teste para criar tela inicial com sucesso
    def testPrincipal_01_TelaInicial_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Principal 01- Tela Inicial criada com sucesso")
        retorno_esperado = Tela_Inicial()
        self.assertEqual(retorno_esperado,0)

    #Inicio teste para criar tela inicial caso ja exista um jogo criado
    def testPrincipal_02_TelaInicial_Jogo_Criado(self): 
        print("Caso de Teste Principal 02- ja existe jogo criado")
        Cria_Novo_Jogo()
        retorno_esperado = Tela_Inicial()
        self.assertEqual(retorno_esperado,1)

class Teste_ModuloPrincipal_Desenha_Tab(unittest.TestCase):
    #Parametro: NULL
    #Retornos possiveis: 0, 1
        #0 - Sucesso
        #1 - Caso nao exista um tabuleiro para ser desenhado.

    #Inicio teste para desenhar o tabuleiro com sucesso
    def testPrincipal_03_DesenhaTab_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Principal 03- Desenho do Tabuleiro criada com sucesso")
        Cria_Tab()
        retorno_esperado = Desenha_Tab()
        self.assertEqual(retorno_esperado,0)

    #Inicio teste para desenhar o tabuleiro caso nao exista um tabuleiro para ser desenhado
    def testPrincipal_04_TelaInicial_Nao_Existe_Tab(self): 
        print("Caso de Teste Principal 04- Nao existe tabuleiro pra ser desenhado")
        Destruir_Tab()
        retorno_esperado =Desenha_Tab()
        self.assertEqual(retorno_esperado,1)

unittest.main()
