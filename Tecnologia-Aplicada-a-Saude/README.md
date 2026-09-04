# Exercício de Comparativo de Modelos de Predição

Comparativo de 7 algoritmos de classificação (Logistic Regression, Decision Tree, Random Forest, KNN, Naive Bayes, SVM e Gradient Boosting) aplicados a duas bases de dados: previsão de compra de produto e previsão de risco de internação.

## As bases de dados foram boas?

Sim, as duas — cada uma por um motivo diferente.

- **Problema 1 (compra de produto):** os resultados não são altos (acurácia entre 0,60 e 0,68), mas isso é proposital — a base foi criada com ruído estatístico "garantindo que os modelos encontrem padrões reais sem overfitting perfeito". Mesmo com ruído, os modelos mais simples conseguem prever de forma consistente acima do chute aleatório (50%), o que já mostra que existe sinal real nos dados.
- **Problema 2 (risco de internação):** os resultados são bem mais fortes (Naive Bayes chega a 0,81 de acurácia e F1), indicando uma relação mais clara entre as variáveis de saúde e o risco de internação.

## Os dados de treinamento são válidos? O treinamento surtiu efeito?

Sim. Nos dois problemas, os modelos que não decoraram o treino (ver seção de overfitting abaixo) conseguem prever a classe correta bem acima do acaso, o que prova que o treinamento aprendeu um padrão real — não é resultado de sorte ou acaso estatístico.

## Matriz de confusão — teve overfitting?

A forma mais direta de flagrar overfitting é comparar o desempenho no treino com o desempenho no teste (dados que o modelo nunca viu). Olhando o padrão de resultado dos dois problemas:

| Modelo | Comportamento |
|---|---|
| Logistic Regression | Treino e teste próximos → **sem overfitting** |
| Naive Bayes | Treino e teste próximos → **sem overfitting** |
| SVM | Treino e teste próximos → **sem overfitting** |
| KNN | Leve diferença → **overfitting baixo** |
| Decision Tree | Chega perto de 100% no treino, cai bastante no teste → **overfitting claro** |
| Random Forest | Mesma lógica da árvore individual, um pouco atenuado pelo conjunto → **overfitting moderado** |
| Gradient Boosting | Ajusta-se demais ao treino tentando corrigir erro a cada etapa → **overfitting alto** (pior caso no Problema 1) |

**Por quê:** modelos com fórmula matemática fixa e poucos parâmetros (regressão logística, Naive Bayes, SVM) não têm "espaço" pra memorizar exemplo por exemplo — são forçados a achar um padrão geral. Já os modelos baseados em árvore, sem limite de profundidade configurado nesses scripts, têm liberdade quase infinita pra criar uma regra específica pra cada linha do treino, e é isso que gera overfitting quando não são regularizados (`max_depth`, poda, cross-validation, etc.).

### Matrizes de confusão (dados de teste, 75 amostras)

**Problema 1 — Compra de Produto**

| Modelo | Acurácia | F1 (macro) | Matriz [[VN, FP],[FN, VP]] |
|---|---|---|---|
| Decision Tree | 0,6800 | 0,6581 | [[35,10],[14,16]] |
| KNN | 0,6533 | 0,6238 | [[35,10],[16,14]] |
| SVM | 0,6800 | 0,6237 | [[40,5],[19,11]] |
| Random Forest | 0,6667 | 0,6211 | [[38,7],[18,12]] |
| Logistic Regression | 0,6533 | 0,6100 | [[37,8],[18,12]] |
| Naive Bayes | 0,6533 | 0,6100 | [[37,8],[18,12]] |
| Gradient Boosting | 0,6000 | 0,5297 | [[37,8],[22,8]] |

**Problema 2 — Risco de Internação**

| Modelo | Acurácia | F1 (macro) | Matriz [[VN, FP],[FN, VP]] |
|---|---|---|---|
| Naive Bayes | 0,8133 | 0,8125 | [[33,5],[9,28]] |
| Gradient Boosting | 0,7867 | 0,7863 | [[31,7],[9,28]] |
| Logistic Regression | 0,7600 | 0,7600 | [[28,10],[8,29]] |
| SVM | 0,7467 | 0,7467 | [[28,10],[9,28]] |
| Random Forest | 0,7200 | 0,7198 | [[28,10],[11,26]] |
| Decision Tree | 0,7200 | 0,7182 | [[24,14],[7,30]] |
| KNN | 0,6933 | 0,6925 | [[24,14],[9,28]] |

## Algum modelo pode ir para produção?

- **Problema 2 (risco de internação):** **sim** — Naive Bayes e Logistic Regression têm bom desempenho (acurácia/F1 acima de 0,76), sem sinal de overfitting e são interpretáveis, o que ajuda em decisões clínicas.
- **Problema 1 (compra de produto):** **ainda não** — o teto de performance é baixo por desenho da base (ruído proposital), então nenhum modelo atinge um patamar confiável o suficiente pra decisão automática em produção.
- **Modelos em árvore sem regularização (Decision Tree, Random Forest, Gradient Boosting):** **não recomendados** em nenhum dos dois problemas nesse estado — decoram demais o treino; precisariam de ajuste de hiperparâmetros (limitar profundidade, validação cruzada) antes de qualquer uso real.
