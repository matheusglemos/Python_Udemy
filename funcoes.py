# Projeto em python 3 referente a aula 34 do Curso python da plataforma Udemy.

# Sintaxe de uma função
def nome_da_funcao(argumento_01,argumento_02):
    # Corpo da função

    # retorne o resultado desejado aqui
    return('alguma coisa')

# Para testarmos o resultado de uma função temos que usar o 'assert', no caso destes exemplos, a plataforma que utilizo já retorna o valor sem precisar usar esse teste.

# Função responsável por retornar um nome
def retorna_nome(nome):
    print(nome)
# resultado 'Meu nome é: João.'
print(retorna_nome('Meu nome é: %s.' % ('João')))


# Função responsável por somar 2 números
def adiciona_dois_numeros(numero_01,numero_02):
    return(numero_01 + numero_02)
# resultado '15'
print(adiciona_dois_numeros(8,7))


# Função responsável por dizer se um número é primo ou Função
def verifica_primo(numero):
    for i in range(2,numero):
        if(numero % i == 0):
            print('Não é primo!')
            break
    else:
        print('É primo!')
# resultado 'Não é primo!'
verifica_primo(33)
