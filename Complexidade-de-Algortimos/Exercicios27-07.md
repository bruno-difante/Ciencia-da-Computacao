# Exercícios 27/07 - Bruno Difante

### Exercício 1 - Acesso Direto

```
int obter(int vetor[], int i) {
  return vetor[i];
}
```
- _a) Quantas operações primitivas são realizadas?_ <br>
  2 operações
- _b) A complexidade depende de n?_ <br>
  Não depende


### Exercício 2 - Contagem em um vetor
```
int contarPares(int vetor[], int n) {
  int quantidade = 0;
  for (int i = 0; i < n; i++) {
    if (vetor[i] % 2 == 0) {
      quantidade++;
    }
  }
  return quantidade;
}
```

- _a) Quantas vezes a condição é avaliada?_ <br>
É avaliada N vezes
- _b) A quantidade de incrementos pode mudar?_ <br>
Sim, se for par vai ser n vezes, se for ímpar vai ser 0
- _c) Qual é a complexidade no melhor e no pior caso?_ <br>
Melhor caso: O²
Pior caso: O²

### Exercício 3 — Dois laços sequenciais
```
for (int i = 0; i < n; i++) {
  printf("%d\n", vetor[i]);
}
for (int j = 0; j < n; j++) {
  soma += vetor[j];
}
```
- _a) Determine T(n) de forma simplificada e explique por que o resultado não é Theta(n²)_ <br>
T(n) Primeiro Laço = 3n + 2 operações primitivas <br>
T(n) Segundo Laço = 4n + 2 operações primitivas <br>
Para ser Theta(n²), um laço teria que estar dentro de outro laço. <br>

### Exercício 4 — Laços aninhados
```
for (int i = 0; i < n; i++) {
  for (int j = 0; j < n; j++) {
    comparacoes++;
  }
}
```
- _a) Quantas vezes a linha comparacoes++ é executada?_ <br>
n²
- _b? Qual é a classe de crescimento?_ <br>
O(n²)

### Exercício 5 - Análise de casos
```
int contem(int vetor[], int n, int x) {
  for (int i = 0; i < n; i++) {
    if (vetor[i] == x) {
      return 1;
    }
  }
  return 0;
}
```
- _a) Descreva uma entrada de melhor caso, uma entrada de pior caso e uma hipótese adequada para calcular o caso médio._ <br>
#### Melhor Caso
- **Entrada:** `contem([5, 2, 3, 4], 4, 5)` — elemento na primeira posição
- **Iterações:** 1
- **Complexidade:** O(1)

#### Pior Caso
- **Entrada:** `contem([2, 3, 4, 5], 4, 1)` — elemento não existe
- **Iterações:** n
- **Complexidade:** O(n)

#### Caso Médio
- **Hipótese:** Elemento tem probabilidade igual de estar em qualquer posição
- **Iterações:** n/2
- **Complexidade:** O(n)

| Caso | Iterações | Complexidade |
|------|-----------|------------|
| Melhor | 1 | O(1) |
| Pior | n | O(n) |
| Médio | n/2 | O(n) |


