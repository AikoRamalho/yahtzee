import unittest
from Jogador import Cria_Novo_Jogador, Destroi_Jogadores, Pega_Jogadores
from Dados import Cria_Dados, Muda_Status, Mostra_Dados, Destroi_Dados, Jogar_Dados
from Rodada import Cria_Rodada, Verifica_Tentativa, Atualiza_Tentativas, Modifica_Dados_Rodada, Deleta_Rodadas, Pega_Rodada
class Test(unittest.TestCase):    

##########################################################################
                        #Modulo Jogador

#Testes da função Cria_Novo_Jogador
    #Parametro: name
        #name - Um nome para o jogador passado como String
    #Retornos possíveis: 0,1,2
        #0 - Sucesso
        #1 - Lista Jogadores ja esta preenchida
        #2 - Nome do jogador foi passado incorretamente
    
    #Inicio teste de criação de jogador com sucesso
    def testJogador_01_CriaNovoJogador_Ok_Condicao_Retorno(self):
        print("Caso de Teste Jogador 01 - Criar jogador com sucesso")
        Destroi_Jogadores()
        retorno_esperado = Cria_Novo_Jogador('aiko')
        self.assertEqual(retorno_esperado, 0)
    #####Fim teste de criação de jogador com sucesso#####
        
    #Inicio teste de criação de jogador quando Jogadores está preenchido
    def testJogador_02_CriaNovoJogador_Ja_Existem_Jogadores(self): 
        print("Caso de Teste Jogador 02 - Ja existem dois jogadores cadastrados")
        Destroi_Jogadores()
        Cria_Novo_Jogador('aiko')
        Cria_Novo_Jogador('carlos')
        retorno_esperado = Cria_Novo_Jogador('aha')
        self.assertEqual(retorno_esperado, 1)
    #####Fim teste de criação de jogador quando Jogadores está preenchido#####

    #Inicio teste de criação de jogador caso o nome seja passado incorretamente
    def testJogador_03_CriaNovoJogador_Nome_Passado_Incorretamente(self): 
        print("Caso de Teste Jogador 03 - Nome passado incorretamente")
        Destroi_Jogadores()
        retorno_esperado = Cria_Novo_Jogador('')
        self.assertEqual(retorno_esperado, 2)
    #####Fim teste de criação de jogador caso o nome seja passado incorretamente#####
#Fim Teste da função Cria_Novo_Jogador

#Testes da função Pega_Jogadores
    #Parametro: NULL
    #Retornos possíveis: {0: jogadores}, {1: []}, {2: []}
        #{0: jogadores} - Sucesso
        #{1: []} - Falta um jogador para ser cadastrado
        #{2: []} - Faltam dois jogadores para serem cadastrados

    #Inicio teste para pegar a lista jogadores com sucesso
    def testJogador_04_PegarJogadores_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogador 04 - Pegar jogadores com sucesso")
        Destroi_Jogadores()
        Cria_Novo_Jogador('aiko')
        Cria_Novo_Jogador('carol')
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{0:[{1: "aiko"}, {2: "carol"}]})
    #####Fim teste para pegar a lista jogadores com sucesso

    #Inicio teste para pegar jogadores quando falta um jogador para ser cadastrado
    def testJogador_05_PegarJogadores_Falta_Um_Jogador(self): 
        print("Caso de Teste Jogador 05 - Falta um jogador para ser cadastrado")
        Destroi_Jogadores()
        Cria_Novo_Jogador('eu')
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{1:[]})
    #####Fim teste para pegar jogadores quando falta um jogador a ser cadastrado#####
        
    #Inicio teste para pegar jogadores quando faltam dois jogadores para serem cadastrados
    def testJogador_06_PegarJogadores_Faltam_Dois_Jogadores(self): 
        print("Caso de Teste Jogador 06 - Faltam dois jogadores para serem cadastrados")
        Destroi_Jogadores()
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{2:[]})
    #####Fim teste para pegar jogadores quando faltam dois jogadores para serem cadastrados#####
#Fim Teste da função Pega_Jogadores
        
##########################################################################
                        #Modulo Dados

#Testes da função Cria_Dados
    #Parametro: NULL
    #Retornos possíveis: 0,1
        #0 - Sucesso
        #1 - Ja existem dados criados

    #Inicio teste para criação de dados com sucesso
    def testDados_01_CriaDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 01 - Criar dados com sucesso")
        Destroi_Dados()
        retorno_esperado = Cria_Dados()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para criação de dados com sucesso#####

    #Inicio teste para criação de dados caso ja existam dados criados
    def testDados_02_CriaDados_Ja_Existem_Dados_Criados(self): 
        print("Caso de Teste Dados 02 - Ja existem dados criados")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Cria_Dados()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para criação de dados caso ja existam dados criados#####
