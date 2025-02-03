from models.Pessoa import Pessoa

listaPessoas = []

def criacaoPessoas(numeroPessoas):
    for i in range(numeroPessoas):
        pessoa = Pessoa(f"Pessoa", f"{i + 1}")
        listaPessoas.append(pessoa)
    return listaPessoas