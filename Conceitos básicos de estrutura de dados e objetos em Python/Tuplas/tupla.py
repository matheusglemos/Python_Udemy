# Projeto em python 3 referente a aula 18 do Curso python da plataforma Udemy.

# Criação de uma tupla se dá pelo uso de '()' e esta estrutura é imutável.

# Criando tuplas
tupla_01 = (1,2,3,4,5,1,1,1,8)
tupla_02 = ('Matheus', 14,5,1997)

# Métodos básicos das tuplas

# Uso do método 'index' que serve para recuperar o índice do elemento passado como paramêtro

# resultado '4'
print(tupla_01.index(5))
# resultado '0'
print(tupla_02.index('Matheus'))

# Uso do método 'count' que serve para contar quantas vezes determinado elemento está se repetindo na tupla

# resultado '4'
print(tupla_01.count(1))