#Fim testes da função Cria_Dados

#Testes da função Muda_Status
    #Parametro: id
        #id - ID de um dado especifico
    #Retornos possíveis: 0,1
        #0 - Sucesso
        #1 - Ja existem dados criados

    #Inicio teste para mudança de status de um dado especifico com sucesso
    def testDados_03_MudaStatus_Ok_Condicao_Retorno_1(self): 
        print("Caso de Teste Dados 03 - Mudanca de estado do dado 1 com sucesso")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status(1)
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para mudança de status de um dado especifico com sucesso#####
        
    #Inicio teste para mudança de status caso o id passado nao corresponda a nenhum dos ids disponiveis
    def testDados_04_MudaStatus_Nao_Existe_Dado(self): 
        print("Caso de Teste Dados 04 - Esse ID nao tem dado correspondente")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status(7)
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para mudança de status caso o id passado nao corresponda a nenhum dos ids disponiveis#####

    #Inicio teste para mudança de status caso o id passado nao corresponda ao tipo int
    def testDados_05_MudaStatus_Nao_Ser_Int(self): 
        print("Caso de Teste Dados 05 - Parametro passado nao corresponde ao tipo 'int'")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status("1")
        self.assertEqual(retorno_esperado,2)
    #####Fim teste para mudança de status caso o id passado nao corresponda ao tipo int#####

    #Inicio teste para mudança de status caso a lista de dados nao exista
    def testDados_06_MudaStatus_Lista_Vazia(self): 
        print("Caso de Teste Dados 06 - Lista de dados nao existente")
        Destroi_Dados()
        retorno_esperado = Muda_Status(1)
        self.assertEqual(retorno_esperado,3)
    #####Fim teste para mudança de status caso a lista de dados nao exista#####   
#Fim testes da função Muda_Status

#Testes da função Jogar_Dados
    #Parametro: NULL
    #Retornos possíveis: 0, 1, 2
        #0 - Sucesso
        #1 - Nao existem dados
        #2 - Todos os dados estao congelados

    #Inicio teste para jogar dados com sucesso
    def testDados_07_JogarDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 07 - Jogada feita com sucesso")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Jogar_Dados()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para jogar dados com sucesso#####

    #Inicio teste para jogar dados caso nao existam dados
    def testDados_08_JogarDados_Dados_Nao_Existentes(self): 
        print("Caso de Teste Dados 08 - Dados nao existentes")
        Destroi_Dados()
        retorno_esperado = Jogar_Dados()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para jogar dados caso nao existam dados#####

    #Inicio teste para jogar dados caso todos os dados estejam congelados
    def testDados_09_JogarDados_Todos_Dados_Congelados(self): 
        print("Caso de Teste Dados 09 - Todos os dados estao congelados")
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
    #####Fim teste para jogar dados caso todos os dados estejam congelados#####
#Fim testes da função Jogar_Dados

#Testes da função Mostra_Dados
    #Parametro: NULL
    #Retornos possíveis: {0: dados}, {1: []}, {2: []}
        #{0: dados} - Sucesso
        #{1: []} - Nao existem dados
        #{2: []} - Os dados nao foram jogados
        
    #Inicio teste para mostrar dados com sucesso
    def testDados_10_MostraDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 10 - Dados foram mostrados com sucesso")
        Destroi_Dados()
        Cria_Dados()
        Jogar_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(list(retorno_esperado.keys())[0], 0)
    #####Fim teste para mostrar dados com sucesso#####

    #Inicio teste para mostrar dados caso nao existam dados
    def testDados_11_MostraDados_Dados_Nao_Existentes(self): 
        print("Caso de Teste Dados 11 - Dados nao existentes")
        Destroi_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(retorno_esperado,{1: []})
    #####Fim teste para mostrar dados caso nao existam dados#####

    #Inicio teste para mostrar dados caso os dados nao tenham sido jogados
    def testDados_12_MostraDados_Dados_Nao_Jogados(self): 
        print("Caso de Teste Dados 12 - Dados nao foram jogados")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(retorno_esperado,{2: []})
    #####Fim teste para mostrar dados caso os dados nao tenham sido jogados#####     
#Fim testes da função Mostra_Dados
    
##########################################################################
                        #Modulo Rodada

