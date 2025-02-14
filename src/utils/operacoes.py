import random, time

def enviaLocal(pessoa, localAtual, ListaLocais):
    destino = pessoa.getDecisao(ListaLocais)
    localAtual.removePessoa(pessoa)
    destino.adicionaPessoa(pessoa)
    print(f"\n-> {pessoa.getNome()} está saindo de '{localAtual.getNome()}' para '{destino.getNome()}' \n===============================================================================================")


#Verifica se o usuário quer continuar no local
def continuarLocal(pessoa):
    return pessoa.getDecisao([True, False])


#Seleciona a Pessoa
def selecionaPessoa(pessoas):
    if isinstance(pessoas, list):
        return random.choice(pessoas)
    else:
        return pessoas
    



def imprimirCidade(cidade):
    while True:
        corredorPrincipal = cidade.getCorredor()
        blocos = cidade.getlistaBlocos()

        print(f"\n\nCidade: {cidade.getNome()}")
        print(f"->Corredor Principal -> {corredorPrincipal.getQuantidadePessoas()} Pessoas")
        
        for b in blocos:
            print(f"\t-> Bloco - {b.getNome()}")
            salas = b.getListaSalas()
            print(f"\t\t-> Corredor de Bloco: {b.getCorredor().getQuantidadePessoas()} Pessoas")
            for sala in salas:
                print(f"\t\t->{sala.getNome()}: {sala.getQuantidadePessoas()} Pessoas")
        time.sleep(1)