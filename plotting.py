import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5,5,100)
def f(x):
	return np.sin(x)/(1+x**2)

plt.plot(t, f(t))
plt.show()