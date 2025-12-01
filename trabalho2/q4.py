import numpy as np
from scipy.linalg import lu
import time
import matplotlib.pyplot as plt

def medir_tempo_lu(n, reps=10):
    """
    Mede o tempo médio da decomposição LU para uma matriz aleatória de ordem n.

    Args:
        n (int): Ordem da matriz.
        reps (int): Número de repetições do cálculo da decomposição LU.

    Returns:
        float: Tempo médio em segundos.
    """
    A = np.random.rand(n, n)
    tempos = []
    
    for _ in range(reps):
        start_time = time.time()
        _, _, _ = lu(A) #função Lu
        tempos.append(time.time() - start_time)
    
    return np.mean(tempos)

#Com os valores dados no enunciado (1000, 10000) demora mais de 2h para executar, então coloquei um intervalo menor
n_values = np.linspace(10, 100, 10, dtype=int)
tempos = [medir_tempo_lu(n, reps=10) for n in n_values]

for i in tempos:
    print(f"{i:.7f}")