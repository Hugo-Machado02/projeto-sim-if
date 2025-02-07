from rich.console import Console
from rich.table import Table
import random
import time
console = Console()

def interfaceGrafica(cidade):
    console.clear()
            
    # Criando tabela para o corredor principal
    corredor_table = Table(title="🚪 Corredor Principal", title_style="bold magenta")
    corredor_table.add_column("Número de Pessoas", justify="center", style="bold yellow")
    corredor_table.add_row(f"{random.randint(0, 20)}")
    console.print(corredor_table, justify="center")
    
    for i in range(4):  # 4 blocos fixos
        bloco_table = Table(title=f"🏢 Bloco {i+1}", title_style="bold cyan", show_lines=True)
        
        # Adicionando todas as 6 salas e o corredor
        for j in range(1, 7):
            bloco_table.add_column(f"🏠 Sala {j}", justify="center", style="bold green")
        bloco_table.add_column("🚪 Corredor", justify="center", style="bold red")

        # Adicionando valores aleatórios para cada sala (2 linhas de ocupação)
        bloco_table.add_row(*[str(random.randint(0, 10)) for _ in range(6)], str(random.randint(0, 15)))

        console.print(bloco_table, justify="center")

    time.sleep(1)
