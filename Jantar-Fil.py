import threading
import time
import random

N = 5  # número de filósofos
garfos = [threading.Lock() for _ in range(N)]
limite = threading.Semaphore(N - 1)  # evita deadlock

def filosofo(i, refeicoes=3):
    for _ in range(refeicoes):  # cada filósofo vai comer um número finito de vezes
        print(f"Filósofo {i} está pensando...")
        time.sleep(random.uniform(1, 2))

        print(f"Filósofo {i} está com fome.")
        limite.acquire()

        garfo_esq = i
        garfo_dir = (i + 1) % N

        garfos[garfo_esq].acquire()
        garfos[garfo_dir].acquire()

        print(f"Filósofo {i} está comendo...")
        time.sleep(random.uniform(1, 2))

        garfos[garfo_esq].release()
        garfos[garfo_dir].release()
        limite.release()

        print(f"Filósofo {i} terminou de comer e voltou a pensar.\n")

# Cria e inicia as threads
threads = []
for i in range(N):
    t = threading.Thread(target=filosofo, args=(i,))
    threads.append(t)
    t.start()

# Aguarda todos terminarem
for t in threads:
    t.join()

print("Todos os filósofos comeram e o programa terminou.")
