# Projeto em python 3 referente a aula 14 do Curso python da plataforma Udemy.

# objetos
lista_01 = ['m','a','t','h','e','u','s']
lista_02 = [1,2,3,4,5,6,7,8,9]
lista_03 = [1,44,516,133,67,-3]
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
lista_aninhada = [lst_1,lst_2,lst_3]

# Indexação e corte

# Pega o elemento de índice 0, resultado 'm'
print(lista_01[0])
# Pega o último elemento, resultado 's'
print(lista_01[len(lista_01)-1])
# Pega tudo a partir do índice 1, resultado ['a','t','h','e','u','s']
print(lista_01[1:])
# Pega tudo até o quarto elemento, resultado ['m','a','t','h']
print(lista_01[:4])

# Atribuindo permanentemente elementos a uma lista_01 com '+'

# resultado '['m','a','t','h','e','u','s','g']'
lista_01 = lista_01 + ['g']
# resultado '[1,2,3,4,5,6,7,8,9,10]'
lista_02 = lista_02 + [10]

# Atribuindo permanentemente elementos a uma lista usando o método 'append'

# resultado '['m','a','t','h','e','u','s','g','u']'
lista_01.append('u')
print(lista_01)
# resultado '[1,2,3,4,5,6,7,8,9,10,11]'
lista_02.append(11)
print(lista_02)

# Removendo elementos da lista usando o método 'pop'

# Método sem parametro, retira o ultimo elemento da lista
# resultado '['m','a','t','h','e','u','s','g']'
lista_01.pop()
print(lista_01)
# Método com parametro, irá remover o elemento do índice indicado
# resultado '[3,4,5,6,7,8,9,10,11]'
lista_02.pop(0)
lista_02.pop(0)
print(lista_02)

# Ordenando uma lista com o método 'sort'

# resultado '[-3,1,44,67,133,516]'
lista_03.sort()
print(lista_03)

# Revertendo uma lista usando o método 'reverse'

# resultado '[11,10,9,8,7,6,5,4,3]'
lista_02.reverse()
print(lista_02)

# Listas aninhadas(Matrizes)

# Acessando o elemento de índice 0 da lista_aninhada, resultado '[1,2,3]'
print(lista_aninhada[0])
# Acessando o elemento de índice 0 da Matriz, resultado '1'
print(lista_aninhada[0][0])
