# Estudo sobre Sistemas Operacionais

## Chaveamento de Contexto
O chaveamento de contexto é o processo pelo qual um sistema operacional alterna entre diferentes processos ou threads em execução. Durante essa troca, o estado do processo atual é salvo e o estado do próximo processo a ser executado é restaurado. Esse mecanismo é essencial para a multitarefa e garante que os recursos do sistema sejam compartilhados de maneira eficiente entre os processos em execução.

## Interrupções
As interrupções são eventos que desviam temporariamente o fluxo normal de execução de um programa para tratar eventos assíncronos. O processamento de interrupções ocorre em diferentes classes, como:
- **Interrupções de Hardware**: Ocasionadas por dispositivos periféricos, como teclado e disco rígido.
- **Interrupções de Software**: Geradas por instruções do próprio programa, como exceções e chamadas de sistema.
- **Interrupções de Timer**: Utilizadas para garantir a alternância entre processos e manter a responsividade do sistema.
- **Interrupções de Falha de Página**: ocorrem quando um processo tenta acessar uma página de memória que não está carregada.

## Comunicação Interprocessos (IPC)
A comunicação entre processos (IPC) é fundamental para permitir que processos troquem informações e coordenem suas ações. Um dos mecanismos clássicos de IPC é o **Pipe**, que permite a comunicação unidirecional entre processos. 
### Exemplo de código com Pipe em C:
```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int fd[2];
    char mensagem[] = "Olá, processo filho!";
    char buffer[100];
    
    if (pipe(fd) == -1) {
        perror("Pipe falhou");
        exit(1);
    }
    
    if (fork() == 0) { // Processo filho
        close(fd[1]);
        read(fd[0], buffer, sizeof(buffer));
        printf("Processo filho recebeu: %s\n", buffer);
        close(fd[0]);
    } else { // Processo pai
        close(fd[0]);
        write(fd[1], mensagem, strlen(mensagem) + 1);
        close(fd[1]);
    }
    return 0;
}
```

## Estudo de Processos no UNIX
No UNIX, os processos são instâncias de execução de programas. Cada processo possui um identificador único (PID) e pode ser criado por meio da chamada de sistema `fork()`, que gera um novo processo filho a partir do processo pai. A comunicação e sincronização entre processos podem ser feitas por meio de sinais (`kill`), pipes e outros mecanismos de IPC.

## Melhorias no Chaveamento de Contexto
Ao longo dos anos, os sistemas operacionais aprimoraram o chaveamento de contexto para torná-lo mais eficiente. Melhorias incluem a introdução de técnicas como salvamento parcial de estado, onde apenas as partes essenciais do contexto são armazenadas e restauradas, reduzindo o tempo de chaveamento. 

Além disso, otimizações em hardware, como o uso de registradores dedicados para troca de contexto e mecanismos de preempção mais rápidos, tornaram o processo mais ágil. O suporte a **multithreading em nível de kernel** e estratégias de escalonamento aprimoradas também contribuíram para diminuir a latência e melhorar o desempenho dos sistemas modernos.
