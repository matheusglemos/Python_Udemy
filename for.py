# Projeto em python 3 referente a aula 28 do Curso python da plataforma Udemy.

# Objeto
l = [1,2,3,4,5,6,7,8,9,10]

# Iteração utilizando 'for'

# resultado :
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
for num in l:
    print(num)

# Iteração utilizando 'for' e operador '%'

# resultado :
# Número ímpar
# 2
# Número ímpar
# 4
# Número ímpar
# 6
# Número ímpar
# 8
# Número ímpar
# 10
for num in l:
    # Condição: Se o número for par exiba-o, caso não exibir 'Número ímpar'
    if num % 2 == 0:
        print(num)
    else:
        print('Número ímpar')

# Somando todos os valores da lista em uma variavel auxiliar

# resultado '55'
list_sum = 0

for num in l:
    list_sum += num

print(list_sum)

# Iterando utilizando 'for' em uma string

# resultado:
# T
# h
# i
# s
#
# i
# s
#
# a
#
# s
# t
# r
# i
# n
# g
#.
for letter in 'This is a string.':
    print(letter)

# Iterando utilizando 'for' em uma Tupla

# resultado:
# 1
# 2
# 3
# 4
# 5
tup = (1,2,3,4,5)

for t in tup:
    print(t)

# resultado :
# (2, 4)
# (6, 8)
# (10, 12)
l = [(2,4),(6,8),(10,12)]
for tup in l:
    print(tup)

# Agora desembalando
# resultado:
# 2
# 6
# 10
for (t1,t2) in l:
    print(t1)

# Iterando sobre um dicionário com a estrutura 'for'

d = {'k1':1,'k2':2,'k3':3}

# Só itera sobre as chaves do dicionário
# resultado:
# k3
# k2
# k1
for item in d:
    print(item)
# Para iterarmos sobre os valores do dicionario precisamos usar o método '.items()'
# resultado : Tuplas contendo chaves e seus valores associados ao dicionario
for item in d.items():
    print(item)
# Para iterarmos sobre os valores do dicionario precisamos usar o método '.items()'
# resultado : valores associados às chaves do dicionario
for i,j in d.items():
    print(j)
