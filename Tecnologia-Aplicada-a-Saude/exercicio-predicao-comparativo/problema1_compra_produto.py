import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score

# Modelos de classificação
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Problema 1 - previsao de compra de produto (dados_predicao_modelos.csv)
# Base sintetica com 250 linhas, ja vem limpa, entao nao precisa tratar nulos igual no exemplo da glicose

# 1. Carregar os dados
df = pd.read_csv('dados_predicao_modelos.csv')

# 2. Features e variável alvo
features = ['Idade', 'Renda_Anual_K', 'Score_Credito', 'Pontuacao_Engajamento']
target = 'Compro_Produto'

X = df[features]
y = df[target]

# 3. Divisão treino/teste com estratificação (mantem a proporcao de 0s e 1s nos dois conjuntos)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# 4. Padronizar (necessário para SVM e KNN, os demais nao dependem tanto disso)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Modelos de classificação
modelos = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'SVM': SVC(),
    'Gradient Boosting': GradientBoostingClassifier()
}

# 6. Avaliar cada modelo
resultados = []
resultados_json = []

print("Avaliação dos Modelos - Problema 1 (Compra de Produto):\n")

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=0)
    matriz = confusion_matrix(y_test, y_pred)

    resultados.append((nome, acc, f1))

    # guarda tudo em formato de dicionario pra depois virar JSON
    resultados_json.append({
        "modelo": nome,
        "acuracia": round(float(acc), 4),
        "f1_score_macro": round(float(f1), 4),
        "matriz_confusao": matriz.tolist()
    })

    print(f"Modelo: {nome}")
    print(f"Acurácia: {acc:.4f}")
    print(f"F1-Score (Macro): {f1:.4f}")
    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("Matriz de Confusão:")
    print(matriz)
    print("-" * 60)

# 7. Ranking final por F1-Score Macro
resultados.sort(key=lambda x: x[2], reverse=True)

print("\nRanking Final dos Modelos:")
print(f"{'Modelo':<25} {'Acurácia':<10} {'F1-Score (Macro)':<15}")
print("-" * 50)
for nome, acc, f1 in resultados:
    print(f"{nome:<25} {acc:<10.4f} {f1:<15.4f}")

# 8. Exportar resultados em JSON padronizado, pra poder ser consumido por outro sistema depois
saida_json = {
    "problema": "Predicao de compra de produto",
    "base": "dados_predicao_modelos.csv",
    "total_amostras": int(len(df)),
    "amostras_treino": int(len(X_train)),
    "amostras_teste": int(len(X_test)),
    "resultados": resultados_json
}

with open('resultado_problema1.json', 'w', encoding='utf-8') as f:
    json.dump(saida_json, f, ensure_ascii=False, indent=2)

print("\nResultados exportados para resultado_problema1.json")
