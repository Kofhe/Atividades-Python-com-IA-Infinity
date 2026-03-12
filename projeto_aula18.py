import sqlite3

# conexão com banco
conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

# criar tabela produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    descricao TEXT,
    quantidade INTEGER,
    preco REAL
)
""")

# criar tabela vendas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    quantidade INTEGER,
    data TEXT
)
""")

conn.commit()


# =====================
# CLASSE PRODUTO
# =====================

class Produto:

    def cadastrar(self):
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        cursor.execute(
            "INSERT INTO produtos(nome,descricao,quantidade,preco) VALUES(?,?,?,?)",
            (nome, descricao, quantidade, preco)
        )

        conn.commit()
        print("Produto cadastrado!")

    def listar(self):

        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("\nPRODUTOS:")
            for p in produtos:
                print(p)

    def atualizar(self):
        id_produto = int(input("ID do produto: "))
        nova_qtd = int(input("Nova quantidade: "))

        cursor.execute(
            "UPDATE produtos SET quantidade=? WHERE id=?",
            (nova_qtd, id_produto)
        )

        conn.commit()
        print("Quantidade atualizada!")

    def remover(self):
        id_produto = int(input("ID do produto: "))

        cursor.execute(
            "DELETE FROM produtos WHERE id=?",
            (id_produto,)
        )

        conn.commit()
        print("Produto removido!")


# =====================
# CLASSE VENDA
# =====================

class Venda:

    def vender(self):
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade vendida: "))

        cursor.execute(
            "INSERT INTO vendas(produto_id,quantidade,data) VALUES(?,?,date('now'))",
            (produto_id, quantidade)
        )

        cursor.execute(
            "UPDATE produtos SET quantidade = quantidade - ? WHERE id=?",
            (quantidade, produto_id)
        )

        conn.commit()
        print("Venda registrada!")


# =====================
# MENU
# =====================

produto = Produto()
venda = Venda()

while True:

    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar quantidade")
    print("4 - Remover produto")
    print("5 - Registrar venda")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        produto.cadastrar()

    elif opcao == "2":
        produto.listar()

    elif opcao == "3":
        produto.atualizar()

    elif opcao == "4":
        produto.remover()

    elif opcao == "5":
        venda.vender()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