#Testes da função Cria_Rodada
    #Parametro: NULL
    #Retornos possíveis: 0, 1
        #0 - Sucesso
        #1 - Numero maximo de rodadas ja foi atingido
        
    #Inicio teste para criar rodada com sucesso        
    def testRodada_01_CriaRodada_Ok_Condicao_Retorno(self):
        print("Caso de Teste Rodada 01 - Criar dados com sucesso")
        retorno_esperado = Cria_Rodada()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para criar rodada com sucesso#####
        
    #Inicio teste para criar rodada caso o numero maximo de rodadas ja tenha sido atingido
    def testRodada_02_CriaRodada_Numero_Maximo_Atingido(self): 
        print("Caso de Teste Rodada 02 - O Numero de rodadas do jogo ja foi atingido")
        Deleta_Rodadas()
        for _ in range(27):
            Cria_Rodada()
        retorno_esperado = Cria_Rodada()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para criar rodada caso o numero maximo de rodadas ja tenha sido atingido#####
#Fim testes da função Cria_Rodada

#Testes da função Verifica_Tentativa
    #Parametro: NULL
    #Retornos possíveis: 0, 1, 2
        #0 - Sucesso
        #1 - Nao existe tentativa disponivel
        #2 - Nao existe rodada criada
        
    #Inicio teste para verificar tentativa com sucesso    
    def testRodada_03_Verifica_Tentativa_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 03 - Ainda existe tentativa disponivel")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Verifica_Tentativa()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para verificar tentativa com sucesso#####
        
    #Inicio teste para verificar tentativa caso nao existam tentativas disponiveis
    def testRodada_04_Verifica_Tentativa_Nao_Existem_Tentativas(self): 
        print("Caso de Teste Rodada 04 -Nao existe tentativa disponivel")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno = Atualiza_Tentativas(0)
        print('retorno da atualiza tentativas: ', retorno)
        retorno_esperado = Verifica_Tentativa()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para verificar tentativa caso nao existam tentativas disponiveis#####
        
    #Inicio teste para verificar tentativa caso nao exista rodada criada
    def testRodada_05_Verifica_Tentativa_Nao_Existe_Rodada(self): 
        print("Caso de Teste Rodada 05 - Nao existe rodada criada")
        Deleta_Rodadas()
        retorno_esperado = Verifica_Tentativa()
        self.assertEqual(retorno_esperado,2)
    #####Fim teste para verificar tentativa caso nao exista rodada criada#####
#Fim testes da função Verifica_Tentativa

#Testes da função Atualiza_Tentativa
    #Parametro: Num
        #Num - Numero de tentativas que quer se colocar naquela rodada
    #Retornos possíveis: 0, 1, 2, 3, 4
        #0 - Sucesso
        #1 - Numero inconsistente
        #2 - numero de tentativas diferente de tentativas -1 do ultimo objeto
        #3 - Numero nao condiz com o range aceito
        #4 - Nao existe rodada criada
        
    #Inicio teste para atualizar tentativa com sucesso
    def testRodada_06_Atualiza_Tentativa_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 06 - Suceso, tentativa atualizada")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Atualiza_Tentativas(2)
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para atualizar tentativa com sucesso#####

    #Inicio teste para atualizar tentativa caso o numero seja inconsistente        
    def testRodada_07_Atualiza_Tentativa_Numero_Inconsistente_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 07 - Numero inconsistente")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Atualiza_Tentativas(3)
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para atualizar tentativa caso o numero seja inconsistente#####

    #Inicio teste para atualizar tentativa caso o numero de tentativas do parametro seja diferente de tentativas -1 do ultimo objeto    
    def testRodada_08_Atualiza_Tentativa_NTentativas_Diferente(self): 
        print("Caso de Teste Rodada 08 - O numero de tentativas no paramentro eh diferente de tentativas -1 do ultimo objeto")
        Deleta_Rodadas()
        retorno_esperado = Atualiza_Tentativas(10)
        self.assertEqual(retorno_esperado,2)
    #####Fim teste para atualizar tentativa caso o numero de tentativas do parametro seja diferente de tentativas -1 do ultimo objeto#####

    #Inicio teste para atualizar tentativa caso o parametro nao seja aceito
    def testRodada_09_Atualiza_Tentativa_Parametro_NaoAceito(self): 
        print("Caso de Teste Rodada 09 - Tentativa no parametro nao condiz com o range aceito")
        Deleta_Rodadas()
        retorno_esperado = Atualiza_Tentativas("1")
        self.assertEqual(retorno_esperado,3)
    #####Fim teste para atualizar tentativa caso o parametro nao seja aceito#####

    #Inicio teste para atualizar tentativa caso nao exista rodada criada
    def testRodada_10_Atualiza_Tentativa_Nao_Existe_RodadaCriada(self): 
        print("Caso de Teste Rodada 10 -Nao existe rodada criada")
        Deleta_Rodadas()
        retorno_esperado = Atualiza_Tentativas(2)
        self.assertEqual(retorno_esperado,4)
    #####Fim teste para atualizar tentativa caso nao exista rodada criada#####
#Fim testes da função Atualiza_Tentativa

