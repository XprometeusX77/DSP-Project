import numpy as np
import matplotlib.pyplot as plt

# Time vector
n = np.arange(-10, 10, 1)

# Create unit step function u[n]
def u(n):
    return np.heaviside(n, 1)

# Create delta function δ[n-2]
def delta(n, k):
    return np.array([1 if i == k else 0 for i in n])

# Generate signals
u_n = u(n)
delta_n = delta(n, 2)  # δ[n-2]

# Plot signals
plt.figure(figsize=(12, 4))

# Plot u[n]
plt.subplot(1, 3, 1)
plt.stem(n, u_n)
plt.title('Unit Step u[n]')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot δ[n-2]
plt.subplot(1, 3, 2)
plt.stem(n, delta_n)
plt.title('Impulse δ[n-2]')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('Amplitude')

# Perform convolution
# The convolution of u[n] with δ[n-2] is just u[n-2]
n_conv = np.arange(-10, 10, 1)
conv_result = u(n_conv - 2)  # Shift the unit step by 2

plt.subplot(1, 3, 3)
plt.stem(n_conv, conv_result)
plt.title('Convolution: (u[n] * δ[n-2])')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
