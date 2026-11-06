# Aula 21/08

## 1. DecisionTreeClassifier (scikit-learn)

O `DecisionTreeClassifier` é um algoritmo de Machine Learning para **classificação**, disponível na biblioteca scikit-learn (`sklearn`). Ele implementa uma **Árvore de Decisão**.

### Como ele raciocina

O algoritmo funciona como uma sequência de perguntas. Imagine que queremos classificar uma pessoa em **alto** ou **baixo risco** para uma doença, usando estas informações:

- Idade
- Pressão arterial
- Glicose
- Colesterol

A árvore pode aprender regras como estas:

```text
                 Glicose > 125?
                  /          \
               SIM            NÃO
                |              |
          Idade > 60?      Baixo risco
           /      \
         SIM      NÃO
          |         |
      Alto risco  Pressão alta?
                   /       \
                 SIM       NÃO
                  |         |
              Alto risco  Baixo risco
```

> **Ponto-chave:** quem usa o algoritmo não escreve essas regras à mão. Ele examina os dados de treinamento e descobre sozinho quais perguntas e divisões separam melhor as classes.

### Exemplo mínimo

```python
from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier()

modelo.fit(X_treino, y_treino)

resultado = modelo.predict(X_teste)
```

| Comando | O que faz |
|---|---|
| `DecisionTreeClassifier()` | Cria o modelo de árvore de decisão. |
| `.fit()` | Treina a árvore com exemplos conhecidos. |
| `.predict()` | Usa o que foi aprendido para classificar dados novos. |

---

## 2. Pipeline de ML com a base de glicose

Este pipeline usa os dados de glicose do repositório do professor Zamberlan.

### Relação com ETL

Do ponto de vista técnico, o código aplica apenas as duas primeiras etapas do ETL:

| Etapa | Aplicada? | O que acontece no código |
|---|---|---|
| **E**xtract (extração) | Sim | `pd.read_csv(url)` carrega os dados do CSV. |
| **T**ransform (transformação) | Sim | Seleção das *features*, separação de `X` e `y`, `train_test_split()` e `StandardScaler()`. |
| **L**oad (carga) | Não | Os dados transformados não são gravados em nenhum destino. |

> **Sobre o Load:** em um ETL tradicional, os dados transformados seriam enviados a algum destino, por exemplo com `df_transformado.to_sql(...)` ou `df_transformado.to_csv(...)`. Isso não aparece no código.

### Visão geral do fluxo

```text
CSV (glicose_data.csv)
        ↓
Carregar com pandas
        ↓
Separar features (X) e target (y)
        ↓
Dividir em treino (70%) e teste (30%)
        ↓
Padronizar com StandardScaler
        ↓
Treinar 7 modelos diferentes
        ↓
Avaliar: acurácia, F1, relatório e matriz de confusão
        ↓
Ranking final por F1-Score
```

### Modelos comparados

| Modelo | Ideia central |
|---|---|
| Logistic Regression | Classificação baseada em probabilidades. |
| Decision Tree | Sequência de regras/perguntas que separam as classes. |
| Random Forest | Várias árvores de decisão cujos resultados são combinados. |
| KNN | Classifica um exemplo olhando seus vizinhos mais próximos. |
| Naive Bayes | Usa probabilidades e o Teorema de Bayes. |
| SVM | Busca a fronteira que melhor separa as classes. |
| Gradient Boosting | Cria modelos em sequência, cada um corrigindo os erros do anterior. |

---

## 3. Código passo a passo

> Os blocos abaixo formam um único script. Execute-os na ordem em que aparecem.

### Passo 0: Importações

```python
# ============================================================
# COMPARAÇÃO DE MODELOS DE CLASSIFICAÇÃO: BASE DE GLICOSE
# ============================================================

# pandas: lê, organiza e manipula dados em formato de tabela.
# Aqui, é usado principalmente para carregar o CSV.
import pandas as pd

# train_test_split: separa a base em treino e teste.
from sklearn.model_selection import train_test_split

# StandardScaler: coloca as variáveis em uma escala parecida.
#
# Exemplo: KCAL pode valer 2000 e SONO pode valer 8.
# Essa diferença de escala atrapalha alguns algoritmos,
# principalmente KNN e SVM.
from sklearn.preprocessing import StandardScaler

# Métricas para medir o desempenho dos modelos
from sklearn.metrics import (
    accuracy_score,        # porcentagem total de acertos
    classification_report, # precision, recall, F1-score e support
    confusion_matrix,      # acertos e erros entre as classes
    f1_score               # equilíbrio entre precision e recall
)

# ------------------------------------------------------------
# Modelos de Machine Learning
# ------------------------------------------------------------

# Regressão Logística: classificação baseada em probabilidades
from sklearn.linear_model import LogisticRegression

# Árvore de Decisão: sequência de regras para separar as classes
from sklearn.tree import DecisionTreeClassifier

# Random Forest: combina o resultado de várias árvores
# Gradient Boosting: modelos em sequência, cada um corrige o anterior
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

# Naive Bayes: probabilidades e Teorema de Bayes
from sklearn.naive_bayes import GaussianNB

# KNN: classifica pelos vizinhos mais próximos
from sklearn.neighbors import KNeighborsClassifier

# SVM: procura a melhor fronteira entre as classes
from sklearn.svm import SVC
```

