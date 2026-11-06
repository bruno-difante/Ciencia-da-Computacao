# Tecnologias Inteligentes Aplicadas à Saúde

## Ficha do TCC analisado

- **Título:** Anamnese Intuitiva Orientada por IA
- **Curso:** Ciência da Computação, Universidade Franciscana (UFN)
- **Autor:** Rian Beskow Friedrich
- **Orientador:** Sylvio André Garcia Vieira
- **Acesso ao trabalho:** *https://tfgonline.lapinf.ufn.edu.br/media/midias/anamnese_GA4moZU.pdf*

---

A **anamnese** é o momento da consulta em que o profissional levanta o histórico do paciente: sintomas, doenças anteriores, hábitos, remédios em uso e casos na família. Nesse sistema, esse levantamento acontece por meio de um formulário.

O formulário reúne dados como idade, pressão arterial, IMC, tabagismo, consumo de álcool, diabetes, histórico familiar e outros fatores clínicos. Depois, essas informações são organizadas e confrontadas com o dataset **Heart Disease**.

O nome **Heart Disease** quer dizer "doença cardíaca". No trabalho, ele designa um *dataset* sobre doenças cardiovasculares, com mais de 10 mil pacientes registrados e 21 atributos clínicos.

> **Dataset:** coleção organizada de dados usada em análises ou no treinamento de modelos de IA.

A IA do protótipo se apoia em **Aprendizado de Máquina supervisionado**, com o algoritmo **Decision Tree Classifier**.

> **Aprendizado supervisionado:** o algoritmo aprende a partir de exemplos cuja resposta já é conhecida. Aqui, cada exemplo de treino informa se o paciente tem ou não doença cardíaca.

> **Decision Tree Classifier (Classificador por Árvore de Decisão):** algoritmo que decide por meio de uma estrutura em formato de árvore, fazendo divisões sucessivas conforme as características dos dados, até chegar a uma classe.

Depois de treinado, o modelo examina os dados da anamnese e calcula a **probabilidade, em porcentagem, de o paciente ter um problema cardíaco**. O profissional recebe esse número como um indicativo de pré-diagnóstico, que serve de apoio à sua decisão e não toma o lugar do julgamento médico.

> **Pré-diagnóstico:** sinal inicial de que pode existir uma condição de saúde. Não substitui o diagnóstico feito por um profissional habilitado.

---

## Em qual área da saúde se encaixa

O trabalho pertence principalmente à **Medicina**, nos seguintes pontos:

- anamnese;
- análise de fatores de risco cardiovascular;
- suporte ao pré-diagnóstico;
- suporte à decisão do profissional.

---

## Técnicas de IA e o que o TCC usa de cada uma

### Aprendizado de Máquina

É a principal técnica do projeto. **Machine Learning** é o ramo da IA em que os algoritmos extraem padrões dos dados para classificar ou predizer resultados.

O sistema treina um `DecisionTreeClassifier` de forma supervisionada, usando registros já rotulados com presença ou ausência de doença cardíaca. Com isso, o modelo aprende como os atributos clínicos se relacionam ao resultado e passa a classificar pacientes novos.

### Reconhecimento de padrões

O sistema faz **reconhecimento de padrões**: encontra combinações e relações recorrentes nos dados clínicos que podem estar ligadas a um certo desfecho.

A árvore de decisão busca relações entre características como:

- idade;
- pressão sanguínea;
- colesterol;
- IMC;
- diabetes;
- tabagismo;
- consumo de álcool;
- histórico familiar;
- glicemia;
- triglicerídeos;
- demais fatores da saúde cardiovascular.

Esses padrões alimentam a estimativa da probabilidade de doença cardíaca.

### Base de amostras para treinamento

O treinamento usa o dataset **Heart Disease**, com cerca de **10 mil registros e 21 atributos**. Essa base é o conjunto de casos conhecidos a partir do qual o algoritmo aprende o que costuma estar associado à presença ou à ausência da doença.

Além disso, o sistema aceita a inclusão de novos dados de pacientes e permite retreinar o modelo.

