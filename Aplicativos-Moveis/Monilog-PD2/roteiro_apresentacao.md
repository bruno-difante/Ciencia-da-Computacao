# Apresentação do Projeto: MoniLog

## Slide 1: Capa
- **Título na tela:** MoniLog
- **Subtítulo:** Sistema de Registro de Ocorrências para Videomonitoramento
- **Seu Nome:** [Seu Nome]
- **O que falar:** "Olá, vou apresentar o MoniLog, um aplicativo que desenvolvi para modernizar o registro de incidentes em centrais de segurança."

---

## Slide 2: O Problema
- **Tópicos na tela:**
  - Centrais de monitoramento precisam de agilidade.
  - Registros manuais são lentos e suscetíveis a falhas.
  - Necessidade de histórico rápido e rastreável.
- **O que falar:** "Hoje, operadores de câmeras lidam com eventos críticos (invasões, falhas). O problema é que anotar isso em papel ou planilhas perde muito tempo e não padroniza a informação. Precisamos de um sistema focado em velocidade."

---

## Slide 3: A Solução (O que o app faz)
- **Tópicos na tela:**
  - Login rápido por turno e operador.
  - Cadastro de ocorrências em menos de 10 segundos.
  - Categorização fixa (Disparo de Alarme, Invasão, etc).
  - Atualização de Status (Em Análise → Resolvido).
- **O que falar:** "Criei o MoniLog. Ele permite que o operador se identifique, veja uma lista das ocorrências do seu turno e registre novos eventos com apenas alguns cliques, usando tipos de eventos pré-definidos para padronizar os dados."

---

## Slide 4: Tecnologias Utilizadas
- **Tópicos na tela:**
  - **Front-end:** Flutter (Dart) — Multiplataforma (Web & Mobile).
  - **Back-end/Banco de Dados:** Drift (SQLite) — Arquitetura Offline-First.
  - **Design:** Material Design em Dark Mode.
- **O que falar:** "Do lado técnico, escolhi o Flutter pela flexibilidade de rodar o mesmo código no navegador ou no celular. Para o banco de dados, usei o Drift com SQLite, garantindo que o app funcione de forma super rápida e offline na máquina do operador."

---

## Slide 5: O Banco de Dados (Modelo de Dados)
- **Imagem sugerida:** (Colocar um print do diagrama ER ou desenhar as duas tabelas).
- **Tópicos na tela:**
  - **Tabela Operador:** ID, Nome, Turno.
  - **Tabela Ocorrencia:** ID, Operador_ID (FK), Tipo, Descrição, Data/Hora, Status.
- **O que falar:** "O banco é relacional e bem direto. Temos a tabela de Operador e a tabela de Ocorrências com uma chave estrangeira, garantindo que saibamos exatamente quem registrou qual evento e a que horas."

---

## Slide 6: Arquitetura Reativa
- **Tópicos na tela:**
  - Uso de **Streams** e **StreamBuilder**.
  - A interface reage automaticamente às mudanças no banco de dados.
- **O que falar:** "Um destaque técnico é a arquitetura reativa. O aplicativo escuta as mudanças no banco. Se eu atualizo o status de uma ocorrência para 'Resolvido', a tela de listagem se atualiza sozinha no mesmo milissegundo, sem precisar recarregar a página."

---

## Slide 7: Demonstração ao Vivo
- **Ação:** (Mudar a tela do slide para o app rodando no Chrome).
- **Roteiro da Demo:**
  1. Digite seu nome e escolha um turno.
  2. Mostre a tela vazia.
  3. Clique no botão de '+' e crie uma "Atividade Suspeita".
  4. Mostre que ela apareceu na lista com a cor amarela.
  5. Edite o status da ocorrência para "Resolvido" e mostre a cor ficando verde.
- **O que falar:** "Vou demonstrar rapidamente o fluxo. Como podem ver, o Design Escuro foi pensado para não cansar a vista do operador que fica olhando telas o dia todo..."

---

## Slide 8: Próximos Passos
- **Tópicos na tela:**
  - Sincronização em Nuvem (Firebase / REST API).
  - Anexar fotos e recortes de vídeo na ocorrência.
  - Dashboard gerencial com gráficos.
- **O que falar:** "O projeto funciona muito bem localmente, mas como visão de futuro, o próximo passo seria sincronizar esse banco de dados local com um servidor na nuvem, permitindo gerar relatórios para os gestores."
