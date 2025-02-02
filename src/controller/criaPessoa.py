from models.Pessoa import Pessoa

listaPessoas = []

def criacaoPessoas(num):
    for i in range(num):
        pessoa = Pessoa(f"Pessoa", f"{i + 1}")
        listaPessoas.append(pessoa)
    return listaPessoas