### Raciocínio automatizado

O trabalho conta com um processo automático de **inferência**, que é a fase em que um modelo já treinado recebe dados novos e devolve uma resposta. Aqui, o modelo recebe as informações do paciente e percorre a árvore de decisão até chegar a uma classificação probabilística.

Porém, não se trata do raciocínio clássico, baseado em uma base explícita de regras médicas. O raciocínio vem, em essência, do modelo de Aprendizado de Máquina treinado com os dados.

### Processamento de Linguagem Natural

Na fundamentação teórica aparecem conceitos como **PLN**, LLMs, RAG, LangChain, Ollama e Whisper. Em resumo:

| Termo | O que é |
|---|---|
| **PLN** | Área da IA que lida com entender, interpretar ou produzir linguagem humana. |
| **LLM** | Modelo de linguagem treinado com enorme volume de texto, capaz de entender e gerar linguagem. |
| **RAG** | Técnica que une um modelo de linguagem a buscas em fontes externas, para respostas mais contextualizadas. |
| **LangChain** | Framework que conecta modelos de linguagem a bancos de dados, APIs e outras ferramentas. |
| **Ollama** | Ferramenta para rodar modelos de linguagem localmente. |
| **Whisper** | Modelo de reconhecimento de fala que transforma áudio em texto. |

Nenhuma dessas técnicas **foi implementada no protótipo atual**. Elas aparecem como caminhos para trabalhos futuros, por exemplo, para interpretar relatos falados ou escritos dos pacientes.

### Redes Neurais

Não são usadas. A técnica adotada é a **Árvore de Decisão (`DecisionTreeClassifier`)**, do campo do Aprendizado de Máquina supervisionado.

### Sistemas Multiagentes

Também não são usados.

---

## Rotinas da saúde: o que se aplica ao trabalho

### 1. Diagnóstico

**Aplica-se? Sim, como pré-diagnóstico e apoio ao diagnóstico.**

O sistema pega os dados da anamnese e, com o modelo treinado, procura padrões associados à doença cardíaca. O resultado entregue ao profissional é um **pré-diagnóstico** acompanhado de uma porcentagem de probabilidade.

Ou seja, o sistema não fecha um diagnóstico médico. Ele funciona como ferramenta de suporte ao profissional.

**Ligação com a disciplina:**

> reconhecer padrões → usar um grande volume de dados → aplicar algoritmos de Aprendizado de Máquina.

Esse é exatamente o caminho seguido pelo TCC.

---

### 2. Monitoramento / Sensoriamento e atuação

**Aplica-se? Não diretamente.**

O sistema não acompanha o paciente de forma contínua e não usa sensores, wearables, equipamentos médicos nem captura automática de sinais em tempo real. Os dados são digitados no preenchimento da anamnese.

Por isso, mesmo guardando informações clínicas, o trabalho não configura monitoramento nem sensoriamento contínuo.

---

### 3. Predição

**Aplica-se? Sim.**

É uma das principais operações inteligentes do sistema. Com base nos dados da anamnese, o modelo calcula a probabilidade de o paciente pertencer à classe "com doença cardíaca".

Fluxo conceitual:

```text
Dados do paciente
        ↓
Pré-processamento
        ↓
Decision Tree Classifier
        ↓
Reconhecimento de padrões
        ↓
Probabilidade de doença cardíaca
        ↓
Pré-diagnóstico mostrado ao profissional
```

Ou seja, o sistema parte de dados conhecidos para **predizer a classe ou a probabilidade de um paciente novo**.

---

### 4. Previsão

**Aplica-se? Não como operação principal.**

Embora *predição* e *previsão* sejam usadas como sinônimos em alguns contextos, o termo mais correto para este trabalho é **predição**.

A aplicação não tenta estimar como o quadro do paciente vai evoluir no tempo, nem projeta valores futuros de uma série temporal. Ela usa as características atuais do paciente para estimar a chance de uma condição cardíaca.

Resumindo:

- **Predição:** estima um resultado desconhecido a partir das características disponíveis.
- **Previsão:** costuma estimar um evento ou valor futuro, geralmente considerando o tempo.

