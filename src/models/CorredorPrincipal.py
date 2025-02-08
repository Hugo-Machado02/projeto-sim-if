from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, imprimirCidade
from dotenv import load_dotenv
import time, os, requests

load_dotenv()
DELAY = float(os.getenv("TEMPO_DELAY"))

class CorredorPrincipal(Corredor):

    def __init__(self, nome, capacidade):
        super().__init__(nome, capacidade)

    def incluiPessoas(self, listaPessoas):
        for pessoa in listaPessoas:
            self.adicionaPessoa(pessoa)

    # Implementação do método abstrato
    def executaCorredor(self, listaDestinos):
        while True:
            pessoas = self.getListaPessoas()
            if pessoas:
                for pessoa in pessoas:
                    if not continuarLocal(pessoa):
                        enviaLocal(pessoa, self, listaDestinos)
                        
                    time.sleep(DELAY)
            else:
                break
            
    def processarPessoas(self, url_cidade=None):
        pessoas = self.getListaPessoas()
        
        for pessoa in pessoas[:]:
            if pessoa.decisaoSaida():
                print(f"{pessoa.getNome()} decidiu sair da cidade.")
                if url_cidade:
                    if self.enviarParaCidade(pessoa, url_cidade)
                    self.removePessoa(pessoa)
            else:
                print(f"{pessoa.getNome()} decidiu ficar na cidade.")

    def enviarParaCidade(self, pessoa, url_cidade):
        try:
            response = requests.post(f"http://{url_cidade}/receberPessoa", json={"nome": pessoa.getNome()})
            if response.status_code == 200:
                print(f"{pessoa.getNome()} foi enviado para outra cidade.")
            else:
                print(f"Falha ao enviar {pessoa.getNome()}.")
        except Exception as e:
            print(f"Erro ao enviar {pessoa.getNome()}: {e}")