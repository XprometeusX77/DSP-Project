
import numpy as np
import matplotlib.pyplot as plt

# Time vector
n = np.arange(-10, 10, 1)

#Shifted unit impulse


# Create shifted unit impulse δ[n-2]
def delta(n, k):
    return np.array([1 if i == k else 0 for i in n])

# Generate signal
delta_n = delta(n, 2)  # δ[n-2]

# Plot signal
plt.figure(figsize=(12, 4))

# Plot δ[n-2]
plt.subplot(1, 3, 2)
plt.stem(n, delta_n)
plt.title('Shifted unit impulse δ[n-2]')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.show()