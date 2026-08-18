# Exercícios II 10/08 - Bruno Difante

Exercícios com laços sequenciais e aninhados, matrizes e análise de casos.

### Exercício 01 - Melhor e pior caso sem early exit

```c
int contarPositivos(int vetor[], int n) {
  int quantidade = 0;
  for (int i = 0; i < n; i++) {
    if (vetor[i] > 0) {
      quantidade++;
    }
  }
  return quantidade;
}
```
- _Considere q como a quantidade de positivos. Determine melhor e pior caso._ <br>
  Como não há `break`, o laço sempre percorre as n posições, avaliando a condição n vezes; o incremento ocorre q vezes (0 ≤ q ≤ n). <br>
  **Melhor caso (q = 0):** T(n) = c1·n → **Θ(n)** <br>
  **Pior caso (q = n):** T(n) = c1·n + c2·n → **Θ(n)** <br>
  Não há diferença assintótica entre os casos: sempre **Θ(n)**, pois o laço nunca termina antecipadamente.

### Exercício 02 - Busca linear com retorno antecipado

```c
int contem(int vetor[], int n, int x) {
  for (int i = 0; i < n; i++) {
    if (vetor[i] == x) {
      return 1;
    }
  }
  return 0;
}
```
- _Analise o elemento na posição k e o caso em que ele não existe._ <br>
  Se `x` está na posição k (0 ≤ k < n), o laço executa **k + 1** iterações antes de retornar. <br>
  **Melhor caso (k = 0):** 1 iteração → **O(1)** <br>
  **Pior caso (elemento na última posição ou inexistente):** n iterações → **O(n)**

### Exercício 03 - Dois laços sequenciais

```c
void processar(int vetor[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d\n", vetor[i]);
  }
  for (int j = 0; j < n; j++) {
    vetor[j] = 0;
  }
}
```
- _Determine T(n)._ <br>
  Primeiro laço: n iterações. Segundo laço: n iterações (independentes, um após o outro, não aninhados). <br>
  **T(n) = c1·n + c2·n = O(n)** — laços sequenciais se somam, não se multiplicam.

### Exercício 04 - Laço triangular

```c
int contarOperacoes(int n) {
  int total = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i; j++) {
      total++;
    }
  }
  return total;
}
```
- _Quantas vezes total++ é executado? Determine T(n)._ <br>
  Para i = 0, 1, 2, ..., n−1 o laço interno executa 1, 2, 3, ..., n vezes. <br>
  Total = 1 + 2 + ... + n = **n(n+1)/2** <br>
  **T(n) = Θ(n²)**

### Exercício 05 - Laço retangular (matriz n × m)

```c
int contarMatriz(int n, int m) {
  int total = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      total++;
    }
  }
  return total;
}
```
- _Quantas vezes total++ é executado? Determine T(n)._ <br>
  O laço interno executa m vezes para cada uma das n iterações do laço externo. <br>
  Total = **n · m** → **T(n, m) = O(n · m)**

### Exercício 06 - Soma de prefixos

```c
void prefixos(int vetor[], int saida[], int n) {
  saida[0] = vetor[0];
  for (int i = 1; i < n; i++) {
    saida[i] = saida[i - 1] + vetor[i];
  }
}
```
- _Considere n maior ou igual a 1. Determine T(n)._ <br>
  1 atribuição inicial (`saida[0]`) + laço com n−1 iterações (cada uma com 2 acessos a vetor, 1 soma e 1 atribuição). <br>
  **T(n) = 1 + c·(n−1) = O(n)**

### Exercício 07 - Dois laços sequenciais com limites distintos

```c
int contarDuasListas(int n, int m) {
  int total = 0;
  for (int i = 0; i < n; i++) {
    total++;
  }
  for (int j = 0; j < m; j++) {
    total++;
  }
  return total;
}
```
- _Determine T(n,m) sem supor que n e m são iguais._ <br>
  Primeiro laço: n iterações. Segundo laço: m iterações (sequenciais, não aninhados). <br>
  **T(n, m) = c1·n + c2·m = O(n + m)**

### Exercício 08 - Laço interno com limite constante