---

### Passo 1: Carregar os dados

```python
url = 'https://raw.githubusercontent.com/alexandrezamberlan/tias/refs/heads/main/predicao_previsao_codigos_exemplos/glicose_data.csv'

# read_csv() lê o CSV e devolve um DataFrame,
# a estrutura do pandas parecida com uma tabela.
df = pd.read_csv(url)
```

---

### Passo 2: Definir features e target

```python
# Features: as informações que serão entregues aos modelos
features = ['INSULINA', 'KCAL', 'CARB', 'SONO', 'padel']

# Target: o que o modelo deve aprender a classificar
target = 'GLICEMIA'

# X: apenas as colunas de entrada
X = df[features]

# y: a resposta correta que queremos classificar
y = df[target]
```

Visualmente:

```text
INSULINA
KCAL
CARB          →   MODELO   →   GLICEMIA
SONO
padel
```

---

### Passo 3: Dividir em treino e teste

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,

    # 30% dos dados vão para TESTE e 70% para TREINO
    test_size=0.3,

    # Semente da divisão aleatória: ao rodar de novo,
    # a divisão será sempre a mesma
    random_state=42,

    # Mantém a proporção das classes em treino e teste
    stratify=y
)
```

**Parâmetros:**

| Parâmetro | Função |
|---|---|
| `test_size=0.3` | Reserva 30% dos dados para teste. |
| `random_state=42` | Garante que a divisão aleatória seja reproduzível. |
| `stratify=y` | Preserva a proporção das classes. Se a base tem 70% de A, 20% de B e 10% de C, treino e teste tentam manter essas proporções. |

**Resultado da divisão:**

| Variável | Conteúdo |
|---|---|
| `X_train` | Entradas usadas no treinamento |
| `y_train` | Respostas corretas do treinamento |
| `X_test` | Entradas usadas para testar o modelo |
| `y_test` | Respostas corretas usadas na comparação |

---

### Passo 4: Padronizar os dados

```python
# Cria o objeto que fará a padronização
scaler = StandardScaler()

# fit_transform() no TREINO:
#   fit       → aprende a média e o desvio padrão dos dados de treino
#   transform → usa esses valores para transformar os dados
#
# Depois disso, cada variável fica com média ≈ 0 e desvio padrão ≈ 1
X_train = scaler.fit_transform(X_train)

# transform() no TESTE:
# NÃO se usa fit de novo. Aplica-se só a transformação já aprendida
# no treino, para que nenhuma informação do teste vaze para o
# treinamento (data leakage).
X_test = scaler.transform(X_test)
```

> **Atenção:** `fit_transform()` só no treino e `transform()` no teste. Fazer `fit` no conjunto de teste causaria *data leakage*.

---

### Passo 5: Criar os modelos

```python
# Dicionário no formato "nome do modelo": objeto do modelo.
# Assim, um único for percorre todos eles.
modelos = {

    # max_iter=1000: até 1000 iterações para o algoritmo
    # achar uma solução durante o treino
    'Logistic Regression': LogisticRegression(max_iter=1000),

    # Regras em formato de árvore (pode sofrer overfitting
    # se crescer demais)
    'Decision Tree': DecisionTreeClassifier(),

    # Várias árvores, com as classificações combinadas
    'Random Forest': RandomForestClassifier(),

    # Observa os exemplos mais próximos para definir a classe
    'KNN': KNeighborsClassifier(),

    # Calcula probabilidades e escolhe a classe mais provável
    'Naive Bayes': GaussianNB(),

    # Procura uma fronteira que separe as classes
    'SVM': SVC(),

    # Modelos em sequência, cada um tentando corrigir os erros do anterior
    'Gradient Boosting': GradientBoostingClassifier()
}
```

---

### Passo 6: Preparar a lista de resultados

```python
# Lista vazia. Cada item guardará a tupla:
# (nome_do_modelo, acurácia, f1_score)
resultados = []

