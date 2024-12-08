import numpy as np
import matplotlib.pyplot as plt

# Time vector
n = np.arange(-10, 10, 1)

# Unit step sequence


# Create unit step sequence u[n]
def u(n):
    return np.heaviside(n, 1)

# Generate signal
u_n = u(n)

# Plot signals
plt.figure(figsize=(12, 4))

# Plot u[n]
plt.subplot(1, 3, 1)
plt.stem(n, u_n)
plt.title('Unit Step sequence u[n]')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.show()


