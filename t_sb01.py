#Calculadora de energia mecanica total                                                  - comentario
#Autor: Paulo Augusto de Jesus Vilela   

print('Calculadora de energia mecanica total')#titulo

while True:#verifica valor entrada 
    ge = str(input('Digite se a energia potencial é gravitacional ou elastica [G/E]: ')).upper()#entrada da energia potencial
    if ge in ['G','E']:
        break
    print('Valor invalido digite novamente!')
    
if ge == 'G':
    try:
        m = float(input('Digite a massa do corpo em kg: '))#entrada da massa
        v = float(input('Digite a velocidade do corpo em m/s: '))#entrada da velocidade
        g = 9.8#gravidade
        h = float(input('Digite a altura do corpo em metros: '))#entrada da altura
        ec= m*v**2/2#calculo da energia cinetica
        epg = m*g*h#calculo da energia potencial gravitacional
        em = ec + epg#calculo da energia mecanica total
        print(f'A energia mecanica total é:{ em:.2f}')#saida da energia mecanica total
    except ValueError:
        print('Erro: Por favor, insira valores numéricos válidos')#mensagem de erro  

else:
    try:
        k= float(input('Digite a constante elástica em N/m: '))#entrada da constante elastica
        x= float(input('Digite a deformação em metros: '))#entrada da deformação
        m = float(input('Digite a massa do corpo em kg: '))#entrada da massa
        v = float(input('Digite a velocidade do corpo em m/s: '))#entrada da velocidade
        ec= m*v**2/2#calculo da energia cinetica
        epe = (k*x**2)/2#calculo da energia potencial elastica
        em = ec + epe#calculo da energia mecanica total
        print(f'A energia mecanica total é: {em:.2f}')#saida da energia mecanica total
    except ValueError:
        print('Erro: Por favor, insira valores numéricos válidos')

print('Fim do programa')#mensagem de fim


        

    

    
        




