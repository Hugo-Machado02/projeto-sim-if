from controller import criaCidade, criaPessoa, criaBloco
import time

#Realiza a criacão dos elementos para a simulacao
def cricacaoElementos(numeroBlocos, numeroSalas, numeroPessoas, maxPessoasCorredor, maxPessoasSalas):
    blocos = criaBloco.geraBlocos(numeroBlocos, numeroSalas, maxPessoasCorredor, maxPessoasSalas)
    cidade = criaCidade.criacaoCidade(blocos)
    pessoas = criaPessoa.criacaoPessoas(numeroPessoas)
    cidade.getCorredor().incluiPessoas(pessoas)

    return cidade