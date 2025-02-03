from controller import criaCidade, criaBloco, criaSalas, criaPessoa

#Realiza a criacão dos elementos para a simulacao
def cricacaoElementos(numeroBlocos, numeroSalas, numeroPessoas):

    blocos = criaBloco.geraBlocos(numeroBlocos, numeroSalas)
    cidade = criaCidade.criacaoCidade(blocos)
    pessoas = criaPessoa.criacaoPessoas(numeroPessoas)

    for p in pessoas:
        cidade.getCorredor().adicionaPessoa(p)
        print(f"{p.getNome()} Entrando no corredor da cidade - {cidade.getNome()}")
    return cidade