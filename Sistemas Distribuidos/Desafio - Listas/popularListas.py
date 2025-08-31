import threading
import random

n = 100000   # quantidade total de números
m = 10       # quantidade de listas 
# quantidade de números exigida pelo desafio
min_val = 1000 
max_val = 100000

# criar m listas vazias
listas = [[] for _ in range(m)]

# função para popular as listas
def popula_lista(lista, quantidade):
    for _ in range(quantidade):
        lista.append(random.randint(min_val, max_val))

# iniciar threads
threads = []
quantidade_por_lista = n // m

for i in range(m):
    t = threading.Thread(target=popula_lista, args=(listas[i], quantidade_por_lista))
    threads.append(t)
    t.start()

# esperar as threads terminarem
for t in threads:
    t.join()

# cálculo de média
todos_numeros = [num for lista in listas for num in lista]
media = sum(todos_numeros) / len(todos_numeros)

print(f"Total de listas: {m}")
print(f"Tamanho de cada lista: {quantidade_por_lista}")
print(f"Quantidade total de números: {len(todos_numeros)}")
print(f"Média geral: {media:.2f}")
