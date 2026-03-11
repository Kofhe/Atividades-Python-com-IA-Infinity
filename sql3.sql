CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10,2)
);

CREATE TABLE Fornecedores (
    FornecedorID INT PRIMARY KEY,
    NomeFornecedor VARCHAR(100),
    Cidade VARCHAR(100)
);

CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT,
    DataEntrada DATE,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

INSERT INTO Produtos VALUES
(1, 'Mouse', 50, 120.00),
(2, 'Teclado', 30, 200.00),
(3, 'Monitor', 15, 950.00);

INSERT INTO Fornecedores VALUES
(1, 'TechDistribuidora', 'São Paulo'),
(2, 'InfoSupply', 'Curitiba'),
(3, 'DigitalStore', 'Londrina');

INSERT INTO Estoque VALUES
(1, 1, 1, 20, '2026-03-10'),
(2, 2, 2, 15, '2026-03-11'),
(3, 3, 3, 10, '2026-03-12');

SELECT *
FROM Produtos
FULL OUTER JOIN Estoque
ON Produtos.ProdutoID = Estoque.ProdutoID;

SELECT ProdutoID, SUM(Quantidade) AS TotalEstoque
FROM Estoque
GROUP BY ProdutoID;

ALTER TABLE Estoque
ADD Localizacao VARCHAR(50);
