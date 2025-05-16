# Mecanismos de Sincronização
##### Conceitos
- processos cooperativos
- seção crítica
- condição de corrida
- proteção da seção crítica (condições para)

##### Proteção da seção crítica
- protocolos de acesso
- spin-lock
- ...

## Semáforo -> tipo de dado abstrato
- um valor inteiro
- uma fila de processos
- duas operações sobre o semáforo
1. P = proberen (testar - wait - down)
2. V = verhogen (incrementar - signal - up - post)
- operações atômicas (não podem ser interrompidas)

##### Operação P
- Decrementa em um o valor do semáforo
- Testa o valor do semáforo

##### Operação V
- Incrementa em um o valor do semáforo
- Se existe processo na fila do semáforo, sinaliza-o
  
