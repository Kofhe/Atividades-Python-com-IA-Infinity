# Crie uma função chamada media 
# que receberá três números como argumentos.
#  Esta função deve calcular a média aritmética desses três números. Para fazer isso, 
# some os três números
#  e, em seguida, divida o resultado por três. 
# Por fim, a função deve retornar o valor da média aritmética calculada.

def media(n1, n2, n3):
    soma = n1 + n2 + n3
    divisao_com_soma = soma / 3
    return divisao_com_soma

print(media(7, 8, 9))
