somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheresvinte = 0
for p in range (1, 5):
    print ('---- Dados da {}ª pessoa! ----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        mulheresvinte += 1

mediaidade = somaidade / 4
print(' A media de idade das pessoas é {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos, e se chama {}'.format(maioridadehomem, nomevelho))
print('E tem {} mulheres menores de 20 anos'.format(mulheresvinte))