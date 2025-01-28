from models.Simulacao import Simulacao
from controller import criaPessoa, criaSalas
from dotenv import load_dotenv
import os

load_dotenv()
NUM_BLOCOS = int(os.getenv("NUM_BLOCOS"))
NUM_SALAS = int(os.getenv("NUM_SALAS"))
NUM_PESSOAS = int(os.getenv("NUM_PESSOAS"))
TEMPO_EXECUCAO = int(os.getenv("TEMPO_EXECUCAO"))

print(f"Teste -> Blocos: {NUM_BLOCOS}; Salas: {NUM_SALAS}; Pessoas: {NUM_PESSOAS}; Execucao: {TEMPO_EXECUCAO};" )

salas = criaSalas.criacaoSalas(NUM_SALAS)

pessoas = criaPessoa.criacaoPessoas(NUM_PESSOAS)

sim = Simulacao(TEMPO_EXECUCAO, pessoas, salas)

sim.iniciaSimulacao()
print("Fim da simulação!")