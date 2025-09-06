#Titulo
print('Dias da semana')

#Lista dias da semana
DiasDaSemana = ['Segunda','terça','Quarta','Quinta','Sexta','Sábado','Domingo']

#iniciador
NumeroSemana = -1



while NumeroSemana <= 7:
    NumeroSemana = int(input('Digite um número de 1 a 7 para saber o dia da semana correspondente: '))
    
    print(f'O dia da semana correspondente ao número {NumeroSemana} é {DiasDaSemana[NumeroSemana -1]}')

print('Número inválido')
