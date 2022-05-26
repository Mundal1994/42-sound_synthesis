import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# def	callback(in_data, frame_count, time_info, status):
# 	data = readframes(frame_count)
# 	return (data, pyaudio.paContinue)
def play_note(note):
    p = pyaudio.PyAudio()
    # Specs
    sample_rate = 44100       # sampling rate, Hz, must be integer
    volume = 0.5     # range [0.0, 1.0]
    duration = 2   # in seconds, may be float
    pitch = 131.87    # sine frequency, Hz, may be float
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)
                    # input=True)
                    # stream_callback=callback)	

    # play. May repeat with different volume values (if done interactively) 
    # stream.write(volume*one_cycle)
    stream.write(volume*note)
    stream.stop_stream()
    stream.close()
    # close PyAudio (7)
    p.terminate()

sample_rate = 44100
duration = 0.5

freqs = [261.63, 293.66, 329.63, 369.99, 392.00, 440.00, 493.88, 523.25]
notes = []
for freq in freqs:
    note = (np.sin(2 * np.pi * np.arange(sample_rate * duration)*freq / sample_rate)).astype(np.float32)
    notes.append(note)
for note in notes:
    play_note(note)