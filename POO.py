# Projeto em python 3 referente a todo o módulo de Programação Orientada a Objetos


# OBJETOS

''' resultado:
 <class 'int'>
 <class 'list'>
 <class 'tuple'>
 <class 'dict'> '''
print(type(1))
print(type([]))
print(type(()))
print(type({}))


# CLASSES

# Criando um novo tipo de objeto chamado Sample
class Sample(object):
    pass

# Instanciando Sample
x = Sample()

# resultado ' <class '__main__.Sample'> '
print(type(x))


# ATRIBUTOS

# O self age como o this em C e Java
class Dog(object):
    # construtor da classe
    def __init__(self,raça):
        # aqui fala que o raça interno a classe será o raça que será inserido no construtor
        self.raça = raça

# instâncias da classe Dog
sam = Dog('Labrador')
frank = Dog('Huskie')

# resultado 'Labrador'
print(sam.raça)
# resultado ' Huskie'
print(frank.raça)


# Classe referente a um Rato
class Rato(object):

  # atributos já definidos
  especie = 'Mamifero'
  sub_especie = 'Roedor'

  # construtor da classe Rato
  def __init__(self,raça,nome):
    self.raça = raça
    self.nome = nome

# instância da classe Rato
gus = Rato('Gabiru','Gus')

# resultado 'Gus'
print(gus.nome)
# resultado 'Gabiru'
print(gus.raça)
# resultado 'Mamifero'
print(gus.especie)
# resultado 'Roedor'
print(gus.sub_especie)


# MÉTODOS

# Classe responsavel por um círculo
class Circulo(object):

  # atributo que define pi como 3.14
  pi = 3.14

  # construtor de um circulo, raio definido como 1 caso não passe valores como parâmetros.
  def __init__(self,raio=1):
    self.raio = raio

  # Método responsavel por calcular a área de um circulo.
  def area(self):
    return self.raio ** 2 * Circulo.pi

  # Método capaz de redefinir o raio do circulo.
  def setraio(self,raio):
    self.raio = raio

  # Método responsavel por retornar o raio.
  def getraio(self):
    return self.raio

# Instância de circulo sem parâmetros, ou seja, raio = 1.
circulo01 = Circulo()

# resultado '3.14'
print(circulo01.area())
# resultado '1'
print(circulo01.getraio())

# Setando valor de raio = 2.
circulo01.setraio(2)

# resultado '12.56'
print(circulo01.area())
# resultado '2'
print(circulo01.getraio())


# HERANÇA

# classe referente a um Animal
class Animal(object):

  # construtor da classe Animal
  def __init__(self):
    print('Animal criado')

  # Método referente a quem eu sou, printando 'Animal'
  def quem_sou(self):
    print('Animal')

  # Método responsavel por comer, printando 'Comendo...'
  def comendo(self):
    print('Comendo...')

# classe referente a um Cachorro, que extende da classe Animal, já que todo Cachorro é um Animal
class Cachorro(Animal):

  # construtor da classe Cachorro, aqui se extende os demais métodos da classe Animal
  def __init__(self):
    Animal.__init__(self)
    print('Cachorro criado')

  # Método de sobreescrita para definir quem eu sou, printando 'Cachorro'
  def quem_sou(self):
    print('Cachorro')

  # Método acrescentado que faz o Cachorro latir.
  def latindo(self):
    print('Woof!')

# resultado ' Animal criado
#             Cachorro criado'
hulk = Cachorro()
# resultado 'Comendo...'
hulk.comendo()
# resultado 'Woof!'
hulk.latindo()
# resultado 'Cachorro'
hulk.quem_sou()


# MÉTODOS ESPECIAIS

# classe referente a um Livro
class Livro(object):

  # construtor da classe Livro, passando como parâmetros, titulo, autor e páginas.
  def __init__(self,titulo,autor,paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

  # Método similar a o len() que retorna a quantidade de páginas do Livro em questão.
  def __len__(self):
    return self.paginas

  # Método similar ao toString() em outras linguagens, retorna a representação textual do Livro.
  def __str__(self):
    return 'Titulo: %s, Autor: %s, Páginas: %i' % (self.titulo,self.autor,self.paginas)

  # Método capaz de deletar o Livro.
  def __del__(self):
    print('Livro destruido')

# instância de um Livro
hp = Livro('Harry Potter', 'J.K.Rowling', 600)

# resultado '600'
print(len(hp))
# resultado ' Titulo: Harry Potter, Autor: J.K.Rowling, Páginas: 600'
print(hp)
# resultado 'Livro destruido', O livro deixa de existir e para usar os métodos só com uma nova instância.
del hp
