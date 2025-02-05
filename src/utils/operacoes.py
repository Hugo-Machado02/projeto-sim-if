def enviaLocal(pessoa, localAtual, ListaLocais):
    if not continuarLocal(pessoa):
        destino = pessoa.getDecisao(ListaLocais)
        localAtual.removePessoa(pessoa)
        destino.adicionaPessoa(pessoa)


