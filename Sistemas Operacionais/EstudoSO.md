### **1. Qual a finalidade da memória cache? Se a memória cache tivesse a mesma capacidade de armazenamento da memória principal, mesmo assim existiriam motivos para os dois tipos de memória existirem? Justifique sua resposta.**

A memória cache serve para armazenar dados mais acessados pela CPU de forma mais rápida que a memória principal.  
Mesmo que tivesse a mesma capacidade, ainda haveria vantagem, pois sua velocidade de acesso é muito maior.

---

### **2. Direct Memory Access (DMA) é um mecanismo que favorece a multiprogramação nos sistemas operacionais? Justifique.**

Sim. O DMA permite a transferência de dados entre memória e dispositivos de E/S sem intervenção da CPU, permitindo que ela execute outros processos simultaneamente, favorecendo a multiprogramação.

---

### **3. Um processo, durante seu ciclo de vida, pode assumir vários estados. Relacione estes estados e os eventos que devem acontecer para a mudança de estado, com as filas de escalonadores de um Sistema Operacional.**

Estados: Novo, Pronto, Em execução, Em espera, Finalizado.  
Novo -> O processo é criado.
Pronto -> O processo é colocado na fila de pronto, onde será executado assim que possível.
Em execução -> O processo é executado enquanto não há interrupção ou evento I/O. Encerrado na fila de execução. 
Em espera -> O processo é encaixado na fila de espera, onde aguarda o evento I/O acabar para ser retornado.
Finalizado -> O processo é finalizado, sendo retirado de qualquer fila.
---

### **4. Em um sistema operacional, um processo pode, em dado instante de tempo, assumir diferentes estados, como: em execução, pronto ou bloqueado (em espera). Considere as afirmativas abaixo sobre as possíveis transições entre esses estados que um processo pode realizar.**

I. Do estado em execução para o estado bloqueado ✅  
II. Do estado em execução para o estado pronto ✅  
III. Do estado pronto para o estado em execução ✅  
IV. Do estado pronto para o estado bloqueado ❌  
V. Do estado bloqueado para o estado em execução ✅  
VI. Do estado bloqueado para o estado pronto ✅  

**Alternativa correta:** (B) Somente as afirmativas I, II, III e VI são verdadeiras.

---

### **5. Considere o exemplo a seguir, com o uso da chamada fork(). Para responder às questões 5.a), 5.b), 5.c) e 5.d), considere o código a seguir:**

```c
int main() {
    int s = 5;
    if (fork() == 0) {
        s = 7;
        printf("Processo filho, s = %d\n", s);
    } else {
        wait(NULL);
        printf("Processo pai, s = %d\n", s);
    }
}
```

**5.a) Quantos processos existem neste exemplo?**  
➡️ 2 processos (pai e filho)

**5.b) Os processos utilizam o mesmo espaço de endereçamento? Justifique.**  
➡️ Não. Após o fork, cada processo possui seu próprio espaço de memória, com cópia dos valores.

**5.c) O que será impresso na tela pelos comandos printf?**  
```
Processo filho, s = 7
Processo pai, s = 5
```

**5.d) Nesse exemplo, foi utilizada a chamada wait. Explique como acontecerá a execução dos processos com esta chamada.**  
➡️ O processo pai executa `wait()`, aguardando o término do processo filho. Só depois disso ele continua a execução.

---

### **6. Considere o exemplo a seguir, com uso da chamada fork():**

```c
int main() {
    fork();
    fork();
    return 0;
}
```

**6.a) Quantos processos existirão quando esse código for executado?**  
➡️ 4 processos

**6.b) Qual a hierarquia dos processos?**  
➡️ Processo raiz cria dois processos, e um deles cria mais um, formando 4 ao total.

---

### **7. Em relação ao gerenciamento de processos, atribua V (verdadeiro) ou F (falso) às afirmativas a seguir.**

- (V) O Bloco de Controle de Processo (PCB) é utilizado para armazenar informações sobre processos.  
- (F) Threads apresentam maior custo de criação que processos.  
- (V) Um processo pode ser criado por uma chamada fork(), copiando o espaço de memória do processo original.

---

### **8. Explique a relação entre multiprogramação e o mecanismo de interrupções em um Sistema Operacional.**

Multiprogramação permite que vários processos compartilhem a CPU.  
As interrupções pausam a execução do processo atual para tratar eventos, como chamadas de E/S, e são essenciais para alternar entre processos.

---

### **9. Leia as afirmações a seguir:**

> **I**: Ao dividirem suas atividades em múltiplas threads que podem ser executadas paralelamente, aplicações podem se beneficiar mais efetivamente dos diversos núcleos dos processadores multicore.  
> **II**: O sistema operacional nos processadores multicore pode alocar os núcleos existentes para executar simultaneamente diversas sequências de código, sobrepondo execuções e reduzindo o tempo de resposta.

**Assinale a alternativa correta:**  
(A) As duas afirmações são verdadeiras, e a segunda justifica a primeira. ✅
