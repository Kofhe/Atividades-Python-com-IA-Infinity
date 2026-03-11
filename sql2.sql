CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10,2)
);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
VALUES (1, 'Mouse', 50, 120.00);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
VALUES (2, 'Teclado', 30, 200.00);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
VALUES (3, 'Monitor', 15, 950.00);
