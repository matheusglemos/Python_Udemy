# Projeto em python 3 referente a aula 27 do Curso python da plataforma Udemy.

# if : se
# elif : se não se
# else : caso não

mes = 'julho'
cont = 0

if(mes == 'janeiro'):
    cont += 1
    print('mês = %i' % cont)
elif(mes == 'fevereiro'):
    cont += 2
    print('mês = %i' % cont)
elif(mes == 'marco'):
    cont += 3
    print('mês = %i' % cont)
elif(mes == 'abril'):
    cont += 4
    print('mês = %i' % cont)
elif(mes == 'maio'):
    cont += 5
    print('mês = %i' % cont)
elif(mes == 'junho'):
    cont += 6
    print('mês = %i' % cont)
elif(mes == 'julho'):
    cont += 7
    print('mês = %i' % cont)
elif(mes == 'agosto'):
    cont += 8
    print('mês = %i' % cont)
elif(mes == 'setembro'):
    cont += 9
    print('mês = %i' % cont)
elif(mes == 'outubro'):
    cont += 10
    print('mês = %i' % cont)
elif (mes == 'novembro'):
    cont += 11
    print('mês = %i' % cont)
elif(mes == 'dezembro'):
    cont += 12
    print('mês = %i' % cont)
else:
    print("Mês inválido.")
