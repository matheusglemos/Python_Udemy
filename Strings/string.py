# Projeto em python 3 referente a aula 10 do Curso python da plataforma Udemy.

# Objetos
nome_01 = "matheus"
nome_02 = "PALOMA"
nome_completo = "Matheus Gusmão Lemos"

# Indexação de strings - '[]'
# O índice em python começa em 0

# Acessando o caractere inicial da string '[0]', resultado 'm'
print(nome_01[0])
# Acessando o segundo caractere da string '[1]', resultado 'a'
print(nome_01[1])
# Acessando o último caractere da string '[len(string)-1]', resultado 's'
print(nome_01[len(nome_01)-1])
# Acessando todos os elementos da string após o índice 1, resultado 'atheus'
print(nome_01[1:])
# Acessando todos os elementos até o índice 3, resultado 'mat'
print(nome_01[:3])
# Acessando todos os elementos até a ultima letra, resultado 'matheu'
print(nome_01[:-1])
# Acessando todos os elementos com um intervalo de 2 em 2 caracteres, resultado 'mtes'
print(nome_01[::2])
# Acessando todos os elementos de trás para frente, resultado 'suehtam'
print(nome_01[::-1])

# Usando método para deixar letras maiúsculas - '.upper'

# Impressão em letras normais
print(nome_01)
# Impressão em letras maiúsculas
print(nome_01.upper())

# Usando método para deixar letras minúsculas - '.lower'

# Impressão em letras normais
print(nome_02)
# Impressão em letras minúsculas
print(nome_02.lower())

# Usando método para dividir uma string - '.split'

# Usando o método sem argumento
# A string será dividida onde existir espaços, como o nome_completo tem 2 espaços
# o resultado será 3 strings. ["Matheus", "Gusmão", "Lemos"]
print(nome_completo.split())
# Usando o método com argumento
# A string será dividida onde existir o que for inserido como argumento, no caso,
# optei pelo caractere 'o', sendo assim, o resultado obtido. ["Matheus Gusmã", "Lem", "s"]
print(nome_completo.split("o"))

# Usando método para adicionar objetos formatados a instruções de impressão - '.format'

# resultado 'Paloma namora com Matheus à 2 anos.'
print('Paloma {}'.format('namora com matheus à 2 anos.'))
