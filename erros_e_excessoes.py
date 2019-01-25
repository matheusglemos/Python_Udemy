# Projeto em python 3 referente a aula 54

'''

# Sintaxe do try/except
try:
       Você tenta fazer algo aqui...
       ...
    except ExceptionI:
       Se causar a ExceptionI, roda isso.
    except ExceptionII:
       Se causar a ExceptionII, roda isso.
       ...
    else:
        Se não causar excessões, roda isso.

 '''

# código que abre e grava um arquivo.
# resultado 'Conteudo escrito com sucesso'
try:
    f = open('testfile','w')
    f.write('Escrevendo um teste aqui')
except IOError:
    # Isso só irá verificar se há uma exceção IOError e, em seguida, executar esta declaração de impressão
   print("Erro: Não foi possível encontrar o arquivo ou ler os dados")
else:
   print("Conteudo escrito com sucesso")
   # fecha o arquivo
   f.close()

# código que abre e lê um arquivo.
# O erro será encontrado neste trecho de código pois o arquivo está com permissões apenas de leitura e não de escrita, sendo assim, não podera escrever ocasionando um erro.
# resultado 'Erro: Não foi possível encontrar o arquivo ou ler os dados'
try:
    f = open('testfile','r')
    f.write('Escrevendo um teste aqui')
except IOError:
    # Isso só verificará uma exceção IOError e, em seguida, executará essa instrução print
   print("Erro: Não foi possível encontrar o arquivo ou ler os dados")
else:
   print("Conteudo escrito com sucesso")
   # fecha o arquivo
   f.close()

# código que abre e lê um arquivo.
# O erro será encontrado neste trecho de código pois o arquivo está com permissões apenas de leitura e não de escrita, sendo assim, não podera escrever ocasionando um erro.
# resultado 'Erro: Não foi possível encontrar o arquivo ou ler os dados'
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
   # Neste caso não declarei o possivel erro, mas deixei em aberto, servindo para qualquer classe de erro.
   print("Erro: Não foi possível encontrar o arquivo ou ler os dados")
else:
   print("Conteudo escrito com sucesso")
   # fecha o arquivo
   f.close()


# FINALLY

'''

# sintaxe do try/finally.
try:
   Seu código aqui
   ...
   Devido a qualquer exceção, este código pode ser ignorado!
finally:
   Este bloco de código sempre seria executado.

'''

# código que abre e escreve em um arquivo.
# resultado 'Sempre executa blocos de código finally'
try:
   f = open("testfile", "w")
   f.write("Escrevendo uma declaração de teste")
finally:
   print("Sempre executa blocos de código finally")

# funcão
# podemos usar finally em conjunto com except
def askint():
  try:
    val = int(raw_input("Entre um inteiro: "))
  except:
    print("Parece que você não digitou um inteiro")

  finally:
    print("Executei!")
  print(val)

# resultado ' Parece que você não digitou um inteiro
#             Executei!'
askint()

# função
# podemos usar finally em conjunto com except
def askint1():
        try:
            val = int(raw_input("Por favor entre com um inteiro: "))
        except:
            print("Parece que você não inseriu um inteiro!")
            val = int(raw_input("Tente novamente - Por favor insira um inteiro: "))
        finally:
            print("Finally, eu sou executado!")
        print(val)

# resultado 'Parece que você não inseriu um inteiro!
#            Finally, eu sou executado!'
askint1()

# continuando a verificação.
# função
# podemos usar finally em conjunto com except
def askint2():
    while True:
        try:
            val = int(raw_input("Por favor insira um inteiro: "))
        except:
            print("Parece que você não inseriu um inteiro!")
            continue
        else:
            print('Sim, isso é um número inteiro!')
            break
        finally:
            print("Finally, eu sou executado!")
        print(val)
