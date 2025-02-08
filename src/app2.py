from models.CorredorPrincipal import CorredorPrincipal
from models.Pessoa import Pessoa

corredor = CorredorPrincipal("Corredor Principal", 40)

# Criando algumas pessoas
pessoa1 = Pessoa("Alice", "Sobrenome 1", "Natural")
pessoa2 = Pessoa("Alysson", "Sobrenome 1", "Natural")

# Adicionando ao corredor
corredor.adicionaPessoa(pessoa1)
corredor.adicionaPessoa(pessoa2)

# Simulando a escolha das pessoas e enviando para outra cidade (se aplicável)
outra_cidade_url = "10.8.0.2:5000"  # IP da outra cidade na VPN
corredor.processarPessoas(outra_cidade_url)

print(f"Pessoas na cidade: {corredor.getListaPessoas()}")