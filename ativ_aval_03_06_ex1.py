#Programa população de paises 

#funções / rotinas / procedures
def calcular_anos(populacaoA, populacaoB):
    anos = 0
    while populacaoA < populacaoB:
        populacaoA *= 0.003  # Crescimento de 3% ao ano
        populacaoB *= 0.015  # Crescimento de 1.5% ao ano
        anos += 1
    return anos

#pergunta a população de dois países e calcula em quantos anos o país A terá a mesma população que o país B, considerando que o país A cresce 3% ao ano e o país B cresce 1.5% ao ano.
populaçãoA = (int(input('Digite a população do país A: ')))

populaçãoB =(int(input('Digite a população do país B: ')))

calcular_anos(populaçãoA, populaçãoB)

print(f'Em {calcular_anos(populaçãoA, populaçãoB)} anos o país A terá a mesma população que o país B.')

#fim do programa







