# 🧵 Trabalho: Operações com Matrizes e Vetores usando Pthreads

Este repositório contém a implementação de dois algoritmos em **linguagem C**, utilizando a biblioteca **Pthread**, com foco em **programação multithreading**.

## ✅ Algoritmos desenvolvidos

1. ### Soma de Matrizes (NxM)
   - Soma duas matrizes de dimensões definidas pelo usuário.
   - Cada linha da matriz é processada por uma **thread independente**, paralelizando a execução.

2. ### Multiplicação de Matriz (NxN) por Vetor (N)
   - Realiza a multiplicação de uma matriz quadrada por um vetor.
   - Cada thread calcula o resultado de uma linha da matriz, otimizando a performance.

## 🐧 Como eu fiz o trabalho no Windows?

- Este projeto foi desenvolvido e executado no Windows Subsystem for Linux (WSL), uma funcionalidade do Windows que permite rodar um ambiente Linux diretamente dentro do sistema operacional, sem precisar de uma máquina virtual ou dual boot.
- Através da extensão "WSL" do VSCode, foi possível editar, compilar e executar os arquivos C em um ambiente Linux completo, garantindo compatibilidade total com bibliotecas como pthread, que não são suportadas nativamente no Windows.

## 🧪 Compilação

```bash
gcc soma_matrizes.c -o soma_matrizes -lpthread
gcc multiplicacao_matriz_vetor.c -o mult_matriz -lpthread
```

## 🚀 Execução

```bash
./soma_matrizes
./mult_matriz
```

---

## 👨‍💻 Autores

Bruno Difante, estudante de Ciência da Computação - Universidade Franciscana (UFN)
Gilberto Morales, estudante de Ciência da Computação - Universidade Franciscana (UFN)
