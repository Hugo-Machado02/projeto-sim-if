from models.Pessoa import Pessoa

listaPessoas = []

def criacaoPessoas(numeroPessoas):
    for i in range(numeroPessoas):
        pessoa = Pessoa(f"Pessoa", f"{i + 1}", "Natural")
        listaPessoas.append(pessoa)
    return listaPessoas

def criacaoPessoasCidades(nome, cidade):
        pessoa = Pessoa(nome, f" - {cidade}", cidade)
        return pessoa