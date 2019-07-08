"""
Trabalhando com arquivos

# Comandos em linha de comando
# Mostra em que pasta você está
pwd

# Criando um arquivo (comando do jupyter)
%%writefile arquivo.ext
Conteuto
"""

# Abrindo um arquivo no Python
arquivo = open('arquivo.txt')

# Lendo uma linha do arquivo. Após a leitura, o cursor passa para alinha seguinte
linha = arquivo.readline()

# Lendo todo o arquivo a partir de onde está o cursor
conteudo = arquivo.read()

# Voltando o cursor para o inicio (o parametro informa o caracter onde o cursor deve parar
arquivo.seek(0)

# Lendo o arquivo de texto com laço de repeticão
for linha in arquivo:
    print(linha)

