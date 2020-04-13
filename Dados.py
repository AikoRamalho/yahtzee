import random
__all__ = ["Cria_Dados", "Muda_Status", "Mostra_Dados", "Destroi_Dados", "Jogar_Dados"]

dados = []

def Cria_Dados():
    qtdDados = len(dados)
    if(qtdDados == 5):
        return 1
    for i in range(1, 6):
        dados.append({ i: {"face": 0, "congelado": False} })
    return 0

def Muda_Status(id):
    if(type(id) != type(0)):
        return 2
    if(id not in range(1,6)):
        return 1
    if(len(dados) == 0):
        return 3
    state = dados[id-1][id]["congelado"]
    dados[id-1][id]["congelado"] = not state
    return 0

def verifica_dados_estao_todos_congelados():
    qtdDadosCongelados = 0
    i = 1
    while(i < 6):
        if(dados[i-1][i]["congelado"]):
            qtdDadosCongelados+=1
        i+=1
    if(qtdDadosCongelados == 5):
        return True
    return False

def Jogar_Dados():
    qtdDados = len(dados)
    i = 1
    if(qtdDados == 0):
        return 1 
    if(verifica_dados_estao_todos_congelados()):
        return 2
    while(i < 6):
        dados[i-1][i]["face"] = random.randint(1,6)
        i+=1
    return 0

def Mostra_Dados():
    qtdDados = len(dados)
    if(qtdDados == 0):
        return {1: []}
    if(dados[0][1]["face"] == 0):
        return {2: []}
    return {0: dados}

def Destroi_Dados():
    qtdJogadores = len(dados)
    if(qtdJogadores == 0):
        return 1
    dados.clear()