# Projeto em python 3 referente a aula 12 do Curso python da plataforma Udemy.

# Objetos
nome_01 = "matheus"
nome_02 = "PALOMA"
nome_completo = "Matheus Gusmão Lemos"
idade_01 = 21
idade_02 = 22

# Formatação de saída simples - 'print'

# resultado 'matheus'
print(nome_01)
# resultado 'Matheus Gusmão Lemos'
print(nome_completo)

# Formatação usando o %s na saída

# resultado 'Meu nome é: Matheus Gusmão Lemos'
print('Meu nome é: %s' % (nome_completo))
# resultado 'Meu primeiro nome é: matheus'
print('Meu primeiro nome é: %s' % (nome_01))

# Formatação com números ponto flutuantes (decimais)

# Os números de ponto flutuante usam o formato %n1.n2f onde o n1 é o número mínimo total de dígitos que a cadeia deve conter.
# O espaço reservado n2 significa quantos números para mostrar após o ponto decimal.

# resultado 'Número ponto flutuante: 13.14'
print('Número ponto flutuante: %1.2f' % (13.144))
# resultado 'Número ponto flutuante: 13'
print('Número ponto flutuante: %1.0f' % (13.144))
# resultado 'Número ponto flutuante: 13.14400'
print('Número ponto flutuante: %1.5f' % (13.144))
# resultado 'Número ponto flutuante:      13.14'
print('Número ponto flutuante: %10.2f' % (13.144))
# resultado 'Número ponto flutuante:                     13.14'
print('Número ponto flutuante: %25.2f' % (13.144))

# Formatação múltipla

# resultado 'Meu nome é matheus e eu tenho 21 anos.'
print('Meu nome é %s e eu tenho %i anos.' % (nome_01,idade_01))
# Usando o método 'lower' para deixar o nome em letras minúsulas na saída.
# Se usasse o método 'upper' para deixar as letras maiúsculas na saída, também funcionaria.
# resultado 'Meu nome é paloma e eu tenho 22 anos.'
print('Meu nome é %s e eu tenho %i anos.' % (nome_02.lower(),idade_02))
# resultado 'Meu nome é matheus tenho 21 anos, estudo ciência da computação na UFCG.'
print('Meu nome é %s tenho %i anos, estudo %s na %s.' % (nome_01, idade_01,'ciência da computação', 'ufcg'.upper()))

# Usando o método '.format' na saída da impressão, abaixo a sintaxa deste método

# 'String aqui {var1} e também {var2}'.format(var1 = 'something1', var2 = 'something2')

# resultado 'Meu nome é Matheus Gusmão Lemos e tenho 21 anos'
print('Meu nome é {a} e tenho {b} anos'.format(a = nome_completo, b = idade_01))
# resultado 'Me chamo matheus e namoro com uma garota chamada paloma à 2 anos.'
print('Me chamo {a} e namoro com uma garota chamada {b} à {c} anos.'.format(a = nome_01, b = nome_02.lower(), c = 2))
