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

# SO - Lista 6
## 1 - a)
| prox. ins  | prox. item  | exc. mutua | esp. vaga | esp. dado |
|------------|-------------|------------|-----------|-----------|
|      0     |      0      |      1     |     3     |     0     |
|      1     |      1      |      0     |     2     |    -1     |
|            |             |      1     |     2     |     0     |
|            |             |      0     |           |           |

## b) 

## c) 
- exclusao_mutua = proteger a seção crítica
- espera_vaga = o produtor somente insere se tiver vaga
- espera_dado = controla o número de itens no buffer. se estiver vazio (0), bloqueia o consumidor
