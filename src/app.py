from models.Pessoa import Pessoa
from controller import criaPessoa, criaBloco
from dotenv import load_dotenv
import os
import time

load_dotenv()
NUM_BLOCOS = int(os.getenv("NUM_BLOCOS"))
NUM_SALAS = int(os.getenv("NUM_SALAS"))
NUM_PESSOAS = int(os.getenv("NUM_PESSOAS"))
TEMPO_EXECUCAO = int(os.getenv("TEMPO_EXECUCAO"))

print(f"Teste -> Blocos: {NUM_BLOCOS}; Salas: {NUM_SALAS}; Pessoas: {NUM_PESSOAS}; Execucao: {TEMPO_EXECUCAO};" )

bloco = criaBloco.geraBlocos(NUM_BLOCOS, NUM_SALAS)

pessoas = criaPessoa.criacaoPessoas(NUM_PESSOAS)

for p in pessoas:
    decisaoBloco = p.decisao(bloco)
    decisaoSala = p.decisao(decisaoBloco.getListaSalas())
    if decisaoSala.entrar(p):
        print(f'A {p.getNome()} Decidiu entrar no {decisaoBloco.getNome()} na {decisaoSala.getNome()}')
    else:
        decisaoBloco.getCorredor().adicionarPessoa(p)
        print(f"A Pessoa {p.getNome()} entrou no Corredor")
    time.sleep(1)

for i in bloco:
    print('\n\n---------------------')
    print(f"{i.getNome()}")
    salas = i.getListaSalas()
    print(f"-> Corredor = {len(i.getCorredor().getListaPessoas())} Pessoas")
    for x in salas:
        print(f"-> {x.getNome()} = {x.quantidadePessoas()} Pessoas")
        time.sleep(1)
        


# pessoas = criaPessoa.criacaoPessoas(NUM_PESSOAS)

# sim = Simulacao(TEMPO_EXECUCAO, pessoas, salas)

# sim.iniciaSimulacao()
print("Fim da simulação!")