#Testes da função Modifica_Dados_Rodada
    #Parametro: NULL
    #Retornos possíveis: 0, 1, 2, 3, 4
        #0 - Sucesso
        #1 - Nao tem tentativas sobrando
        #2 - Os dados estão congelados
        #3 - Nao existem dados
        #4 - Nao existe rodada criada

    #Inicio teste para modificar a rodada com sucesso    
    def testRodada_11_ModificaDadosRodada_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 11 - Sucesso, objeto rodada atualizado")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para modificar a rodada com sucesso#####

    #Inicio teste para modificar a rodada caso nao tenham tentativas sobrando
    def testRodada_12_ModificaDadosRodada_Sem_Tentativas_Sobrando(self): 
        print("Caso de Teste Rodada 12 -Nao tem tentivas sobrando")
        Deleta_Rodadas()
        Cria_Rodada()
        Atualiza_Tentativas(0)
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para modificar a rodada caso nao tenham tentativas sobrando#####

    #Inicio teste para modificar a rodada caso os dados estejam congelados    
    def testRodada_13_ModificaDadosRodada_Dados_Congelados(self): 
        print("Caso de Teste Rodada 13 -Dados estao Congelados")
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
    #####Fim teste para modificar a rodada caso os dados estejam congelados#####
        
    #Inicio teste para modificar a rodada caso nao existam dados    
    def testRodada_14_ModificaDadosRodada_Nao_Existe_Dado(self): 
        print("Caso de Teste Rodada 14 -Nao existem dados")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,3)
    #####Fim teste para modificar a rodada caso nao existam dados#####
        
    #Inicio teste para modificar a rodada caso nao exista rodada    
    def testRodada_15_ModificaDadosRodada_Nao_Existe_Rodada(self): 
        print("Caso de Teste Rodada 15 - Nao existe rodada criada")
        Deleta_Rodadas()
        retorno_esperado = Modifica_Dados_Rodada()
        Destroi_Dados()
        self.assertEqual(retorno_esperado,4)
     #####Fim teste para modificar a rodada caso nao exista rodada######   
#Fim testes da função Modifica_Dados_Rodada

#Testes da função Pega_Rodada
    #Parametro: NULL
    #Retornos possíveis: {0: rodadas[numero_rodada-1]}, {1: None}
        #{0: rodadas[numero_rodada-1]} - Sucesso
        #{1: None} - Lista de Rodadas esta vazia

    #Inicio teste para pegar rodada com sucesso    
    def testRodada_16_PegaRodada_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Rodada 16 - Sucesso")
        Deleta_Rodadas()
        Cria_Rodada()
        retorno_esperado = Pega_Rodada()
        self.assertEqual(retorno_esperado,{0: { 1: {"tentativas":3 ,"dados_rodada": []} }})
    #####Fim teste para pegar rodada com sucesso######

    #Inicio teste para pegar rodada caso a lista de Rodadas esteja vazia    
    def testRodada_17_PegaRodada_Lista_Rodadas_Vazia(self): 
        print("Caso de Teste Rodada 17 - Lista de Rodadas Vazia")
        Deleta_Rodadas()
        retorno_esperado = Pega_Rodada()
        self.assertEqual(retorno_esperado,{1:None})
    #####Fim teste para pegar rodada caso a lista de Rodadas esteja vazia#####
#Fim testes da função Pega_Rodada

##########################################################################
                        #Modulo Jogo

#Testes da função Cria_Novo_Jogo
    #Parametro: NULL
    #Retornos possíveis: 0,1
        #0 - Sucesso
        #1 - Jogo ja criado

    #Inicio teste para criar novo jogo com sucesso
    def testJogo_01_CriaNovoJogo_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogo 01 - Jogo novo criado com sucesso")
        retorno_esperado = Cria_Novo_Jogo()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para criar novo jogo com sucesso#####    

    #Inicio teste para criar novo jogo caso ja haja um jogo criado
    def testJogo_02_CriaNovoJogo_Jogo_Ja_Criado(self): 
        print("Caso de Teste Jogo 02 - Jogo ja criado")
        retorno_esperado = Cria_Novo_Jogo()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para criar novo jogo caso ja haja um jogo criado#####
#Fim testes da função Cria_Novo_Jogo