```c
int repetirTresVezes(int n) {
  int total = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 3; j++) {
      total++;
    }
  }
  return total;
}
```
- _Explique por que dois laços não implicam necessariamente Θ(n²)._ <br>
  O laço interno tem limite **fixo (3)**, independente de n, então ele não contribui para o crescimento assintótico — apenas multiplica por uma constante. <br>
  Total de execuções de `total++` = n · 3 = 3n → **T(n) = Θ(n)**, e não Θ(n²). <br>
  Dois laços aninhados só resultam em Θ(n²) quando **ambos** os limites dependem de n.

### Exercício 09 - Soma de matriz n × n

```c
int somarMatriz(int matriz[][100], int n) {
  int soma = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      soma = soma + matriz[i][j];
    }
  }
  return soma;
}
```
- _Determine T(n) e a quantidade de acessos aos elementos._ <br>
  Laços aninhados, ambos de tamanho n: **n² iterações**, cada uma com 1 acesso à matriz. <br>
  Acessos aos elementos: **n²** <br>
  **T(n) = Θ(n²)**

### Exercício 10 - Comparações todos-contra-todos

```c
int contarIguais(int vetor[], int n) {
  int iguais = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (vetor[i] == vetor[j]) {
        iguais++;
      }
    }
  }
  return iguais;
}
```
- _Considere p como a quantidade de comparações verdadeiras._ <br>
  As comparações (`vetor[i] == vetor[j]`) são sempre executadas **n²** vezes; o incremento `iguais++` ocorre **p** vezes, onde n ≤ p ≤ n² (pelo menos a diagonal, i = j, é sempre verdadeira). <br>
  **T(n) = c1·n² + c2·p** → independente de p (pois p ≤ n²), a complexidade é **Θ(n²)**

### Exercício 11 - Laço triangular (j a partir de i)

```c
int contarTriangulo(int n) {
  int total = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      total++;
    }
  }
  return total;
}
```
- _Determine quantas vezes total++ é executado._ <br>
  Para i = 0, 1, ..., n−1 o laço interno executa n, n−1, ..., 1 vezes. <br>
  Total = n + (n−1) + ... + 1 = **n(n+1)/2** → **Θ(n²)**

### Exercício 12 - Apenas a diagonal da matriz

```c
int somarDiagonal(int matriz[][100], int n) {
  int soma = 0;
  for (int i = 0; i < n; i++) {
    soma = soma + matriz[i][i];
  }
  return soma;
}
```
- _A matriz possui n² elementos, mas quantos são visitados?_ <br>
  Apenas um laço simples, de 0 a n−1, acessando `matriz[i][i]`. <br>
  Elementos visitados: **n** (apenas a diagonal, não os n² elementos da matriz). <br>
  **T(n) = O(n)**

### Exercício 13 - Comparações com j < i

```c
int contarMaiores(int vetor[], int n) {
  int total = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (vetor[i] > vetor[j]) {
        total++;
      }
    }
  }
  return total;
}
```
- _Considere p como a quantidade de condições verdadeiras._ <br>
  O laço interno executa 0, 1, 2, ..., n−1 vezes (para i = 0, 1, ..., n−1). <br>
  Comparações sempre executadas: 0+1+...+(n−1) = **n(n−1)/2** <br>
  O incremento `total++` ocorre **p** vezes, onde p ≤ n(n−1)/2. <br>
  **T(n) = Θ(n²)**, independente do valor de p.

### Exercício 14 - Laço com break (melhor/pior caso)

```c
int somaAteNegativo(int vetor[], int n) {
  int soma = 0;
  for (int i = 0; i < n; i++) {
    if (vetor[i] < 0) {
      break;
    }
    soma = soma + vetor[i];
  }
  return soma;
}
```
- _Determine o melhor caso e o pior caso._ <br>
  **Melhor caso:** o primeiro elemento é negativo → o laço encerra na primeira iteração → **O(1)** <br>
  **Pior caso:** nenhum elemento é negativo (ou só o último é) → o laço percorre todo o vetor → **O(n)**

### Exercício 15 - Laços aninhados retangulares (matriz n × m)

```c
void imprimirSomas(int matriz[][100], int n, int m) {
  for (int i = 0; i < n; i++) {
    int somaLinha = 0;
    for (int j = 0; j < m; j++) {
      somaLinha = somaLinha + matriz[i][j];
    }
    printf("%d\n", somaLinha);
  }
}
```
- _Determine T(n,m) e a complexidade._ <br>
  Para cada uma das n linhas, o laço interno percorre m colunas. <br>
  **T(n, m) = c1·n·m + c2·n = O(n · m)**
