# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

usuario=input("qual seu nome: ").capitalize() #coloca todas as iniciais maiusculas
tel=input("qual seu tel: ")
email=input("qual seu email: ")
contato = {
    'nome':usuario,
    'telefone': tel,
    'email:' : email
    }
print(f'Olá,{contato["nome"] } do telefone {contato["telefone"]} email:{contato["email:"]}')
