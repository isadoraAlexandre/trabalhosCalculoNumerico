#A
import numpy as np
import matplotlib.pyplot as plt
import math

def z1_exata(t, w):
    return np.cos(t * w)

def z2_exata(t, w):
    return -w * np.sin(w * t)

w = 2.0
v0 = 0
y0 = 1
tf = 10.0
dt = 0.01
nt = int(tf/dt) + 1

t = np.linspace(0, tf, nt)
z1 = np.zeros(nt)
z2 = np.zeros(nt)
z1e = z1_exata(t, w)
z2e = z2_exata(t, w)

z1[0] = y0
z2[0] = v0

for n in range(0, nt-1):
    z1[n+1] = z1[n] + dt * z2[n]
    z2[n+1] = z2[n] - dt * w**2 * z1[n]

# Plotagem dos resultados
plt.plot(t, z1, label="z1", color='blue')
plt.plot(t, z1e, color='blue', linestyle='--', label="Solução exata")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend(loc="best")
plt.title("Comparação z1")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

plt.plot(t, z2, label="z2", color='orange')
plt.plot(t, z2e, color='orange', linestyle='--', label="Solução exata")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend(loc="best")
plt.title("Comparação z2")
plt.xlabel('t')
plt.ylabel("y'(t)")
plt.show()

#B
import numpy as np
import matplotlib.pyplot as plt
import math

def z1_exata(t, w):
    return np.cos(t * w)

w = 2.0
v0 = 0
y0 = 1
tf = 10.0
t = np.linspace(0, tf, nt)
z1e = z1_exata(t, w)

valores_dt = [0.005, 0.01, 0.05, 0.1, 0.2]

for dt in valores_dt:
  nt = int(tf/dt) + 1
  t_dt = np.linspace(0, tf, nt)
  z1 = np.zeros(nt)
  z2 = np.zeros(nt)
  
  z1[0] = y0
  z2[0] = v0

  for n in range(0, nt-1):
      z1[n+1] = z1[n] + dt * z2[n]
      z2[n+1] = z2[n] - dt * w**2 * z1[n]
  
  plt.plot(t_dt, z1, label=f"$h = {dt}$")

plt.plot(t, z1e, color='black', linestyle='--', label="Solução exata")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend(loc="best")
plt.title("Teste com valores diferentes de delta t")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()