def enviaLocal(pessoa, localAtual, ListaLocais):
    if not continuarLocal(pessoa):
        destino = pessoa.getDecisao(ListaLocais)
        localAtual.removePessoa(pessoa)
        destino.adicionaPessoa(pessoa)


#Verifica se o usuário quer continuar no local
def continuarLocal(pessoa):
    return pessoa.getDecisao([True, False])


def imprimirCidade(cidade):
    corredorPrincipal = cidade.getCorredor()
    blocos = cidade.getlistaBlocos()

    print(f"\n\nCidade: {cidade.getNome()}")
    print(f"->Corredor Principal -> {corredorPrincipal.getQuantidadePessoas()} Pessoas")
    for b in blocos:
        print(f"\t-> Bloco - {b.getNome()}")
        salas = b.getListaSalas()
        print(f"\t\t-> Corredor de Bloco: {b.getCorredor().getQuantidadePessoas()} Pessoas")
        for sala in salas:
            print(f"\t\t-> Sala: {sala.getQuantidadePessoas()} Pessoas")