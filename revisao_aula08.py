# Importe o módulo 'os' e use a função 'listdir' 
# para listar todos os arquivos e pastas presentes
#  no diretório onde o script Python está sendo executado. 
# A função 'listdir' retornará uma lista contendo os nomes 
# dos arquivos e pastas. Após obter essa lista, exiba cada 
# item da lista individualmente na saída do console.

#importar os
import os
#função que lista arquivos
os.listdir(".") #"." significa diretorio atual
#guardar o retorno numa variavel
itens = os.listdir(".")
#irá percorrer a lista e mostrar o item dos itens
for item in itens:
    print(item)
