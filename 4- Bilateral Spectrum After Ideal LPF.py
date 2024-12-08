
# x(t) = 5 cos(2π 2000 t) + 3 cos(2π 3000 t)

import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f1, f2 = 2000, 3000  # Frequencies in Hz
A1, A2 = 5, 3        # Amplitudes
fs = 8000            # Sampling frequency in Hz
fc = 4000            # Cutoff frequency for LPF in Hz

# Create frequency axis up to 20 kHz for plotting
f = np.linspace(-20000, 20000, 20000)  # Bilateral axis for full spectrum analysis

# Function to create spectrum of a cosine wave
def cosine_spectrum(A, f0, f):
    spectrum = np.zeros_like(f)
    spectrum += (A/2) * (np.abs(f - f0) < 1)  # Positive frequency delta
    spectrum += (A/2) * (np.abs(f + f0) < 1)  # Negative frequency delta
    return spectrum

# Function to create spectrum of a sampled cosine
def sampled_cosine_spectrum(A, f0, fs, f):
    spectrum = np.zeros_like(f)
    for k in range(-5, 6):  # Consider replicas up to ±5*fs
        spectrum += cosine_spectrum(A, f0 + k*fs, f)
    return spectrum

# Calculate spectrums
original_spectrum = cosine_spectrum(A1, f1, f) + cosine_spectrum(A2, f2, f)
sampled_spectrum = sampled_cosine_spectrum(A1, f1, fs, f) + sampled_cosine_spectrum(A2, f2, fs, f)


# Create ideal lowpass filter
H = np.where(np.abs(f) <= fc, 1, 0)  # LPF filter for bilateral spectrum
recovered_spectrum = sampled_spectrum * H


#-------------------------------------------

#Bilateral Spectrum of Sampled Signa

recovered_spectrum = sampled_spectrum * H

plt.figure(figsize=(6, 4))
plt.plot(f/1000, recovered_spectrum)
plt.title('Bilateral Spectrum after Ideal LPF')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(-20, 20)
plt.tight_layout()
plt.show()