#Testes da função Verifica_Rodada
    #Parametro: ID
        #ID - Id da rodada
    #Retornos possíveis: 0,1,2,3
        #0 - Sucesso
        #1 - Ainda restam tentativas
        #2 - Id nao correspondente com os ids disponiveis
        #3 - Id passado incorretamente

    #Inicio teste para verificar rodada com sucesso                     
    def testJogo_03_VerificaRodada_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogo 03 - Rodada Verificada corretamente")
        Atualiza_Tentativas(0)                
        retorno_esperado = Verifica_Rodada(1) #Considerando que o ID da rodada é um int que começa em 1
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para verificar rodada com sucesso#####

    #Inicio teste para verificar rodada caso restem tentativas
    def testJogo_04_VerificaRodada_Ainda_Restam_Tentativas(self): 
        print("Caso de Teste Jogo 04 - Ainda Restam Tentativas")
        Cria_Rodada()         
        retorno_esperado = Verifica_Rodada(2) 
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para verificar rodada caso restem tentativas#####
        
    #Inicio teste para verificar rodada caso o id passado nao corresponda aos ids disponiveis                   
    def testJogo_05_VerificaRodada_Nao_Tem_O_ID(self): 
        print("Caso de Teste Jogo 05 - Id nao correspondente com os ids disponiveis")   
        retorno_esperado = Verifica_Rodada(200) 
        self.assertEqual(retorno_esperado,2)
    #####Fim teste para verificar rodada caso o id passado nao corresponda aos ids disponiveis#####

    #Inicio teste para verificar rodada caso o id tenha sido passado incorretamente
    def testJogo_06_VerificaRodada_ID_Passado_Incorretamente(self): 
        print("Caso de Teste Jogo 06 - ID passado incorretamente")   
        retorno_esperado = Verifica_Rodada("1") 
        self.assertEqual(retorno_esperado,3)
    #####Fim teste para verificar rodada caso o id tenha sido passado incorretamente#####
#Fim testes da funcao Verifica_Rodada

#Testes da função Atualiza_JogadorAtual
    #Parametros: JogadorAtual,Jogadores
        #Jogadores - A lista de Jogadores do jogo
        #JogadorAtual - O valor de jogador_atual do objeto jogo
    #Retornos possíveis: {0: Jogador_Atual}, {1: []}, {2: []}, {3: []}
        #{0: Jogador_Atual} - Sucesso
        #{1: []} - Caso o parâmetro Jogadores não sejam uma lista de dois jogadores.
        #{2: []} - Caso JogadorAtual não seja um objeto Jogador.
        #{3: []} - Caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo

    #Inicio teste para atualizar jogador atual com sucesso
    def testJogo_07_AtualizaJogadorAtual_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogo 07 - Sucesso ao atualizar o jogador")
        jogadorAtual = {1: "Aiko"}
        jogadores = [{1: "Aiko"}, {2: "Carol"}]
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores) #Considerando que começa com o Aiko
        self.assertEqual(retorno_esperado,{0: {2: "Carol"}})
    #####Fim teste para atualizar jogador atual com sucesso#####

    #Inicio teste para atualizar jogador atual caso o parâmetro Jogadores não sejam uma lista de dois jogadores
    def testJogo_08_AtualizaJogadorAtual_Jogadores_Nao_Passado_Corretamente(self): 
        print("Caso de Teste Jogo 08 - Jogadores nao passado corretamente")
        jogadorAtual = {2: "Carol"}
        jogadores = "nao lista"                 
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores)
        self.assertEqual(retorno_esperado,{1: []})
    #####Fim teste para atualizar jogador atual caso o parâmetro Jogadores não sejam uma lista de dois jogadores#####

    #Inicio teste para atualizar jogador atual caso JogadorAtual não seja um objeto Jogador    
    def testJogo_09_AtualizaJogadorAtual_JogadorAtual_Nao_Passado_Corretamente(self): 
        print("Caso de Teste Jogo 09 - JogadorAtual nao é um objeto Jogador")
        jogadorAtual = "nao Jogador"
        jogadores = [{1: "Aiko"}, {2: "Carol"}]             
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores)
        self.assertEqual(retorno_esperado,{2: []})
    #####Fim teste para atualizar jogador atual caso JogadorAtual não seja um objeto Jogador#####
        
    #Inicio teste para atualizar jogador atual caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo
    def testJogo_10_AtualizaJogadorAtual_JogadorAtual_Nao_Faz_Parte_De_Jogadores(self): 
        print("Caso de Teste Jogo 10 - JogadorAtual nao faz parte da lista Jogadores")
        jogadorAtual = {3: "Carlos"}
        jogadores = [{1: "Aiko"}, {2: "Carol"}]             
        retorno_esperado = Atualiza_JogadorAtual(jogadorAtual,jogadores)
        self.assertEqual(retorno_esperado,{3: []})
    #####Fim teste para atualizar jogador atual caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo#####
#Fim testes da funcao Atualiza_JogadorAtual

##########################################################################
                        #Modulo Pontuacao
