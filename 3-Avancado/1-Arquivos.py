"""
Trabalhando com arquivos

# Comandos em linha de comando
# Mostra em que pasta você está
pwd

# Criando um arquivo
%%writefile arquivo.ext
Conteuto
"""

# Abrindo um arquivo no Python
arquivo = open('arquivo.ext')

# Lendo uma linha do arquivo. Após a leitura, o cursor passa para alinha seguinte
linha = arquivo.readline()

# Lendo todo o arquivo a partir de onde está o cursor
conteudo = arquivo.read()

# Voltando o cursor para o inicio
arquivo.seek(0)
