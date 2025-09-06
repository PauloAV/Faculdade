#Calculadora de IMCa
#Autor:Paulo Augusto de Jesus Vilela RGM:11251505301
#iniciador
pergunta = 's'
while pergunta == 's':
    #Entrada de dados 
    peso= float(input('Digite seu peso (Kg): '))
    altura = float(input('Digite sua altura (m):'))
    idade = int(input('Digite sua idade:'))
    #Calculo do IMC
    imc= peso/ altura**2
    #Estrutura de dados composto encadeado
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        classificacao = 'Peso normal'
        
    elif imc >= 25 and imc < 30:
        classificacao = 'Sobrepeso'

    elif imc >= 30 and imc < 35:
        classificacao = 'Obesidade Grau I'

    elif imc >= 35 and imc < 40:
        classificacao = 'Obesidade grau II'
    else:
        classificacao = 'Obesidade grau III'
    #saida de dados
    print(f'\nSeu IMC é: {imc:.2f}')
    print(f'Classificação: {classificacao}')
    pergunta = str(input('Quer continuar [S/N]: '))


print("Fim")
