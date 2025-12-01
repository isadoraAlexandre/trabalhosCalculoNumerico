import numpy as np

#função para teste, retorna a inversa já calculada
def inversa(A):
    B = [[0.25, 0.125],
         [0.125, 0.3125]]
    return B

def condMatriz(A):
    """
    Calcula o número de condição de uma matriz A utilizando a norma-2.
    
    Parâmetros:
        A (numpy.ndarray): Matriz quadrada.
        
    Retorna:
        float: Número de condição da matriz A.
    """
    
    norma_A = np.linalg.norm(A, ord=2)
    A_inv = inversa(A) #função inversa()
    norma_A_inv = np.linalg.norm(A_inv, ord=2)
    
    cond = norma_A * norma_A_inv
    
    return cond

A = np.array([[5, -2], [-2, 4]], dtype=float)
cond = condMatriz(A)
print(f'{cond:.2f}')