#AJEITAR ESSES TESTES!!!
#Testes da função Calcula_Pontuacao
    #Parametro: NULL
    #Retornos possíveis: {0: PontosJogador}, {1: []}
        #{0: Jogador_Atual} - Sucesso
        #{1: []} - Caso as casas da coluna não esteja devidamente preenchidas
        
    #Inicio teste para calcular pontuacao com sucesso 
    def testPontuacao_01_CalculaPontuacao_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Pontuacao 01 - Pontuacao calculada com sucesso")
        retorno_esperado = Calcula_Pontuacao()
        self.assertEqual(retorno_esperado,{0: pontosJogador})#Nao sei como passar pontosJogador
    #####Fim teste para calcular pontuacao com sucesso#####
        
    #Inicio teste para calcular pontuacao caso as casas da coluna nao estejam devidamente preenchidas                     
    def testPontuacao_02_CalculaPontuacao_Colunas_Nao_Preenchidas(self): 
        print("Caso de Teste Pontuacao 02 - Casas da coluna nao estao devidamente preenchidas")
        #Nao sei como fazer para dar esse erro
        retorno_esperado = Calcula_Pontuacao()
        self.assertEqual(retorno_esperado,{1: []})
    #####Fim teste para calcular pontuacao caso as casas da coluna nao estejam devidamente preenchidas#####
#Fim testes da função Calcula_Pontuacao

#Testes da função Tipo_Pontuacao
    #Parametro: Dados, JogadorAtual
        #Dados - Os dados gerados pelo jogador
        #JogadorAtual - O Jogador Atual
    #Retornos possíveis: {0: ListaPontuação}, {1: []}, {2: []}, {3: []}, {4: []}
        #{0: Jogador_Atual} - Sucesso
        #{1: []} - Caso o Dado não seja um objeto Dado
        #{2: []} - Caso JogadorAtual não seja um objeto Jogador
        #{3: []} - Caso de erro ao mostrar os tipos de pontuação
        #{4: []} - Caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo

    #Inicio teste para tipo da pontuacao com sucesso
    def testPontuacao_03_TipoPontuacao_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Pontuacao 03 - Sucesso ao dizer que tipo de pontuacao pode ser feita")
        Dados = Jogar_Dados()
        JogadorAtual = {2: "Carol"}
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{0: ListaPontuacao})
    #####Fim teste para tipo da pontuacao com sucesso#####
        
    #Inicio teste para tipo da pontuacao caso o Dado não seja um objeto Dado
    def testPontuacao_04_TipoPontuacao_Dado_Nao_Seja_Objeto_Dado(self): 
        print("Caso de Teste Pontuacao 04 - Dado não é um objeto Dado")
        Destruir_Dados()
        JogadorAtual = {2: "Carol"}
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{1: []})
    #####Fim teste para tipo da pontuacao caso o Dado não seja um objeto Dado
    #Inicio teste para tipo da pontuacao caso JogadorAtual não seja um objeto Jogador    
    def testPontuacao_05_TipoPontuacao_JogadorAtual_Nao_Seja_Objeto_Jogador(self): 
        print("Caso de Teste Pontuacao 05 - Dado não é um objeto Dado")
        Dados = Jogar_Dados()
        JogadorAtual = "nao jogador"
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{2: []})
    #####Fim teste para tipo da pontuacao caso JogadorAtual não seja um objeto Jogador#####
        
    #Inicio teste para tipo da pontuacao caso de erro ao mostrar os tipos de pontuação
    def testPontuacao_06_TipoPontuacao_Nao_É_Possivel_Mostrar_Os_Tipos(self): 
        print("Caso de Teste Pontuacao 06 - Não é possível mostrar os tipos de pontuação")
        #Nao sei como fazer para dar esse erro
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{3: []})
    #####Fim teste para tipo da pontuacao caso de erro ao mostrar os tipos de pontuação#####
        
    #Inicio teste para tipo da pontuacao caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo   
    def testPontuacao_07_TipoPontuacao_JogadorAtual_Nao_Faz_Parte_De_Jogadores(self): 
        print("Caso de Teste Pontuacao 07 - JogadorAtual nao faz parte da lista Jogadores")
        Dados = Jogar_Dados()
        JogadorAtual = {3: "Carlos"}
        retorno_esperado = Tipo_Pontuacao(Dados,JogadorAtual)
        self.assertEqual(retorno_esperado,{4: []})
    #####Fim teste para tipo da pontuacao caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo#####
#Fim testes da funcao Tipo_Pontuacao        

##########################################################################
                        #Modulo Tabuleiro

