'''
tipos de expressoes numericas

adição -> +
subtração -> -
multiplicação -> *
divisão -> /
divisão inteira -> //
potenciação -> **
módulo -> %
precedência de operadores -> (), **, *, /, //, %, +, -

% (módulo) -> resto da divisão
como funciona o módulo?
7 % 4 -> 3
deu esse resultado porque 4 cabe 1 vez em 7 e sobra 3

como saber se um número é par ou ímpar?
n1 = 1
n2 = 2
n1 % 2 -> 1 (ímpar)
n2 % 2 -> 0 (par)

repeticao de algo

repeticao = 'A' * 5
print(repeticao)

concatenacao de strings

concatenacao = 'a' + 'b' + 'c'
print(concatenacao)
'''

n1 = 1
n2 = 2

if n1 % 2 == 0:
    print(f'{n1} é par')
else:
    print(f'{n1} é ímpar')

if n2 % 2 == 0:
    print(f'{n2} é par')
else:
    print(f'{n2} é ímpar')

      
'''
precedencia de operadores
maior para menor:
(), **, *, /, //, %, +, -

formatação de strings
f'{variavel}'
f'{variavel:.2f}' -> 2 casas decimais
.format(variavel)
formato = 'a{} b{} c{}'.format(a, b, c)
se quiser colocar quantidade de casas decimais
formato = 'a{:.2f} b{:.3f} c{:.4f}1.format(a, b, c)

parametro nomeado
formato = 'a{nome} b{nome2} c{nome3}'.format(nome=a, nome2=b, nome3=c)
oque eu nomear dentro do () tem que ser colocado no {}

'''