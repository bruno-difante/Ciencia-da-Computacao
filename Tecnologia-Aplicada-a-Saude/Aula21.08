# Tecnologias Inteligentes Aplicadas à Saúde: Aula 21/08

## 1. Predição vs. Previsão

**Predição** e **Previsão** parecem sinônimos, mas na área de IA cada uma tem uma finalidade distinta.

### Predição

A **predição** consiste em definir ou classificar um resultado com base nos dados que se tem em mãos.

Em geral, dispomos de informações de entrada sobre um paciente e queremos que um modelo descubra a qual classe ou situação ele pertence.

**Exemplo na saúde:**

Um sistema recebe dados do exame de um tumor e tenta enquadrá-lo como:

* **Benigno**
* **Maligno**

Aqui, o foco não é descobrir **quando** algo vai ocorrer, e sim reconhecer uma condição a partir das informações disponíveis.

Na Ciência da Computação, isso é feito com técnicas de **Machine Learning**, principalmente algoritmos de classificação.

Esquema simplificado:

```text
Dados do paciente/exame
        ↓
Modelo de Machine Learning
        ↓
Classificação
        ↓
Benigno ou Maligno
```

Outros exemplos:

* Predizer se um paciente tem uma determinada doença.
* Classificar um paciente em risco baixo, médio ou alto.
* Detectar em uma imagem sinais de uma certa patologia.
* Predizer a chance de um paciente ser reinternado.

---

### Previsão

A **previsão** diz respeito a estimar o que vai ocorrer **no futuro**, por isso tem uma ligação forte com o **tempo**.

Exemplo:

> Quantos leitos de UTI provavelmente serão necessários na semana que vem?

Para isso, podem-se usar dados históricos:

```text
Semana 1 → 70 leitos ocupados
Semana 2 → 74 leitos ocupados
Semana 3 → 81 leitos ocupados
Semana 4 → 85 leitos ocupados
                ↓
        Modelo de previsão
                ↓
Semana 5 → cerca de 90 leitos
```

Esse tipo de problema pode envolver **séries temporais**, nas quais dados coletados ao longo do tempo servem para estimar valores futuros.

Outros exemplos:

* Prever a quantidade de internações no mês seguinte.
* Prever a demanda por medicamentos.
* Prever como determinada doença vai evoluir.
* Prever a procura por atendimento hospitalar em um certo período.

### Diferença principal

Em resumo:

**Predição → "O que é / qual a classe ou o resultado?"**

**Previsão → "O que provavelmente vai acontecer no futuro?"**

---

# 2. Reconhecimento de Padrões

O **Reconhecimento de Padrões** é uma área fundamental da Inteligência Artificial.

A proposta é usar dados para descobrir **características, relações ou comportamentos recorrentes**.

Na saúde há um enorme volume de dados aproveitáveis para isso, como:

* idade;
* peso;
* pressão arterial;
* frequência cardíaca;
* resultados de exames;
* histórico de doenças;
* medicamentos em uso;
* internações anteriores;
* informações registradas em prontuários.

Um algoritmo consegue examinar esses dados e achar relações difíceis de notar manualmente quando há muitos pacientes envolvidos.

### Exemplo

Considere uma base com milhares de pacientes:

```text
Paciente | Idade | Pressão | Glicose | Histórico | Diagnóstico
---------------------------------------------------------------
A        | 65    | Alta    | Alta    | Sim       | Doença X
B        | 25    | Normal  | Normal  | Não       | Saudável
C        | 70    | Alta    | Alta    | Sim       | Doença X
...
```

O algoritmo pode perceber que certas combinações de características surgem com frequência em pacientes que desenvolveram uma doença específica.

Assim, é possível criar modelos aptos a reconhecer esses padrões em pacientes novos.

---

## Dados estruturados

**Dados estruturados** são informações organizadas conforme um formato definido, geralmente apresentadas em tabelas, campos ou registros.

Por exemplo:

```text
Paciente
├── nome
├── idade
├── peso
├── pressão arterial
├── glicemia
└── diagnóstico
```

Um banco de dados SQL é um exemplo típico de armazenamento de dados estruturados.

Na saúde, dados estruturados podem estar em:

* Prontuários Eletrônicos de Saúde;
* históricos de pacientes;
* resultados de laboratório;
* registros de internação;
* informações sobre medicamentos;
* sinais vitais guardados em sistemas.

A Inteligência Artificial pode usar essas bases para achar padrões e depois fazer **classificações, predições ou previsões**.

---

# 3. Sistema de Recomendação vs. Sistema de Apoio à Decisão

Ambos usam informações para auxiliar o usuário, mas com propósitos diferentes.

## Sistema de Recomendação

Um **Sistema de Recomendação** procura sugerir algo relevante para um usuário específico.

Um caso bem conhecido é o da **Netflix**, que avalia dados como o histórico de visualizações e as preferências para indicar filmes e séries.

De forma simplificada:

```text
Perfil do usuário
        +
Histórico/comportamento
        ↓
Sistema de Recomendação
        ↓
Sugestões personalizadas
```