print("Avaliação dos Modelos:\n")
```

---

### Passo 7: Treinar e avaliar todos os modelos

```python
# modelos.items() percorre chave e valor do dicionário.
# Exemplo: nome = "Decision Tree", modelo = DecisionTreeClassifier()
for nome, modelo in modelos.items():

    # ---------- Treinamento ----------
    # fit(): treina o modelo.
    # X_train = características, y_train = respostas corretas.
    # O algoritmo tenta aprender a relação entre X e y.
    modelo.fit(X_train, y_train)

    # ---------- Predição ----------
    # predict(): usa o modelo treinado para classificar dados
    # que não foram vistos no treino.
    # y_pred = respostas previstas pelo modelo.
    y_pred = modelo.predict(X_test)

    # ---------- Acurácia ----------
    # Compara a resposta real (y_test) com a prevista (y_pred).
    #
    #              acertos
    # acurácia = -----------
    #               total
    #
    # Exemplo: 90 acertos em 100 exemplos = 0.90 = 90%
    acc = accuracy_score(y_test, y_pred)

    # ---------- F1-Score ----------
    # Junta Precision e Recall em uma só métrica.
    #
    # Precision: "Dos que o modelo disse serem dessa classe,
    #             quantos realmente eram?"
    # Recall:    "De todos que realmente eram dessa classe,
    #             quantos o modelo encontrou?"
    #
    # average='macro': calcula o F1 de cada classe separadamente
    #   e tira a média simples, dando o mesmo peso a todas as classes.
    # zero_division=0: se uma divisão for impossível, retorna 0
    #   em vez de gerar erro ou aviso.
    f1 = f1_score(
        y_test,
        y_pred,
        average='macro',
        zero_division=0
    )

    # ---------- Guardar resultado ----------
    # append() adiciona um item ao final da lista.
    # Exemplo: ("Random Forest", 0.92, 0.91)
    resultados.append((nome, acc, f1))

    # ---------- Mostrar resultado do modelo ----------
    print(f"Modelo: {nome}")
    print(f"Acurácia: {acc:.4f}")
    print(f"F1-Score (Macro): {f1:.4f}")

    # classification_report(): métricas por classe
    #   precision = precisão
    #   recall    = capacidade de encontrar os exemplos da classe
    #   f1-score  = equilíbrio entre precision e recall
    #   support   = quantidade real de exemplos da classe
    print("Relatório de Classificação:")
    print(
        classification_report(
            y_test,
            y_pred,
            zero_division=0
        )
    )

    # confusion_matrix(): mostra quais classes o modelo acertou
    # e quais ele confundiu.
    #
    #              PREVISTO
    #             A       B
    #
    # REAL A     40       5
    #      B      3      22
    #
    # 40 = A classificada corretamente
    #  5 = A confundida com B
    #  3 = B confundida com A
    # 22 = B classificada corretamente
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    print("-" * 60)
```

---

### Passo 8: Ordenar os modelos (ranking)

```python
# Cada item da lista tem a forma:
#   (nome, acurácia, f1)
#      0       1      2
#
# lambda x: x[2] → ordena pelo índice 2, o F1-Score
# reverse=True   → do MAIOR F1 para o MENOR
resultados.sort(
    key=lambda x: x[2],
    reverse=True
)
```

---

### Passo 9: Mostrar o ranking final

```python
print("\nRanking Final dos Modelos:")

print(
    f"{'Modelo':<25} "
    f"{'Acurácia':<10} "
    f"{'F1-Score (Macro)':<15}"
)

print("-" * 50)

# Percorre os resultados já ordenados pelo F1-Score
for nome, acc, f1 in resultados:

    # .4f → 4 casas decimais (0.913327 vira 0.9133)
    print(
        f"{nome:<25} "
        f"{acc:<10.4f} "
        f"{f1:<15.4f}"
    )
```

---

## 4. Resumo rápido

### Métricas

| Métrica | Pergunta que responde |
|---|---|
| **Acurácia** | Qual porcentagem do total o modelo acertou? |
| **Precision** | Dos que o modelo apontou como de uma classe, quantos realmente eram? |
| **Recall** | De todos que realmente eram da classe, quantos o modelo encontrou? |
| **F1-Score** | Qual o equilíbrio entre precision e recall? |
| **Matriz de confusão** | Quais classes foram acertadas e quais foram confundidas entre si? |

### Boas práticas do código

- Separe **treino** e **teste** antes de qualquer outra coisa.
- Use `fit_transform()` só no treino e `transform()` no teste, para evitar *data leakage*.
- Use `stratify=y` para manter a proporção das classes.
- Use `random_state` para que o experimento possa ser reproduzido.
- Compare vários modelos com as mesmas métricas e a mesma divisão de dados.
- O ranking aqui usa o F1 *macro*, porque ele dá o mesmo peso a todas as classes.
