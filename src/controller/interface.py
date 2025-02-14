from rich.console import Console
from rich.table import Table
import time, os
from dotenv import load_dotenv

load_dotenv()
NUM_BLOCOS = str(os.getenv("NUM_BLOCOS"))
NUM_SALAS = str(os.getenv("NUM_SALAS"))
NUM_PESSOAS = str(os.getenv("NUM_PESSOAS"))

console = Console()

def interfaceGrafica(cidade):
    dadosGerados = [NUM_PESSOAS, NUM_BLOCOS, NUM_SALAS]
    PessoasCorredorPrincipal = cidade.getCorredor()
    Blocos = cidade.getlistaBlocos()
    
    while True:
        console.clear()
        
        #Gerando a tabela para os dados Gerados
        geracaoDados = Table(title=f"{cidade.getNome()}", title_style="bold cyan", show_lines=True)
        geracaoDados.add_column("Pessoas Criadas", justify="center", style="bold yellow")
        geracaoDados.add_column("Blocos gerados", justify="center", style="bold yellow")
        geracaoDados.add_column("Salas Geradas", justify="center", style="bold yellow")
        geracaoDados.add_row(*[i for i in dadosGerados])

        console.print(geracaoDados, justify="center")

        #Gerando a tabela para o Corredor Principal
        CorredorPrincipal = Table(title="IF Goiano - Campus Morrinhos", title_style="bold cyan", show_lines=True)
        CorredorPrincipal.add_column("🚪 Corredor Principal", justify="center", style="bold yellow")
        CorredorPrincipal.add_row(str(PessoasCorredorPrincipal.getQuantidadePessoas()))
        console.print(CorredorPrincipal, justify="center")
        
        #Gerando a tabela para os Blocos e Salas
        for bloco in Blocos:  # 4 blocos fixos
            blocoDados= Table(title=f"🏢 Bloco {bloco.getNome()}", title_style="bold cyan", show_lines=True)

            dadosSalas = []
            
            for sala in bloco.getListaSalas():
                dadosSalas.append(sala.getQuantidadePessoas())
                blocoDados.add_column(f"🏠 Sala {sala.getNome()}", justify="center", style="bold green")
            blocoDados.add_column("🚪 Corredor", justify="center", style="bold red")
            dadosSalas.append(bloco.getCorredor().getQuantidadePessoas())


            blocoDados.add_row(*[str(i) for i in dadosSalas])

            console.print(blocoDados, justify="center")
        time.sleep(1)