#Testes da função Cria_Tab
    #Parametro: NULL
    #Retornos possíveis: 0, 1
        #0 - Sucesso
        #1 - Ja existe tabuleiro

    #Inicio teste para criacao do tabuleiro com sucesso
    def testTabuleiro_01_CriarTab_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 01- Tabuleiro inicializado com sucesso")
        retorno_esperado = Cria_Tab()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para criacao do tabuleiro com sucesso#####

    #Inicio teste para criacao do tabuleiro caso ja exista um tabuleiro
    def testTabuleiro_02_CriarTab_Ja_Existe_Tabuleiro(self): 
        print("Caso de Teste Tabuleiro 02 - Tabuleiro ja existe")
        retorno_esperado = Criar_Tab()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para criacao do tabuleiro caso ja exista um tabuleiro#####
#Fim testes da funcao Cria_Tab
        
#Testes da função Destruir_Tab
    #Parametro: NULL
    #Retornos possíveis: 0, 1
        #0 - Sucesso
        #1 - Nao existe tabuleiro

    #Inicio teste para destruir tabuleiro com sucesso
    def testTabuleiro_03_DestruirTab_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 03 - Tabuleiro destruido com sucesso")
        retorno_esperado = Destruir_Tab()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para destruir tabuleiro com sucesso#####
        
    #Inicio teste para destruir tabuleiro caso nao exista tabuleiro
    def testTabuleiro_04_DestruirTab_Nao_Existe_Tab(self): 
        print("Caso de Teste Tabuleiro 04 - Tabuleiro nao existe")
        retorno_esperado = Destruir_Tab()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para destruir tabuleiro com sucesso#####
#Fim testes da funcao Destruir_Tab

#Testes da função InserirPontuacao
    #Parametro: pontuação_atual, jogadorAtual
        #pontuação_atual - pontuação gerada pelo conjunto de dados da rodada
        #jogadorAtual - jogador que gerou a pontuação atual
    #Retornos possíveis: {0: listaPont}, {1: []}, {2: []}, {3: []}
        #{0: listaPont} - Sucesso
        #{1: []} - Caso o parametro pontuação_atual não seja int
        #{2: []} - Caso JogadorAtual não seja um objeto Jogador.
        #{3: []} - Caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo
        
    #Inicio teste para inserir pontuacao com sucesso    
    def testTabuleiro_05_InserirPontuacao_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 05 - Pontuacao Inserida com sucesso")
        Cria_Tab()
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 20
        retorno_esperado = InserirPontuação(pontuação_atual, jogadorAtual)
        self.assertEqual(retorno_esperado,{0:listaPont})# nao sei retornar a lista
    #####Fim teste para inserir pontuacao com sucesso#####
        
    #Inicio teste para inserir pontuacao caso o parametro pontuação_atual não seja int
    def testTabuleiro_06_InserirPontuacao_PontuacaoAtual_Nao_Int(self): 
        print("Caso de Teste Tabuleiro 06 - Pontuacao Atual nao é INT")
        jogadorAtual = {2: "Carol"}
        pontuação_atual = "Quina" 
        retorno_esperado = InserirPontuação(pontuação_atual, jogadorAtual)
        self.assertEqual(retorno_esperado,{1:[]})
    #####Fim teste para inserir pontuacao caso o parametro pontuação_atual não seja int#####

    #Inicio teste para inserir pontuacao caso JogadorAtual não seja um objeto Jogador
    def testTabuleiro_07_InserirPontuacao_JogadorAtual_Nao_Objeto(self): 
        print("Caso de Teste Tabuleiro 07 - Jogador Atual não é objeto")
        jogadorAtual = "nao Jogador"
        pontuação_atual = 20            
        retorno_esperado = InserirPontuação(pontuação_atual, jogadorAtual)
        #tem que colocar aqui como retorno esperado o inserir pontuacao? ou só atualiza
        #tem que colocar só a InserirPontuação
        self.assertEqual(retorno_esperado,{2:[]})
    #####Fim teste para inserir pontuacao caso JogadorAtual não seja um objeto Jogador#####

    #Inicio teste para inserir pontuacao caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo   
    def testTabuleiro_08_InserirPontuacao_JogadorAtual_Nao_Está_Jogo(self): 
        print("Caso de Teste Tabuleiro 08 - Jogador Atual não está no Jogo")
        jogadorAtual = {3: "Carlos"}
        jogadores = [{1: "Aiko"}, {2: "Carol"}]
        pontuação_atual = 20  
        retorno_esperado = InserirPontuação(pontuação_atual, jogadorAtual)
        self.assertEqual(retorno_esperado,{3:[]})
    #####Fim teste para inserir pontuacao caso o parametro jogadorAtual não corresponda com nenhum dos jogadores presentes no jogo#####
#Fim testes da funcao InserirPontuacao

