#Caixa de uma lanchonete 
#Autores:Paulo Vilela Vinicius Henrique
#Data: 06/03/2023
#Objetivo: Calcular o valor total de uma compra, considerando os preços dos produtos e a quantidade comprada.


#funções / rotinas / procedures
#função para exibir o menu de produtos disponíveis na lanchonete
def menu():
    print("Bem-vindo à lanchonete!")
    print("Selecione o produto que deseja comprar:")
    print('Código | Produto          | Preço')
    print('-------|------------------|-------')
    print('100    | Cachorro Quente  | R$ 3,50')
    print('101    | Bauru Simples    | R$ 3,80')
    print('102    | Bauru com Ovo    | R$ 4,50')
    print('103    | Hambúrguer       | R$ 4,70')
    print('104    | Cheeseburguer    | R$ 5,30')
    print('105    | Refrigerante     | R$ 4,00')
    print('-------|------------------|-------')
  
#função para calcular o total da compra com base no código do produto e na quantidade desejada
def calcular_total(codigo, quantidade):
    precos = {
        100: 3.50,
        101: 3.80,
        102: 4.50,
        103: 4.70,
        104: 5.30,
        105: 4.00
    }
    # Verifica se o código do produto está no dicionário de preços
    if codigo in precos:
        total = precos[codigo] * quantidade
        return total
    else:
        return None


soma = 0
while True:
    menu()
    # Solicita o código do produto e a quantidade desejada
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade desejada: "))
    total = calcular_total(codigo, quantidade)
    if total is None:
        print('Código do produto invalido.Tente novamente.' )
        continue
    soma+=total 
    adicionar = str(input('Quer adicionar mais produtos [S/N]')).lower()
    if adicionar == 'n':
        print(f'O total da compra: R$ {soma:.2f}')
        break

        
            
       
            
       
    
        

   











