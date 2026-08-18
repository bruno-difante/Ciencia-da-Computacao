# Exercícios 10/08 - Bruno Difante

Exercícios com operações constantes, decisões simples e laços lineares.

### Exercício 01 - Operações constantes

```c
void calcular(void) {
  int x = 5;
  x = x * 2;
  printf("%d\n", x);
}
```
- _Determine T(n) e a complexidade assintótica._ <br>
  Todas as instruções são operações constantes (1 atribuição, 1 multiplicação + atribuição, 1 impressão), executadas uma única vez, independente de qualquer entrada. <br>
  **T(n) = 3** (constante) → **O(1)**

### Exercício 02 - Decisão simples

```c
int maior(int a, int b) {
  if (a > b) {
    return a;
  }
  return b;
}
```
- _Calcule a quantidade de passos nos dois possíveis casos._ <br>
  Caso `a > b`: 1 avaliação da condição + 1 retorno = **2 passos** <br>
  Caso `a <= b`: 1 avaliação da condição + 1 retorno = **2 passos** <br>
  Como não há entrada de tamanho variável (n), os dois casos são iguais → **O(1)**

### Exercício 03 - Laço com limite fixo

```c
void imprimir(void) {
  for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
  }
}
```
- _Quantas vezes a impressão é executada? Qual é a complexidade?_ <br>
  A impressão é executada **5 vezes**, sempre, pois o limite do laço (5) é fixo e não depende de nenhuma entrada. <br>
  **Complexidade: O(1)** — tempo constante, já que o número de repetições não cresce com n.

### Exercício 04 - Laço linear sobre um vetor

```c
void somar(int vetor[], int n) {
  int soma = 0;
  for (int i = 0; i < n; i++) {
    soma = soma + vetor[i];
  }
  printf("%d\n", soma);
}
```
- _Determine T(n) e a classe de crescimento._ <br>
  1 atribuição inicial + laço executado n vezes (condição avaliada n+1 vezes, soma e incremento n vezes cada). <br>
  **T(n) = 3n + 2** → **Θ(n)** (classe de crescimento linear)

### Exercício 05 - While linear

```c
int contarAte(int n) {
  int i = 0;
  while (i < n) {
    i++;
  }
  return i;
}
```
- _Calcule as avaliações da condição, os incrementos e T(n)._ <br>
  Avaliações da condição: **n + 1** (n verdadeiras + 1 falsa) <br>
  Incrementos (`i++`): **n** <br>
  **T(n) = 1 (inicialização) + (n+1) + n = 2n + 2** → **O(n)**

### Exercício B6 - Decisão simples

```c
int absoluto(int x) {
  if (x < 0) {
    x = -x;
  }
  return x;
}
```
- _Determine a contagem quando x é negativo e quando não é._ <br>
  `x` negativo: 1 avaliação + 1 atribuição (`x = -x`) + 1 retorno = **3 passos** <br>
  `x` não negativo: 1 avaliação + 1 retorno = **2 passos** <br>
  Em ambos os casos o custo é constante, não depende de n → **O(1)**

### Exercício 07 - Operações aritméticas

```c
int media3(int a, int b, int c) {
  int soma = a + b + c;
  int media = soma / 3;
  return media;
}
```
- _Conte as operações aritméticas, atribuições e retorno._ <br>
  2 somas + 1 atribuição (`soma`) + 1 divisão + 1 atribuição (`media`) + 1 retorno = **6 operações** <br>
  **T(n) = 6** (constante) → **O(1)**

### Exercício 08 - Laço com limite fixo (regressivo)

```c
void regressiva(void) {
  int i = 10;
  while (i > 0) {
    printf("%d\n", i);
    i--;
  }
}
```
- _Determine o total de passos e a complexidade._ <br>
  1 inicialização + 11 avaliações da condição (10 verdadeiras + 1 falsa) + 10 impressões + 10 decrementos = **32 passos**, sempre fixo, pois o limite (10) não depende de nenhuma entrada. <br>
  **Complexidade: O(1)**