No TCC, o que ocorre é principalmente **predição**.

---

### 5. Recomendação

**Aplica-se? Parcialmente, como apoio à decisão, mas não como sistema de recomendação.**

O sistema não indica diretamente:

- medicamentos;
- tratamentos;
- procedimentos;
- exames;
- mudanças de conduta.

Ele entrega uma informação preditiva, que o profissional pode usar como suporte para decidir por conta própria. Por isso, o trabalho se aproxima mais de um **Sistema de Apoio à Decisão Clínica** do que de um Sistema de Recomendação.

---

## Apoio à Decisão vs. Recomendação

### Sistema de Apoio à Decisão

Oferece informações, análises, classificações ou estimativas para ajudar o profissional a decidir.

No TCC, a IA mostra ao profissional:

- os dados da anamnese;
- a probabilidade percentual de doença cardíaca;
- a classificação de risco;
- o indicativo de pré-diagnóstico.

A decisão final é sempre do profissional de saúde. Por isso, o trabalho é classificado principalmente como **Sistema de Apoio à Decisão Clínica**.

### Sistema de Recomendação

Sugere uma ação, item ou alternativa considerada adequada para determinada situação. Na saúde, poderia indicar:

- um exame;
- um tratamento;
- uma conduta clínica;
- um medicamento;
- uma intervenção.

O protótipo do TCC **não faz esse tipo de recomendação diretamente**.

---

## Predição vs. Previsão no contexto do TCC

| Conceito | Definição | Aparece no TCC? |
|---|---|---|
| **Predição** | Estima uma classe, resultado ou probabilidade desconhecida a partir dos dados disponíveis. | **Sim.** Estima a probabilidade de doença cardíaca com base na anamnese. |
| **Previsão** | Estima um evento ou valor futuro, geralmente considerando o comportamento ao longo do tempo. | **Não diretamente.** Não há séries temporais nem projeção da evolução clínica. |

---

## Como a disciplina se conecta ao TCC

O fluxo principal do trabalho, relacionado ao conteúdo estudado:

```text
ANAMNESE DO PACIENTE
        ↓
Coleta de dados clínicos
        ↓
BASE DE AMOSTRAS
Heart Disease Dataset
10.000+ registros
        ↓
APRENDIZADO DE MÁQUINA
Decision Tree Classifier
        ↓
RECONHECIMENTO DE PADRÕES
        ↓
PREDIÇÃO
Probabilidade de doença cardíaca
        ↓
PRÉ-DIAGNÓSTICO
        ↓
SISTEMA DE APOIO À DECISÃO
        ↓
PROFISSIONAL DE SAÚDE
Decisão clínica final
```

---

## Quadro-resumo da classificação

| Item estudado | No TCC? | Como se manifesta |
|---|---|---|
| Medicina | **Sim** | Anamnese e avaliação de doença cardíaca |
| Diagnóstico | **Sim** | Indicativo de pré-diagnóstico |
| Monitoramento / Sensoriamento | **Não** | Sem coleta contínua nem sensores |
| Predição | **Sim** | Probabilidade de presença de doença cardíaca |
| Previsão | **Não diretamente** | Não estima evolução futura no tempo |
| Recomendação | **Parcialmente** | Dá apoio à decisão, mas não recomenda tratamentos |
| Aprendizado de Máquina | **Sim** | Decision Tree Classifier |
| Reconhecimento de padrões | **Sim** | Relação entre atributos clínicos e doença cardíaca |
| Base de amostras para treinamento | **Sim** | Heart Disease Dataset |
| Redes Neurais | **Não** | Não implementadas |
| Processamento de Linguagem Natural | **Só teoria/futuro** | LLM, RAG, Whisper etc. não foram implementados |
| Sistemas Multiagentes | **Não** | Não implementados |
| Sistema de Apoio à Decisão | **Sim** | Probabilidade e pré-diagnóstico para auxiliar o profissional |
| Sistema de Recomendação | **Não diretamente** | Não indica tratamento, medicamento nem procedimento |
