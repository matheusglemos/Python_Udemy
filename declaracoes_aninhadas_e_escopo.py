# Projeto em python 3 referente a aula 37 do Curso python da plataforma Udemy.

# Exemplo sobre escopo 
x = 25

def printer():
    x = 50
    return x

# resultado '25', pois se trata da variavel x criada na linha 4,
print(x)
# resultado '50' pois representa o x atribuido a chamada da função 'printer'
print(printer())


# Exemplo sobre escopo utilizando de funções aninhadas
name = 'variavel global'

def hello():
    name = 'Matheus'

    def hello():
        print('Hello, '+name)

    hello()

# resultado 'Hello, Matheus', se trata de uma variavel local(dentro da função)
hello()
# resultado 'variavel global'
print(name)

# Exemplo sobre escopo utilizando variaveis locais
x = 50

def func(x):
    print('x globalmente vale', x)
    x = 2
    print('Localmente x vale', x)

# resultado 'x globalmente vale 50'
#           'Localmente x vale 2'
func(x)
# resultado 'Fora da função x vale 50'
print('Fora da função x vale', x)

# Exemplo sobre escopo utilizando 'global' nas variaveis dentro da função para alterar o valor global de uma variavel
x = 50

def func():
    global x
    print('Esta função está usando o valor global x!')
    print('Por causa da variavel global o valor de x é:', x)
    x = 2
    print('Rodando a função, o valor global de x passa a ser', x)

# resultado 'Antes de chamar a função, x é: 50'
print('Antes de chamar a função, x é:', x)
# resultado 'Esta função está usando o valor global x!'
#           'Por causa da variavel global o valor de x é: 50'
#           'Rodando a função, o valor global de x passa a ser 2'
func()
# resultado 'Valor de x após a chamada da função: 2'
print('Valor de x após a chamada da função:', x)
