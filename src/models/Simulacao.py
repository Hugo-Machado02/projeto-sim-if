import time
class Simulacao:

    def __init__(self, tempo, listaPessoas, listaSalas):
        self.tempo = tempo
        self.listaPessoas = listaPessoas
        self.listaSalas = listaSalas

    def iniciaSimulacao(self):
        tempoInicial = time.time()
        while time.time() - tempoInicial < self.tempo:
            print(f"Contagem: {time.time() - tempoInicial}")
            for i in self.listaPessoas:
                print(i.getNome())
                time.sleep(1)
            for i in self.listaSalas:
                print(i.getNome())
                time.sleep(1)
            print("\n\n\n")
        time.sleep(2)
