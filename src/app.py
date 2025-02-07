from controller.geraElementos import cricacaoElementos
from controller.criaPessoa import criacaoPessoas
from utils.operacoes import imprimirCidade
from dotenv import load_dotenv
import os
import time

#Carrega Variaveis de ambiente
load_dotenv()
NUM_BLOCOS = int(os.getenv("NUM_BLOCOS"))
NUM_SALAS = int(os.getenv("NUM_SALAS"))
NUM_PESSOAS = int(os.getenv("NUM_PESSOAS"))
TEMPO_EXECUCAO = int(os.getenv("TEMPO_EXECUCAO"))

cidade = cricacaoElementos(NUM_BLOCOS, NUM_SALAS, NUM_PESSOAS)
cont = 1
listaPersonalizada = []
listaPersonalizada2 = []
for bloco in cidade.getlistaBlocos():
    listaPersonalizada.append(bloco)

corredorPrincipal = cidade.getCorredor()
timeInicial = time.time();

while time.time() - timeInicial < TEMPO_EXECUCAO:
    corredorPrincipal.executaCorredor(cidade, listaPersonalizada)

    for b in cidade.getlistaBlocos():
        for s in b.getListaSalas():
            listaPersonalizada2.append(s)
        listaPersonalizada2.append(cidade.getCorredor())
        b.execucaoBlocos(cidade, listaPersonalizada2)

imprimirCidade(cidade)
print("Fim da simulação!")