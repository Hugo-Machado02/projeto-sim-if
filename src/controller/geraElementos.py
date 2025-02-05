from controller import criaCidade, criaSalas, criaPessoa, criaBloco

#Realiza a criacão dos elementos para a simulacao
def cricacaoElementos(numeroBlocos, numeroSalas, numeroPessoas):
    blocos = criaBloco.geraBlocos(numeroBlocos, numeroSalas)
    cidade = criaCidade.criacaoCidade(blocos)
    pessoas = criaPessoa.criacaoPessoas(numeroPessoas)
    cidade.getCorredor().incluiPessoas(pessoas)

    return cidade