Na saúde, um sistema assim poderia indicar:

* hábitos mais saudáveis;
* exercícios físicos;
* materiais educativos;
* trilhas de cuidado;
* medidas de prevenção.

Por exemplo, conforme os dados de uma pessoa, o sistema poderia sugerir atividades que melhorem sua qualidade de vida.

É importante tratar com cautela as recomendações de saúde, já que uma sugestão computacional não deve substituir automaticamente a avaliação de um profissional.

---

# 4. Sistema de Apoio à Decisão

Um **Sistema de Apoio à Decisão** não necessariamente decide no lugar do profissional.

Sua meta é oferecer **informações, análises ou alertas que ajudem na tomada de decisão**.

Na medicina isso é especialmente relevante, pois a decisão final pode continuar sendo de responsabilidade do profissional de saúde.

### Exemplo

Suponha que um médico vá prescrever dois medicamentos.

O sistema detecta uma interação conhecida entre eles:

```text
Médico prescreve:
Medicamento A
      +
Medicamento B
      ↓
Sistema verifica a combinação
      ↓
⚠ Possível interação medicamentosa
      ↓
Informação exibida ao médico
      ↓
Médico analisa e decide
```

O sistema está **auxiliando a decisão**, e não necessariamente decidindo pelo médico.

Outros exemplos:

* avisos sobre alergias;
* detecção de possíveis interações entre medicamentos;
* exibição de fatores de risco;
* apoio à interpretação de exames;
* destaque de informações importantes do histórico do paciente.

---

# 5. Principais Áreas de Atuação das Tecnologias Inteligentes na Saúde

As tecnologias inteligentes podem ser empregadas em várias frentes dentro da saúde.

## 5.1 Recomendação

Uso de sistemas inteligentes para sugerir ações ou conteúdos personalizados.

Exemplos:

* hábitos saudáveis;
* exercícios;
* conteúdos de bem-estar;
* trilhas de cuidado;
* acompanhamento individualizado.

A recomendação pode levar em conta as características e o histórico do usuário, gerando sugestões mais adequadas ao seu perfil.

---

## 5.2 Predição e Previsão

### Predição

Procura identificar um resultado ou risco a partir dos dados disponíveis.

Exemplo:

```text
Dados clínicos
     ↓
Modelo
     ↓
Risco de doença
```

### Previsão

Procura estimar eventos futuros, levando em conta também a dimensão do tempo.

Exemplo:

```text
Histórico de internações
        ↓
Modelo de previsão
        ↓
Estimativa de internações
para o mês seguinte
```

Essas técnicas servem tanto para pacientes individuais quanto para o planejamento hospitalar e epidemiológico.

---

# 6. Diagnóstico

A Inteligência Artificial também pode funcionar como ferramenta de **apoio ao diagnóstico**.

Um exemplo relevante é a análise de imagens médicas.

Podem ser examinadas imagens de:

* Raio-X;
* tomografia;
* ressonância magnética;
* ultrassonografia;
* outros tipos de exame.

Algoritmos de Inteligência Artificial, sobretudo técnicas de **Machine Learning e Deep Learning**, conseguem aprender os padrões presentes nessas imagens.

Exemplo:

```text
Imagem de Raio-X
       ↓
Modelo de IA
       ↓
Reconhecimento de padrões
       ↓
Possível alteração detectada
       ↓
Profissional avalia o resultado
```

A IA pode atuar como um recurso complementar, ajudando o profissional a identificar alterações.

---

# 7. Monitoramento e Sensoriamento

Outra aplicação relevante é o acompanhamento contínuo do estado de um paciente.

Isso pode ser feito por meio de **sensores e dispositivos wearables**.

### Wearables

*Wearable* significa, basicamente, uma tecnologia que pode ser **vestida ou usada junto ao corpo**.

Exemplos:

* smartwatch;
* pulseiras inteligentes;
* sensores cardíacos;
* sensores de glicose;
* aparelhos de monitoramento médico.

Esses dispositivos podem captar informações como:

```text
Paciente
   ↓
Sensores / Wearable
   ↓
Frequência cardíaca
Oxigenação
Temperatura
Movimentação
etc.
   ↓
Sistema
   ↓
Análise dos dados
   ↓
Possível alerta
```

Por exemplo, se um dispositivo perceber uma mudança significativa na frequência cardíaca, essa informação pode ser enviada a um sistema responsável pelo acompanhamento.

---

## IoT na saúde

Nesse contexto também surge o conceito de **IoT — Internet of Things (Internet das Coisas)**.

A IoT consiste no uso de dispositivos físicos conectados, capazes de **coletar e trocar informações por meio de uma rede**.

Na saúde, podemos ter:

```text
Sensor
   ↓
Coleta dados do paciente
   ↓
Internet/Rede
   ↓
Servidor / Sistema
   ↓
Processamento dos dados
   ↓
Profissional de saúde
```

Isso viabiliza o **monitoramento remoto de pacientes**, dispensando que toda a coleta de informações seja feita presencialmente.
