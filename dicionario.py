# Projeto em python 3 referente a aula 16 do Curso python da plataforma Udemy.

# Objetos
dados = {'nome':'Matheus','idade':'21','status':'namorando'}
d = {'anos':{'meses':{'dias':'minutos'}}}
dic_01 = {'chave_01':123,'chave_02':[12,23,33],'chave_03':['item0','item1','item2']}
dic_02 = {}

# Construindo um dicionário
# sintaxe = {"key":"value"}'

# Exibindo o valor associado a uma chave do meu dicionário, resultado '['item0','item1','item2']'
print(dic_01['chave_03'])
# Exibindo o valor associado ao índice 1 da chave 3 do dicionário, resultado 'item1'
print(dic_01['chave_03'][1])
# Exibindo saida usando métodos nos itens, resultado 'MATHEUS'
print(dados['nome'].upper())

# Alterando valores através das chaves

# Modificando o status de relacionamento, resultado 'casado'
dados['status'] = 'casado'
print(dados['status'])

# Criando chaves por atribuição

# Começando com um dicionário vazio, poderíamos adicionar-lhe continuamente, resultado '{'cachorro': 'ringo','raca': 'Pastor Alemão'}'
dic_02['cachorro'] ='ringo'
dic_02['raca'] ='Pastor Alemão'
print(dic_02)

# Aninhamento de dicionários

# Exibindo o valor 'MINUTOS' que está dentro do dicionário dias, o dicionário dias está dentro do dicionário meses, o dicionário meses está dentro do dicionario anos que por sua vez está dentro do dicionario dic_aninhados
# resultado 'MINUTOS'
print(d['anos']['meses']['dias'].upper())

# Métodos para dicionários

# Método 'keys', retorna uma lista com todas as chaves associadas ao dicionário

# resultado '['status','idade','nome']', OBS: dicionários não possuem ordem, já que os valores são associados as suas chaves e não à posições.
print(dados.keys())

# Método 'values', retorna uma lista com todos os valores associados ao dicionário

# resultado '['casado','21','Matheus']', OBS: dicionários não possuem ordem, já que os valores são associados as suas chaves e não à posições.
print(dados.values())

# Método 'itens', retorna tuplas de todos os itens (key,value)

# resultado '[('status', 'casado'),('idade', '21'),('nome', 'Matheus')]', OBS: dicionários não possuem ordem, já que os valores são associados as suas chaves e não à posições.
print(dados.items())
