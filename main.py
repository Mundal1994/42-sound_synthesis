import pyaudio
import numpy as np
import matplotlib.pyplot as plt

class track:
	pitch = 'c'

p = pyaudio.PyAudio()
sampling_rate = 44100       # sampling rate, Hz, must be integer
volume = 0.5     # range [0.0, 1.0]

duration = 1   # in seconds, may be float
pitch = 150.0    # sine frequency, Hz, may be float

samples = (np.sin(2*np.pi*np.arange(sampling_rate*duration)*pitch/sampling_rate)).astype(np.float32)

# Visualize the wave
# plt.plot(np.tile(samples, 2))
# plt.show()

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
				channels=1,
				rate=fs,
				output=True)	

# play. May repeat with different volume values (if done interactively) 
stream.write(volume*samples)	
stream.stop_stream()
stream.close()
p.terminate()
