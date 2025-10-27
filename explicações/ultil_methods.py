'''
len(ler quantas chaves tem)
keys(ler quantos nomes de chave tem)
values(ler os valores que estao dentro das chaves, ex: x: 'y' | vai ler o "y")
items(ler as chaves e os valores, ou seja, values + keys)
setdefalut(adiciona valor mesmo sem a chave existir)

copy/shallow copy(copia so a parte superficial do codigo, ou seja, copia so ao valores, oque tem dentro dos valores nao copia, ele basicamente deixa
tudo no mesmo plano, exemplo
a = [[1, 2], [3, 4]])
b = a.copy()

b[0][0] = 99
print(a) [[99, 2] ...] eles são listas diferentes, mas compartilham os mesmos itens dentro

deepcopy(copia tudo e separa eles, ou seja, independente um do outro, exemplo
c = b.copy (exemplo de cima)
c[0][0] = 111
print(a) [[99, 2] ...] a ficou do jeito que tava, ou seja, independente
print(c) [[111, 2] ...] o valor de c mudou sou ele, nao os dois, ou seja com deep ele copia o formato porem se mudar o valor
so muda de quem mudou e o copy ou shallow copy se mudar o valor de um ele copia o formato e muda o valor para o ultimo colocado
)

get(obtem a chave direto sem usar "[]"
print(p1.get('chave aqui'))
pop(retorna o valor, porem apaga a chave, dois em um)
update(muda os valores da chave para novos, e a mesma coisa de voce mudar manualmente la em chaves ne
bom para 2 scripts diferente, se for so em um, da pra mudar manualmente)
'''
