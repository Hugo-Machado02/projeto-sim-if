from models.Pessoa import Pessoa

listaPessoas = []

def criacaoPessoas(num):
    for i in range(num):
        pessoa = Pessoa(f"Pessoa {i + 1}", f"local {i + 1}", f"Local {i + 1}")
        listaPessoas.append(pessoa)
    return listaPessoas