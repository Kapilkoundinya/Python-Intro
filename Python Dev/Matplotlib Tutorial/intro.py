import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)


# Plot function
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(['Sine', 'Cosine'])
plt.title("Sine and Cosine Plots")
plt.show()

