import unittest
from Jogador import Cria_Novo_Jogador, Destroi_Jogadores, Pega_Jogadores
from Dados import Cria_Dados, Muda_Status, Mostra_Dados, Destroi_Dados, Jogar_Dados
class Test(unittest.TestCase):    

    #Modulo Jogador
    def testJogador_01_CriaNovoJogador_Ok_Condicao_Retorno(self):
        print("Caso de Teste Jogador 01 - Criar jogador com sucesso")
        Destroi_Jogadores()
        retorno_esperado = Cria_Novo_Jogador('aiko')
        self.assertEqual(retorno_esperado, 0)

    def testJogador_02_CriaNovoJogador_Ja_Existem_Jogadores(self): 
        print("Caso de Teste Jogador 02 - Já existem dois jogadores cadastrados")
        Destroi_Jogadores()
        Cria_Novo_Jogador('aiko')
        Cria_Novo_Jogador('carlos')
        retorno_esperado = Cria_Novo_Jogador('aha')
        self.assertEqual(retorno_esperado, 1)

    def testJogador_03_CriaNovoJogador_Nome_Passado_Incorretamente(self): 
        print("Caso de Teste Jogador 03 - Nome passado incorretamente")
        Destroi_Jogadores()
        retorno_esperado = Cria_Novo_Jogador('')
        self.assertEqual(retorno_esperado, 2)
    
    def testJogador_04_PegarJogadores_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Jogador 04 - Pegar jogadores com sucesso")
        Destroi_Jogadores()
        Cria_Novo_Jogador('aiko')
        Cria_Novo_Jogador('carol')
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{0:[{1: "aiko"}, {2: "carol"}]})

    def testJogador_05_PegarJogadores_Falta_Um_Jogador(self): 
        print("Caso de Teste Jogador 05 - Falta um jogador para ser cadastrado")
        Destroi_Jogadores()
        Cria_Novo_Jogador('eu')
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{1:[]})

    def testJogador_06_PegarJogadores_Faltam_Dois_Jogadores(self): 
        print("Caso de Teste Jogador 06 - Faltam dois jogadores para serem cadastrados")
        Destroi_Jogadores()
        retorno_esperado = Pega_Jogadores()
        self.assertEqual(retorno_esperado,{2:[]})

    #Modulo Dados
    def testDados_01_CriaDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 01 - Criar dados com sucesso")
        Destroi_Dados()
        retorno_esperado = Cria_Dados()
        self.assertEqual(retorno_esperado,0)

    def testDados_02_CriaDados_Ja_Existem_Dados_Criados(self): 
        print("Caso de Teste Dados 02 - Já existem dados criados")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Cria_Dados()
        self.assertEqual(retorno_esperado,1)

    def testDados_03_MudaStatus_Ok_Condicao_Retorno_1(self): 
        print("Caso de Teste Dados 03 - Mudança de estado do dado 1 com sucesso")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status(1)
        self.assertEqual(retorno_esperado,0)

    def testDados_04_MudaStatus_Nao_Existe_Dado(self): 
        print("Caso de Teste Dados 04 - Esse ID não tem dado correspondente")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status(7)
        self.assertEqual(retorno_esperado,1)

    def testDados_05_MudaStatus_Nao_Ser_Int(self): 
        print("Caso de Teste Dados 05 - Parametro passado nao corresponde ao tipo 'int'")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Muda_Status("1")
        self.assertEqual(retorno_esperado,2)

    def testDados_06_MudaStatus_Lista_Vazia(self): 
        print("Caso de Teste Dados 06 - Lista de dados nao existente")
        Destroi_Dados()
        retorno_esperado = Muda_Status(1)
        self.assertEqual(retorno_esperado,3)

    def testDados_07_JogarDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 07 - Jogada feita com sucesso")
        Destroi_Dados()
        Cria_Dados()
        retorno_esperado = Jogar_Dados()
        self.assertEqual(retorno_esperado,0)

    def testDados_08_JogarDados_Dados_Nao_Existentes(self): 
        print("Caso de Teste Dados 08 - Dados nao existentes")
        Destroi_Dados()
        retorno_esperado = Jogar_Dados()
        self.assertEqual(retorno_esperado,1)

    def testDados_09_JogarDados_Todos_Dados_Congelados(self): 
        print("Caso de Teste Dados 09 - Todos os dados estão congelados")
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

    def testDados_10_MostraDados_Ok_Condicao_Retorno(self): 
        print("Caso de Teste Dados 10 - Dados foram mostrados com sucesso")
        Destroi_Dados()
        Cria_Dados()
        Jogar_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(list(retorno_esperado.keys())[0], 0)

    def testDados_11_MostraDados_Dados_Nao_Existentes(self): 
        print("Caso de Teste Dados 11 - Dados nao existentes")
        Destroi_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(retorno_esperado,{1: []})

    def testDados_12_MostraDados_Dados_Nao_Jogados(self): 
        print("Caso de Teste Dados 12 - Dados nao foram jogados")
        Cria_Dados()
        retorno_esperado = Mostra_Dados()
        self.assertEqual(retorno_esperado,{2: []})

unittest.main()
