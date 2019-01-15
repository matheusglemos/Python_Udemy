# Projeto em python 3 referente a aula 36 do Curso python da plataforma Udemy.

# Observar que a função 'square' pode ser escrita de 3 formas, uma mais simplificada que a outra.

# forma 01
def square(num):
    result = num**2
    return result

# forma 02
def square(num):
    return num**2

# forma 03
def square(num): return num ** 2

# resulrado '4'
print(square(2))


# Usando expressões lambda para a mesma função

# resultado '9'
square = lambda num: num**2
print(square(3))

# Expressão lambda que verifica se o número é par
par = lambda x: x % 2 == 0
# resultado 'True'
print(par(4))

# Expressão lambda que retorna o primeiro caractere de uma string
first = lambda s: s[0]
# resultado 'M'
print(first('Matheus'))

# Expressão lambda que inverte uma string
rev = lambda s: s[::-1]
# resultado 'suehtam'
print(rev('Matheus'))
