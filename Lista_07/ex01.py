#titulo
print('Conversor de temperatura')

celsius = 0 #iniciador

while celsius >= -5:
    celsius = float(input('Digite a temperatura em graus celsius° para saber o seu valor em Fahrenheit e Kelvin:'))
    fahrenheit = celsius*1.8 + 32
    kelvin = celsius + 273.15
    print(f'A temperatura {celsius} C° em fahrenheit é {fahrenheit } F° e em Kelvin é {kelvin} K° ')

print('Obrigado')
