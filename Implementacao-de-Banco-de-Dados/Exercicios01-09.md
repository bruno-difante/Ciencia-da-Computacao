# Exercícios - Aula 01/09

### Bruno Difante

---

## 1. Variáveis no SQL Server (1.1 a 1.4)

**Enunciado:** Declarar variáveis para nome, quantidade em estoque e preço de um produto; atribuir valores; exibir com `PRINT` e `SELECT`; e realizar um cálculo de salário total a partir de salário base e bônus.

```sql
-- 1.1 Declaração de Variáveis
DECLARE @NomeProduto VARCHAR(50);
DECLARE @QuantidadeEstoque INT;
DECLARE @PrecoProduto DECIMAL(10,2);

-- 1.2 Atribuição de Valores
SET @NomeProduto = 'Notebook';
SET @QuantidadeEstoque = 15;
SET @PrecoProduto = 2999.99;

-- 1.3 Exibição de Valores
PRINT 'Produto: ' + @NomeProduto;
PRINT 'Quantidade em estoque: ' + CAST(@QuantidadeEstoque AS VARCHAR(10));
PRINT 'Preço: R$ ' + CAST(@PrecoProduto AS VARCHAR(20));

SELECT 
    @NomeProduto AS NomeProduto,
    @QuantidadeEstoque AS QuantidadeEstoque,
    @PrecoProduto AS PrecoProduto;

-- 1.4 Cálculo utilizando Variáveis
DECLARE @SalarioBase DECIMAL(10,2);
DECLARE @Bonus DECIMAL(10,2);
DECLARE @SalarioTotal DECIMAL(10,2);

SET @SalarioBase = 5000.00;
SET @Bonus = 800.00;
SET @SalarioTotal = @SalarioBase + @Bonus;

SELECT @SalarioTotal AS SalarioTotal;
```

---

## 2.4. Conversão de String para Data

**Enunciado:** Declarar `@DataNascimento` como `VARCHAR(10)` com o valor `'15/08/1990'` e convertê-la para `DATE` utilizando `CONVERT`.

```sql
DECLARE @DataNascimento VARCHAR(10);
SET @DataNascimento = '15/08/1990';

DECLARE @DataNascimentoConvertida DATE;
SET @DataNascimentoConvertida = CONVERT(DATE, @DataNascimento, 103);

SELECT 
    @DataNascimento AS DataOriginal,
    @DataNascimentoConvertida AS DataConvertida;
```

---

## 3.2. IF / ELSE com Múltiplas Condições

**Enunciado:** Declarar `@NotaFinal` (0 a 100) e exibir uma mensagem diferente conforme a faixa de nota.

```sql
DECLARE @NotaFinal INT;
SET @NotaFinal = 82;

IF @NotaFinal >= 90
    PRINT 'Aprovado com Excelência';
ELSE IF @NotaFinal >= 70
    PRINT 'Aprovado';
ELSE IF @NotaFinal >= 50
    PRINT 'Em Recuperação';
ELSE
    PRINT 'Reprovado';
```

---

## 4.3. Exercício Prático - While percorrendo a tabela Produtos

**Enunciado:** Usando um loop `WHILE`, percorrer a tabela `Produtos` e exibir o nome de cada produto com preço maior que 100.

```sql
DECLARE @Produtos TABLE (
    Indice INT IDENTITY(1,1) PRIMARY KEY,
    Nome VARCHAR(50),
    Preco DECIMAL(10,2)
);

INSERT INTO @Produtos (Nome, Preco) VALUES
('Notebook', 2999.99),
('Mouse', 49.90),
('Monitor', 850.00),
('Teclado', 89.90),
('Cadeira Gamer', 1200.00);

DECLARE @Indice INT = 1;
DECLARE @TotalProdutos INT;
DECLARE @PrecoLimite DECIMAL(10,2) = 100.00;
DECLARE @NomeAtual VARCHAR(50);
DECLARE @PrecoAtual DECIMAL(10,2);

SET @TotalProdutos = (SELECT COUNT(*) FROM @Produtos);

WHILE @Indice <= @TotalProdutos
BEGIN
    SELECT 
        @NomeAtual = Nome, 
        @PrecoAtual = Preco
    FROM @Produtos
    WHERE Indice = @Indice;

    IF @PrecoAtual > @PrecoLimite
        PRINT @NomeAtual + ' - R$ ' + CAST(@PrecoAtual AS VARCHAR(20));

    SET @Indice = @Indice + 1;
END
```

---

## 5.1. DESAFIO - Procedimento Armazenado `CalcularDesconto`

**Enunciado:** Criar um procedimento que recebe preço original e quantidade comprada, aplica 10% de desconto se a quantidade for maior que 10, e — se a quantidade for menor que 5 — aplica um desconto adicional de 1% por unidade acima de 1 usando um loop `WHILE`, retornando o preço final.

```sql
CREATE PROCEDURE CalcularDesconto
    @PrecoOriginal DECIMAL(10,2),
    @Quantidade INT,
    @PrecoFinal DECIMAL(10,2) OUTPUT
AS
BEGIN
    DECLARE @PercentualDesconto DECIMAL(5,2) = 0;
    DECLARE @Contador INT;

    IF @Quantidade > 10
        SET @PercentualDesconto = 10;
    ELSE
        SET @PercentualDesconto = 0;

    IF @Quantidade < 5
    BEGIN
        SET @Contador = 2; -- começa a contar a partir da 2ª unidade
        WHILE @Contador <= @Quantidade
        BEGIN
            SET @PercentualDesconto = @PercentualDesconto + 1;
            SET @Contador = @Contador + 1;
        END
    END

    SET @PrecoFinal = @PrecoOriginal * @Quantidade * (1 - @PercentualDesconto / 100.0);

    PRINT 'Quantidade: ' + CAST(@Quantidade AS VARCHAR(10));
    PRINT 'Desconto aplicado: ' + CAST(@PercentualDesconto AS VARCHAR(10)) + '%';
    PRINT 'Preço final: R$ ' + CAST(@PrecoFinal AS VARCHAR(20));
END
```

**Execução:**

```sql
DECLARE @Resultado DECIMAL(10,2);

-- Exemplo 1
EXEC CalcularDesconto @PrecoOriginal = 100.00, @Quantidade = 15, @PrecoFinal = @Resultado OUTPUT;
SELECT @Resultado AS PrecoFinal_Exemplo1;

-- Exemplo 2
EXEC CalcularDesconto @PrecoOriginal = 100.00, @Quantidade = 4, @PrecoFinal = @Resultado OUTPUT;
SELECT @Resultado AS PrecoFinal_Exemplo2;

-- Exemplo 3
EXEC CalcularDesconto @PrecoOriginal = 100.00, @Quantidade = 7, @PrecoFinal = @Resultado OUTPUT;
SELECT @Resultado AS PrecoFinal_Exemplo3;
```
