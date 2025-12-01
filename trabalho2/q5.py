import numpy as np
import matplotlib.pyplot as plt

def produto_esclar(a, b):
    

def ajuste_quadrados_minimos(log_n, log_tempos):
    """Ajuste por quadrados mínimos para dados linearizados sem utilizar funções estabelecidas."""
    
    # Calculando os coeficientes da regressão linear manualmente
    """n = len(log_n)
    soma_x = np.sum(log_n)
    soma_y = np.sum(log_tempos)
    soma_x2 = np.sum(log_n ** 2)
    soma_xy = np.sum(log_n * log_tempos)
    
    # Fórmulas do ajuste por mínimos quadrados
    b = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    log_a = (soma_y - b * soma_x) / n
    a = np.exp(log_a)  # Convertendo log(a) para a"""

    fi0 = np.array
    
    return a, b

# Exemplo de uso
def main():
    # Dados fictícios para demonstração
    n = np.array([10, 20, 40, 80, 160])  # Tamanhos de entrada
    tempos = np.array([0.01, 0.04, 0.16, 0.64, 2.56])  # Tempos correspondentes
    
    # Aplicando logaritmo
    log_n = np.log(n)
    log_tempos = np.log(tempos)
    
    # Ajustando
    a, b = ajuste_quadrados_minimos(log_n, log_tempos)
    
    # Gerando valores ajustados para o gráfico
    ajuste = a * n ** b
    
    # Plotando
    plt.scatter(n, tempos, label="Dados originais", color='red')
    plt.plot(n, ajuste, label=f"Ajuste: T(n) = {a:.4f} * n^{b:.4f}", color='blue')
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tamanho da entrada (n)")
    plt.ylabel("Tempo (T(n))")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()
    
    print(f"Coeficientes ajustados: a = {a:.4f}, b = {b:.4f}")

if __name__ == "__main__":
    main()