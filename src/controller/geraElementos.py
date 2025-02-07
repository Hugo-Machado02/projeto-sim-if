from controller import criaCidade, criaPessoa, criaBloco
import time

#Realiza a criacão dos elementos para a simulacao
def cricacaoElementos(numeroBlocos, numeroSalas, numeroPessoas, maxPessoasCorredor, maxPessoasSalas):
    print("Gerando elementos...")
    blocos = criaBloco.geraBlocos(numeroBlocos, numeroSalas, maxPessoasCorredor, maxPessoasSalas)
    cidade = criaCidade.criacaoCidade(blocos)
    pessoas = criaPessoa.criacaoPessoas(numeroPessoas)
    time.sleep(1.5)   

    print("Inserindo Pessoas no Corredor Principal")
    cidade.getCorredor().incluiPessoas(pessoas)
    time.sleep(1.5)

    return cidade