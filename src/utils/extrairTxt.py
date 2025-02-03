def lerTXT(arquivoTXT):
    with open(arquivoTXT, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    print(linhas)