### Exercício 09 - Laço com passo 2

```c
void imprimirPares(int n) {
  for (int i = 0; i < n; i += 2) {
    printf("%d\n", i);
  }
}
```
- _Determine T(n)._ <br>
  O laço executa aproximadamente **n/2** vezes (o passo é 2 em vez de 1). <br>
  **T(n) ≈ c · (n/2)** → continua **O(n)**, pois dividir por uma constante não muda a classe de crescimento.

### Exercício 10 - Somatório

```c
int somaAteN(int n) {
  int soma = 0;
  for (int i = 1; i <= n; i++) {
    soma = soma + i;
  }
  return soma;
}
```
- _Determine T(n) e a complexidade._ <br>
  1 atribuição inicial + laço com n iterações (condição avaliada n+1 vezes, soma e incremento n vezes cada). <br>
  **T(n) = 3n + 2** → **O(n)**

### Exercício 11 - Cópia de vetor

```c
void copiar(int origem[], int destino[], int n) {
  for (int i = 0; i < n; i++) {
    destino[i] = origem[i];
  }
}
```
- _Conte os acessos aos vetores e determine T(n)._ <br>
  A cada iteração há 1 leitura em `origem[i]` e 1 escrita em `destino[i]`: **2n acessos**. <br>
  **T(n) = c · n** → **O(n)**

### Exercício 12 - Maior valor com contagem de atualizações

```c
int maiorValor(int vetor[], int n) {
  int maior = vetor[0];
  for (int i = 1; i < n; i++) {
    if (vetor[i] > maior) {
      maior = vetor[i];
    }
  }
  return maior;
}
```
- _Considere p como a quantidade de atualizações do maior valor._ <br>
  A comparação é sempre executada **n − 1** vezes; a atribuição `maior = vetor[i]` é executada **p** vezes, onde `0 ≤ p ≤ n − 1`. <br>
  **T(n) = c1·(n−1) + c2·p**. Mesmo no pior caso (vetor crescente, p = n−1) ou melhor caso (vetor decrescente, p = 0), a complexidade continua **O(n)**, pois quem domina o crescimento é o número de comparações, sempre linear.

### Exercício 13 - While regressivo com n

```c
void contarAteZero(int n) {
  int i = n;
  while (i >= 0) {
    printf("%d\n", i);
    i--;
  }
}
```
- _Quantas vezes o corpo e a condição são executados?_ <br>
  Corpo (impressão + decremento): executado **n + 1** vezes (de n até 0, inclusive). <br>
  Condição: avaliada **n + 2** vezes (n+1 verdadeiras + 1 falsa). <br>
  **T(n) = 1 + (n+2) + 2(n+1) = 3n + 5** → **O(n)**

### Exercício 14 - Soma de ímpares

```c
int somarImpares(int n) {
  int soma = 0;
  for (int i = 1; i <= n; i++) {
    if (i % 2 != 0) {
      soma = soma + i;
    }
  }
  return soma;
}
```
- _Considere o = teto(n/2), a quantidade de números ímpares._ <br>
  O laço percorre todos os n valores (condição e teste `i % 2 != 0` executados n vezes); a soma só ocorre quando i é ímpar, ou seja, **o = ⌈n/2⌉** vezes. <br>
  **T(n) = c1·n + c2·o**, e como o ≤ n, a complexidade continua **O(n)**.

### Exercício 15 - Comparação de vetores

```c
int contarDiferencas(int a[], int b[], int n) {
  int diferentes = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] != b[i]) {
      diferentes++;
    }
  }
  return diferentes;
}
```
- _Considere q como a quantidade de posições diferentes._ <br>
  O laço sempre percorre as n posições (2 acessos aos vetores + 1 comparação por iteração); o incremento `diferentes++` ocorre **q** vezes, onde `0 ≤ q ≤ n`. <br>
  **T(n) = c1·n + c2·q** → como q ≤ n, a complexidade é **O(n)** em qualquer caso.
