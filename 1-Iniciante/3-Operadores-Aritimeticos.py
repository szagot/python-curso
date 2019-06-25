"""

+  Soma
-  Subtração
*  Multiplicação
/  Divisão
** Potência - pode-se usar a função pow(n, p). Exemplo: pow(5,2) é o mesmo que 5**2 (5 elevado ao quadrado)
// Divisão inteira
%  Módulo - sobra da divisão

Raiz quadrada: Basta potencializar frações.
Exemplo1: Raiz quadrada de 25 -> 25**(1/2)
Exemplo2: Raiz cúbica de 27 -> 27**(1/3)

Ordem de Precedência
1 - ()
2 - **
3 - *  /  //  %
4 - +  -

=====
Alguns operadores permitem serem usados com strings. Neste caso, muda para:
+  Concatena. Exemplo: 'Oi' + 'Olá' == 'OiOlá'
*  Repete a string pelo número multiplicado. Exemplo: 'Oi' * 2 == 'OiOi'

"""

# Exemplo de cada um dos operadores
som = 5 + 2
sub = 5 - 2
div = 5 / 2
mul = 5 * 2
exp = 5 ** 2
divInt = 5 // 2
mod = 5 % 2

print(
    (
            'Resultados de 5 e 2\n\n' +
            'Soma: {}\n' +
            'Subtração: {}\n' +
            'Divisão: {}\n' +
            'Multiplicação: {}\n' +
            'Exponenciação: {}\n' +
            'Divisão Inteira: {}\n' +
            'Sobra da Divisão: {}'
    ).format(som, sub, div, mul, exp, divInt, mod)
)
