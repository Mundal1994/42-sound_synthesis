from dataclasses import asdict
from tracemalloc import stop
import pyaudio
import numpy as np
#import matplotlib.pyplot as plot
#from scipy import signal
import math

def play_note(note):
    p = pyaudio.PyAudio()
    volume = 0.5
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)
    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*note)
    stream.stop_stream()
    stream.close()
    # close PyAudio (7)
    p.terminate()

def convert_note_to_hz(char):
    file = open("notes.txt", 'r')
    lines = file.readlines()
    for line in lines:
        # print(note)
        if (char in line):
            arr = line.split()
            hz = float(arr[1])
    file.close()
    return (hz)

sample_rate = 44100
duration = 0.5
freqs = []

hz = convert_note_to_hz("C5")
freqs.append(hz)
# freqs = freqs.astype(float)
print(freqs)
notes = []
duration=1.5
sampling_rate=44100
### Sin waves ####
for freq in freqs:
	frames = int(duration*sampling_rate)
	note = np.cos(2*np.pi*hz*np.linspace(0,duration,frames))
	
	#note = (np.sin(2 * np.pi * np.arange(sample_rate*duration)*freq/sample_rate)).astype(np.float32)
	#square wave
	note = np.clip(10*note, -1, 1)

	#triangular wave
	#note = np.cumsum(np.clip(note*10, -1, 1))
	#note = note/max(np.abs(note))
	notes.append(note)

for note in notes:
	play_note(note)