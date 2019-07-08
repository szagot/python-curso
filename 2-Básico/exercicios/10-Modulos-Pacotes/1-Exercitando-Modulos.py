from modulos import moeda, dados

valor = dados.leia_dinheiro('Digite o preço: R$ ')
moeda.resumo(valor, 12, 20)
