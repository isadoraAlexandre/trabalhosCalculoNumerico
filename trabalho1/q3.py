import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
    return x**2 + y**2

# Definindo o domínio
x = np.linspace(-5, 5, 40)
y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(x, y)

# Campo escalar
f = X**2 + Y**2

# Gradiente analítico
grad_fx = (func(X+0.01, Y) - func(X, Y)) / 0.01
grad_fy = (func(X, Y+0.01) - func(X, Y)) / 0.01

# Visualização do campo escalar // Visualização do gradiente
fig, axes = plt.subplots(1, 2, figsize=(11, 5))
c1 = axes[0].contourf(X, Y, f, levels=50, cmap='viridis')
plt.colorbar(c1, ax=axes[0], label='f(x, y)')
axes[0].set_title('Campo Escalar $f(x, y) = x^2 + y^2$')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].grid(True)

q = axes[1].quiver(X, Y, grad_fx, grad_fy, color='red', label='Gradiente Analítico')
axes[1].contour(X, Y, f, levels=50, cmap='viridis', alpha=0.4)
axes[1].set_title('Gradiente Analítico sobre o Campo Escalar')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')

plt.tight_layout()
plt.show()