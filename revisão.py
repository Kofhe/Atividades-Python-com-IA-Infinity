# Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o
#  preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, 
# calcule o valor total da compra somando todos os preços armazenados no dicionário. 
# Por fim, exiba o valor total da compra.

lista = {}

for i in range(5):
    produto1 = input(f'Adiciona seu produto:')

    preco1 = float(input('Digite o preço do produto:'))
   
    lista[produto1] = preco1 #Guarda o produto como chave e o preço como valor.


soma_lista = sum(lista.values()) 

print(f'Seus produtos deram: R$ {soma_lista} reais')
