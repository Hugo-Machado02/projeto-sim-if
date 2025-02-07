def enviaLocal(pessoa, localAtual, ListaLocais):
    destino = pessoa.getDecisao(ListaLocais)
    localAtual.removePessoa(pessoa)
    destino.adicionaPessoa(pessoa)
    print(f"\n-> {pessoa.getNome()} está saindo de '{localAtual.getNome()}' para {destino.getNome()}\n===============================================================================================")


#Verifica se o usuário quer continuar no local
def continuarLocal(pessoa):
    decisao = pessoa.getDecisao([True, False])
    if decisao:
        print(f"\n-> {pessoa.getNome()} Decidiu ficar no Local\n===============================================================================================")
        
    return decisao


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