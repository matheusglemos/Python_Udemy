# Projeto em python 3 referente a aula 31 do Curso python da plataforma Udemy.

# Pega todas as letras em uma string e exibe-a em seguida
lista = [x for x in 'word']
print(lista)

# Eleva o quadrado itens no range e o transformam em lista
# resultado '[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'
lst = [x**2 for x in range(0,11)]
print(lst)

# Cria uma lista de números pares, utilizando para isso o if
# resultado '[0, 2, 4, 6, 8, 10]'
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

# Converte Celsius para Fahrenheit
# resultado '[32.0, 50.0, 68.18, 94.1]'
celsius = [0,10,20.1,34.5]

fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius]
print(fahrenheit)

# Também podemos realizar compreensões de lista aninhadas

# resultado '[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]'
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)
