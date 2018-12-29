# Projeto em python 3 referente a aula 19 do Curso python da plataforma Udemy.

# Primeiro criei um arquivo .txt na pasta correspondente a aula de arquivos para poder ter acesso a mesma.

# Abrindo um arquivo
dados = open('teste.txt')

# Lendo um arquivo, resultado 'Este eh o texto que sera usado para testes na aula de arquivos.'
print(dados.read())
print ('-----')

# Tentando ler um arquivo sem resetar seu cursor, resultado 'linha vazia'
print(dados.read())
print ('-----\n')

# Usando o metodo 'seek' para mover o cursor para o inicio do texto
dados.seek(0)

# Exibindo o arquivo txt novamente apos mover o cursor, resultado 'Este eh o texto que sera usado para testes na aula de arquivos.'
print(dados.read())

# Usando o metodo 'seek' para mover o cursor para o indice 6 do texto
dados.seek(6)

# Exibindo o arquivo txt novamento apos mover o cursor, resultado 'h o texto que sera usado para testes na aula de arquivos.'
print(dados.read())

# Exibindo o arquivo txt usando o metodo 'readlines' que retorna uma lista com todas as linhas contidas no arquivos
dados.seek(0)
print(dados.readlines())

# Iterando sobre arquivos

dados_01 = open("text.txt")

# Usando estrutura for de repeticao para iterar sobre o objeto 'dados_01'
for i in dados_01:
    print(i)
