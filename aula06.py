#Calculo salarial
#data : 31/02/2025


print('\n\n calculo salarial')     #titulo
h = int(input('digite o numero de horas trabalhadas'))
sal_min = float (input('digite o valor do salario minimo:'))

#processamento 
valor_h_trab = sal_min/2 
valor_bruto = h * valor_h_trab
imposto = valor_bruto * 0.03
sal