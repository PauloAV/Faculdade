#calculadora conta final hóspede
#Autores:Paulo Augusto de Jesus Vilela RGM:11251505301
#Autores:Vinicius Henrique Silva Bomfim RGM:11251104665
import math
print('-----------------------------------------')
print('Calculadora de conta final do hóspede')
print('-----------------------------------------')
#pergunta nome do hospede 
nome = str(input("Digite o nome do hóspede: ")).upper()
#pergunta numero de diarias
num_diarias = int(input('Digite o número de diarias utilizadas: '))
#pergunta consumo interno
con_interno= float(input('Digite seu consumo interno: '))
#pergunta qual apartamento foi usado
tipo_apto = str(input('Digite qual apartamento foi usado:\nApartamento A\nApartamento B\nApartamento C\nApartamento D\nDigite a letra correspondente:')).upper()
#tabela de valores dos apartamentos
a = 130
b = 200
c = 70
d = 300
#condicionais para calcular o valor da diaria de acordo com o tipo de apartamento
if tipo_apto == 'A':
    valor_diaria = a * num_diarias
elif tipo_apto == 'B':
    valor_diaria = b * num_diarias
elif tipo_apto == 'C':  
    valor_diaria = c * num_diarias
elif tipo_apto == 'D':
    valor_diaria = d * num_diarias
else:
    print('Apartamento inválido.')
#calculo o subtotal 
subtotal = (valor_diaria + con_interno)
#calculo do valor total e função math.round arredonda o valor para 2 casas decimais  
taxa_servico = round(subtotal * 0.10, 2)
#calculo do valor total e função math.round arredonda o valor para 2 casas decimais
total_conta = round(subtotal + taxa_servico, 2)
#mostra os resultados
print('-----------------------------------------')
print('Nome do hóspede:', nome)
print('Tipo de apartamento:', tipo_apto)
print('Número de diárias:', num_diarias)
print('Valor da diária:', valor_diaria)
print('Subtotal:', subtotal)
print('Taxa de serviço (10%):', taxa_servico)
print('Valor total da conta:', total_conta)
print('-----------------------------------------')
print('Obrigado pela preferência!')
print('Volte sempre!')
print('-----------------------------------------')
