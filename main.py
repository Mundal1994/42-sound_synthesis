import pyaudio
import numpy as np
import matplotlib.pyplot as plt

class track:
	pitch = 'c'

def	callback(in_data, frame_count, time_info, status):
	data = frame_count
	return (data, pyaudio.paContinue)


p = pyaudio.PyAudio()
sampling_rate = 44100       # sampling rate, Hz, must be integer
volume = 0.5     # range [0.0, 1.0]

duration = 1   # in seconds, may be float
pitch = 300.0    # sine frequency, Hz, may be float
pitch2 = 200.0

#### Sine wave ####
sample1 = (np.sin(2*np.pi*np.arange(sampling_rate*duration)*pitch/sampling_rate)).astype(np.float32)
sample2 = (np.sin(2*np.pi*np.arange(sampling_rate*duration)*pitch2/sampling_rate)).astype(np.float32)

# Visualize the wave
# plt.plot(np.tile(samples, 2))
# plt.show()

# 'output = True' indicates that the sound will be played rather than recorded
# for paFloat32 sample values must be in range [-1.0, 1.0]
# stream = p.open(format=pyaudio.paFloat32,
# 				channels=1,
# 				rate=sampling_rate,
# 				output=True)	

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sampling_rate,
                output=True,
                stream_callback=callback)

# play. May repeat with different volume values (if done interactively) 
stream.write(volume*sample1)
stream.stop_stream()
stream.close()
# close PyAudio (7)
p.terminate()