#Testes da função Verifica_Vencedor
    #Parametro: NULL
    #Retornos possíveis: {0: ID}, {1: null}, {2: null}
        #{0: ID} - Sucesso
        #{1: null} - Caso o tabuleiro esteja vazio.
        #{2: null} - Caso não haja tabuleiro criado.

    #Inicio teste para verificacao do vencedor com sucesso
    def testTabuleiro_09_VerificaVencedor_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 09 - Verificação feita com sucesso")
        Destruir_Tab()
        #Nao sei se é necessario, mas vou colocar todas as pontuações para preencher o tabuleiro
        Cria_Tab()
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 5 #5 1's
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 4 #4 1's 
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 10 #5 2's
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 10 #5 2's 
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 15 #5 3's
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 15 #5 3's 
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 20 #5 4's
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 20 #5 4's 
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 25 #5 5's
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 25 #5 5's 
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 30 #5 6's
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 30 #5 6's 
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 19 #3 iguais de 5 e 2 de 2 "Tres de um tipo"
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 17 #3 iguais de 5 e 2 de 1 "Tres de um tipo"
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 24 #4 iguais de 5 e 1 de 4 "Quatro de um tipo"
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 23 #4 iguais de 5 e 1 de 3 "Quatro de um tipo"
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 25 #Full House
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 25 #Full House
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 30 #Sequencia Baixa
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 30 #Sequencia Baixa
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 40 #Sequencia Alta
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 40 #Sequencia Alta
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 50 #YAHTZEE
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 50 #YAHTZEE
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {1: "Aiko"}
        pontuação_atual = 0 #Chance
        InserirPontuação(pontuação_atual, jogadorAtual)
        jogadorAtual = {2: "Carol"}
        pontuação_atual = 0 #Chance
        InserirPontuação(pontuação_atual, jogadorAtual)
        retorno_esperado = Verifica_Vencedor()
        self.assertEqual(retorno_esperado,{0: 1})
    #####Fim teste para verificacao do vencedor com sucesso#####

    #Inicio teste para verificacao do vencedor caso o tabuleiro esteja vazio
    def testTabuleiro_09_VerificaVencedor_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 09 - Verificação feita com sucesso")
        Destruir_Tab()
        Cria_Tab()
        retorno_esperado = Verifica_Vencedor()
        self.assertEqual(retorno_esperado,{1: NULL})
    #####Fim teste para verificacao do vencedor caso o tabuleiro esteja vazio#####

    #Inicio teste para verificacao do vencedor caso não haja tabuleiro criado
    def testTabuleiro_09_VerificaVencedor_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Tabuleiro 09 - Verificação feita com sucesso")
        Destruir_Tab()
        retorno_esperado = Verifica_Vencedor()
        self.assertEqual(retorno_esperado,{2: NULL})
    #####Fim teste para verificacao do vencedor caso não haja tabuleiro criado#####
#Fim testes da funcao Verifica_Vencedor
        
##########################################################################
                        #Modulo Principal

#Testes da função Tela_Inicial
    #Parametro: NULL
    #Retornos possíveis: 0, 1
        #0 - Sucesso
        #1 - Caso já exista um jogo criado

    #Inicio teste para criar tela inicial com sucesso
    def testPrincipal_01_TelaInicial_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Principal 01- Tela Inicial criada com sucesso")
        retorno_esperado = Tela_Inicial()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para criar tela inicial com sucesso#####

    #Inicio teste para criar tela inicial caso já exista um jogo criado
    def testPrincipal_02_TelaInicial_Jogo_Criado(self): 
        print("Caso de Teste Principal 02- Já existe jogo criado")
        Cria_Novo_Jogo()
        retorno_esperado = Tela_Inicial()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para criar tela inicial caso já exista um jogo criado#####
#Fim testes da funcao Tela_Inicial

#Testes da função Desenha_Tab
    #Parametro: NULL
    #Retornos possíveis: 0, 1
        #0 - Sucesso
        #1 - Caso não exista um tabuleiro para ser desenhado.

    #Inicio teste para desenhar o tabuleiro com sucesso
    def testPrincipal_03_DesenhaTab_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Principal 03- Desenho do Tabuleiro criada com sucesso")
        Cria_Tab()
        retorno_esperado = Desenha_Tab()
        self.assertEqual(retorno_esperado,0)
    #####Fim teste para desenhar o tabuleiro com sucesso#####

    #Inicio teste para desenhar o tabuleiro caso não exista um tabuleiro para ser desenhado
    def testPrincipal_04_TelaInicial_Nao_Existe_Tab(self): 
        print("Caso de Teste Principal 04- Nao existe tabuleiro pra ser desenhado")
        Destruir_Tab()
        retorno_esperado =Desenha_Tab()
        self.assertEqual(retorno_esperado,1)
    #####Fim teste para desenhar o tabuleiro caso não exista um tabuleiro para ser desenhado#####
#Fim testes da funcao Desenha_Tab

unittest.main()
