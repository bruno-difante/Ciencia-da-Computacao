## **1. Qual a finalidade da memória cache?**
A memória cache armazena dados frequentemente acessados para acelerar a leitura da memória.  
Mesmo que tivesse a mesma capacidade da memória principal, a cache ainda seria útil por ser muito mais rápida.

---

## **2. O que é DMA (Direct Memory Access)?**
É um mecanismo que permite que dispositivos de E/S acessem diretamente a memória, sem intervenção da CPU.  
Isso favorece a multiprogramação pois libera a CPU para outras tarefas enquanto o acesso ocorre.

---

## **3. Ciclo de vida de um processo**
### Transições válidas entre estados:
- I. Execução → Bloqueado ✅  
- II. Execução → Pronto ✅  
- III. Pronto → Execução ✅  
- IV. Pronto → Bloqueado ❌  
- V. Bloqueado → Execução ✅  
- VI. Bloqueado → Pronto ✅  

✅ **Gabarito correto: B — I, II, III e VI são verdadeiras**

---

## **4. Código com `fork()`**
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

### **5.a) Quantos processos existem neste exemplo?**  
➡️ **2** (pai e filho criados pelo `fork()`)

### **5.b) Utilizam o mesmo espaço de endereçamento?**  
➡️ **Não.** Cada processo tem sua própria cópia do espaço de memória.

### **5.c) Saída esperada do programa:**  
```
Processo filho, s = 7
Processo pai, s = 5
```

### **5.d) O que faz a chamada `wait()`?**  
➡️ O processo pai espera o término do processo filho antes de continuar.

---

## **6. Código com múltiplos `fork()`**
```c
int main() {
    fork();
    fork();
    return 0;
}
```

### **6.a) Quantos processos são criados?**  
➡️ **4 processos** ao total.

### **6.b) Hierarquia dos processos:**  
```
P → P1
  → P2
     → P3
```

---

## **7. Julgue como V ou F**
- ✅ **(V)** PCB armazena dados de processo e ajuda no contexto de troca.
- ❌ **(F)** Threads não têm maior custo de criação que processos.
- ✅ **(V)** fork() cria processo com mesmo conteúdo de memória.

---

## **8. Multiprogramação vs Interrupções**
- **Multiprogramação**: execução de vários processos na CPU de forma concorrente.  
- **Interrupções**: eventos que pausam o processo atual para tratar ações urgentes.

---

## **9. Threads e processadores multicore**
**Afirmações:**
- Aplicações com múltiplas threads aproveitam melhor núcleos múltiplos ✅  
- SO aloca múltiplos núcleos para sequências diferentes de código ✅  

✅ **Gabarito: A — As duas são verdadeiras e a segunda justifica a primeira**
