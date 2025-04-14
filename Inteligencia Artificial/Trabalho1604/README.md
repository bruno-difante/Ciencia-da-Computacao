# Algoritmo Genético - Roteamento de Cidades 🚗💨

Este projeto utiliza **Algoritmo Genético (AG)** para resolver o **Problema de Roteamento de Cidades**, com 9 cidades numeradas de 1 a 9. O objetivo é encontrar a melhor ordem de visita entre elas, minimizando as penalidades de ordem incorreta e cidades repetidas.

## Descrição 🔍

A rota perfeita é:  
[1, 2, 3, 4, 5, 6, 7, 8, 9]


A **aptidão** de uma rota é calculada com base em duas penalidades:

- **Ordem incorreta**: Se uma cidade de número maior aparecer antes de uma cidade de número menor, é aplicada uma penalidade de **10 pontos**.
- **Cidades repetidas**: Se uma cidade aparecer mais de uma vez, é aplicada uma penalidade de **20 pontos** para cada ocorrência.

## Objetivo 🎯

Encontrar a melhor rota possível, minimizando as penalidades e evoluindo as gerações utilizando as técnicas do **Algoritmo Genético**.

## Arquivos 📂

- **`cromossomo.py`**: Classe que representa uma rota e calcula a aptidão.
- **`util.py`**: Funções auxiliares, como a geração aleatória de rotas.
- **`ag.py`**: Implementação das funções do Algoritmo Genético (seleção, reprodução, mutação).
- **`main.py`**: Execução do algoritmo.

## Resultados ⚡

Ao rodar o programa, o algoritmo evolui as rotas através das gerações até encontrar a melhor solução possível.


## Colaboradores 👨‍💻👨‍💻

**Bruno Difante de Moraes da Silva**  
Curso de Ciência da Computação – Universidade Franciscana (UFN)

📧 E-mail: b.difante@ufn.edu.br

🔗 GitHub: [@Bruno](https://github.com/bouulzzz) 

---

**Gabriel Maier Teixeira**  
Curso de Ciência da Computação – Universidade Franciscana (UFN)

📧 E-mail: gabriel.teixeira@ufn.edu.br 

🔗 GitHub: [@Gabriel](https://github.com/Teizinn) 


