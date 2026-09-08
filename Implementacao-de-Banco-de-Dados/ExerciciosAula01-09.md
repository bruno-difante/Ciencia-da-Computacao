## Exercícios feitos em aula, utilizando o banco EMPRESA.sql

### Descobrindo a idade da funcionária Jennifer
---
```sql
DECLARE @data_nasc DATE,
        @idade INT
SELECT @data_nasc = F.Datanasc
    FROM FUNCIONARIO AS F
    WHERE F.Pnome = 'Jennifer';

SET @idade = YEAR(GETDATE()) - YEAR(@data_nasc);
PRINT @idade;
```
---

### CAST -> Muda o tipo dos objetos, transforma um INT em um VARCHAR, por exemplo
---
```sql
SELECT 'O funcionario' 
        + Pnome
        + 'tem o salario de: R$'
        + CAST(Salario AS VARCHAR(10)), Cpf
FROM FUNCIONARIO;
```
---

### CONVERT -> Converter FLOAT ou DATAS para numeros reais
---
```sql
SELECT 'O'
        + Pnome
        + 'tem o salario de: R$'
        + CONVERT(VARCHAR(10), Salario) AS 'Nome + Salario'
FROM FUNCIONARIO;
```
---

### Comparando o salário de um funcionário com a média salarial
---
```sql
DECLARE @media DECIMAL(10,2);
        @salario;
        
SELECT @media = AVG (F.Salario)
FROM FUNCIONARIO AS F;

        
SELECT @salario = F.Salario
FROM FUNCIONARIO AS F;
WHERE F.Pnome = 'Jennifer'

IF (@salario < @media ) 
    PRINT 'Funcionario fudido,'
ELSE
    PRINT 'Ta no lucro'
```
---
