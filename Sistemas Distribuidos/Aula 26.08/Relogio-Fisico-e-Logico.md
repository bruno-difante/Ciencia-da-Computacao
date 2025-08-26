# ⏰ Relógios Físicos e Lógicos / Exclusão Mútua / Eleição de Líder

## 1. Relógios Físicos  

### Conceito  
O **relógio físico** é o relógio real de um computador ou dispositivo, baseado em hardware. Ele mede o tempo cronológico (segundos, milissegundos, etc.) e pode ser acessado pelo sistema operacional (ex.: `System.currentTimeMillis()` em Java).  

### Problema  
Em sistemas distribuídos, cada máquina mantém seu próprio relógio, e pequenas diferenças podem gerar inconsistências, já que não existe um “tempo absoluto” perfeito.  

**Exemplo:**  
- Computador A: evento X → 10:00:01  
- Computador B: evento Y → 09:59:59  

Na prática, X pode ter ocorrido depois de Y, mas os relógios estão **desalinhados**.  

---

## 2. Relógios Lógicos  

### Conceito  
O **relógio lógico** não mede tempo real, mas sim a **ordem dos eventos**. É usado em sistemas distribuídos para definir o que aconteceu antes ou depois, independentemente do relógio físico.  

- Criado por **Leslie Lamport (1978)** → **Relógio de Lamport**.  
- Cada processo mantém um contador lógico `L`.  

### Regras básicas  
1. Evento local: `L = L + 1`  
2. Ao enviar mensagem: incluir `L` junto.  
3. Ao receber mensagem: `L = max(L, L_mensagem) + 1`.  

**Exemplo:**  
- Processo A envia mensagem com `L = 2`.  
- Processo B tinha `L = 0`.  
- Ao receber: `L = max(0,2)+1 = 3`.  

Assim, B sabe que o evento de A ocorreu antes do recebimento.  

---

### Diferenças  

| Relógio Físico ⏱️ | Relógio Lógico 🕹️ |
|-------------------|-------------------|
| Mede tempo real (horas:minutos:segundos) | Mede ordem de eventos |
| Pode estar errado/desincronizado | Não depende do tempo real |
| Útil para timestamps reais | Útil para consistência em sistemas distribuídos |

---

### Aplicações práticas  

- **Bancos:** relógio lógico garante que um depósito seja registrado antes de um saque.  
- **Git:** usa timestamps físicos, mas a ordem real vem da estrutura de commits (DAG).  
- **Protocolos (Paxos, Raft):** garantem ordem correta de logs e eleição de líderes.  

---

### Exemplo Java (Relógio Lógico)

```java
class Processo {
    private int id;
    private int L = 0; // relógio lógico

    public Processo(int id) { this.id = id; }

    public int eventoLocal() {
        L++;
        System.out.println("Processo " + id + " evento local. L=" + L);
        return L;
    }

    public int enviarMensagem() {
        L++;
        System.out.println("Processo " + id + " envia mensagem. L=" + L);
        return L;
    }

    public void receberMensagem(int L_msg) {
        L = Math.max(L, L_msg) + 1;
        System.out.println("Processo " + id + " recebe mensagem. L=" + L);
    }
}

public class Simulacao {
    public static void main(String[] args) {
        Processo A = new Processo(1);
        Processo B = new Processo(2);

        A.eventoLocal(); 
        int L_msg = A.enviarMensagem(); 
        B.receberMensagem(L_msg); 
        B.eventoLocal(); 
        int L_msg2 = B.enviarMensagem(); 
        A.receberMensagem(L_msg2);
        A.eventoLocal(); 
    }
}
```

| Passo | Evento          | Processo | L final |
|-------|-----------------|----------|---------|
| 1     | Evento local    | A        | 1       |
| 2     | Envia msg       | A        | 2       |
| 3     | Recebe msg      | B        | 3       |
| 4     | Evento local    | B        | 4       |
| 5     | Envia msg       | B        | 5       |
| 6     | Recebe msg      | A        | 6       |
| 7     | Evento local    | A        | 7       |

---

## 3. Exclusão Mútua  

### Conceito  
A exclusão mútua garante que apenas **um processo por vez** acesse uma **seção crítica** (ex.: impressora, banco de dados).  

### Propriedades  
1. **Mutualidade:** no máximo um processo na seção crítica.  
2. **Progresso:** se a seção está livre, alguém deve entrar.  
3. **Espera limitada:** nenhum processo fica esperando para sempre.  

### Exemplo em Java  

```java
class Recurso {
    public synchronized void acessar(int id) {
        System.out.println("Processo " + id + " entrou na seção crítica");
        try { Thread.sleep(1000); } catch (InterruptedException e) {}
        System.out.println("Processo " + id + " saiu da seção crítica");
    }
}

public class Exclusao {
    public static void main(String[] args) {
        Recurso r = new Recurso();
        new Thread(() -> r.acessar(1)).start();
        new Thread(() -> r.acessar(2)).start();
    }
}
```

👉 O `synchronized` em Java garante **exclusão mútua**: apenas uma thread por vez executa o método.  

---

## 4. Eleição de Líder  

### Conceito  
Em sistemas distribuídos, pode ser necessário eleger um **líder** para coordenar decisões (ex.: backups, controle de recursos).  
A eleição acontece quando:  
1. Não existe líder.  
2. O líder atual falha.  

---

### Algoritmo de Bully  

1. Cada processo tem um **ID único**.  
2. Quando detecta falha, um processo inicia eleição.  
3. Ele envia mensagens para processos com **ID maior**.  
4. Se ninguém responde, ele vira líder.  
5. Se alguém responde, o maior assume a eleição.  

### Exemplo em Java  

```java
class Processo {
    int id;
    boolean lider = false;

    public Processo(int id) { this.id = id; }

    public void eleger(Processo[] processos) {
        boolean existeMaior = false;
        for (Processo p : processos) {
            if (p.id > this.id) {
                System.out.println("Proc " + id + " envia msg para " + p.id);
                existeMaior = true;
            }
        }
        if (!existeMaior) {
            lider = true;
            System.out.println("Proc " + id + " é o líder!");
        }
    }
}

public class Eleicao {
    public static void main(String[] args) {
        Processo[] p = { new Processo(1), new Processo(2), new Processo(3) };
        p[0].eleger(p); // Processo 1 inicia
    }
}
```

---

## ✅ Resumo Final  

- **Relógio físico:** tempo real, mas sujeito a erros.  
- **Relógio lógico:** ordem causal de eventos.  
- **Exclusão mútua:** apenas um processo acessa a seção crítica.  
- **Eleição de líder:** garante coordenação em sistemas distribuídos.  
