# Desenvolver um programa de linha de comando que permite
# aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
# prioridades e categorias. O projeto será organizado em várias
# partes e usará funções, listas, tuplas, dicionários, conjuntos e
# um ambiente virtual. Passos do projeto:

# Configuração do Ambiente Virtual:
# Crie um ambiente virtual usando o módulo venv

# Definição de Dados:

# Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir

# informações como nome, descrição, prioridade e categoria. Você pode usar
# dicionários para representar as tarefas.

# Funções:
# Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
# como concluídas, exibir tarefas por prioridade ou categoria, e outras
# funcionalidades que desejar.

# Menu de Comandos:
# Crie um menu de comandos de linha de comando que permita ao
# usuário interagir com o programa.

tarefas = []

# Gerenciador de Tarefas Simples

# Lista principal que armazenará todas as tarefas
tarefas = []

# Conjunto para armazenar categorias únicas
categorias = set()

# Função para adicionar uma tarefa
def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (Alta/Média/Baixa): ")
    categoria = input("Categoria: ")

    # Criando o dicionário da tarefa
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    categorias.add(categoria)  # adiciona categoria ao conjunto
    print("Tarefa adicionada com sucesso!\n")

# Função para listar todas as tarefas
def listar_tarefas(lista=None):
    if lista is None:
        lista = tarefas
    if not lista:
        print("Nenhuma tarefa cadastrada.\n")
        return
    for i, tarefa in enumerate(lista, 1):
        status = "✔" if tarefa["concluida"] else "✖"
        print(f"{i}. [{status}] {tarefa['nome']} - {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']}")
    print()

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    escolha = input("Digite o número da tarefa para marcar como concluída: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha-1]["concluida"] = True
            print("Tarefa marcada como concluída!\n")
        else:
            print("Número inválido.\n")
    else:
        print("Entrada inválida.\n")

# Função para filtrar tarefas por prioridade
def filtrar_por_prioridade():
    prioridade = input("Digite a prioridade para filtrar (Alta/Média/Baixa): ")
    filtradas = [t for t in tarefas if t["prioridade"].lower() == prioridade.lower()]
    listar_tarefas(filtradas)

# Função para filtrar tarefas por categoria
def filtrar_por_categoria():
    if not categorias:
        print("Nenhuma categoria cadastrada.\n")
        return
    print("Categorias disponíveis:", ", ".join(categorias))
    categoria = input("Digite a categoria para filtrar: ")
    filtradas = [t for t in tarefas if t["categoria"].lower() == categoria.lower()]
    listar_tarefas(filtradas)

# Menu principal
def menu():
    while True:
        print("=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Filtrar por prioridade")
        print("5. Filtrar por categoria")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            filtrar_por_prioridade()
        elif opcao == "5":
            filtrar_por_categoria()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o menu
if __name__ == "__main__":
    menu()
