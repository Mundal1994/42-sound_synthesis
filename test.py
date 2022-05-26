#pyAudio demo by RSAXVC
#Generates a transmit waveform of a near frequency,
#and plays it in a loop, while listening to the mic
#and plotting it

import pyaudio
import numpy as np
import struct
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Configuration Options
FS = 48000 #Sample Rate, Try 16000, 32000, 96000, 192000
FRAME_SIZE = 2048 #Try powers of two in the 256-8192 range
IDEAL_FREQ = 255.0 #ish, will be adjusted later
VOLUME = 0.1 #more is louder
CHANNELS = 1 #one or two please

#So to avoid regenerating our reference oscillators
#every packet, select the next lowest frequency that
#can align the oscillations to fit neatly into
#FRAME_SIZE. This means we can simply repeat
#a single block of samples without glitches
#and without doing any trig per callback
OSC_PER_FRAME = int(IDEAL_FREQ * FRAME_SIZE / FS)
ACTUAL_FREQ = float(OSC_PER_FRAME) * FS / FRAME_SIZE
print ("Actual Freq:",ACTUAL_FREQ,"Hz")

#Generate Reference Oscillator
samples_tx = VOLUME * (np.sin(2*np.pi*np.arange(FRAME_SIZE)/FRAME_SIZE*OSC_PER_FRAME)).astype(np.float32)

#Clean up any DC-bias
samples_tx = samples_tx - np.mean( samples_tx )
if CHANNELS == 2:
	#interleave samples for stereo
	samples_tx = np.repeat( samples_tx, 2 )

#initialize samples_rx so we don't have to worry about initialization race conditions with the plot
samples_rx = samples_tx

#define audio io callback
#This gets called with a block of incoming mic samples,
#and returns a block of outgoing speaker samples. Blocks are
#frame_count * CHANNELS long. It's important this not block too long
#or there will be glitches in the audio.
def callback(in_data, frame_count, time_info, status):
	global samples_rx
	in_data = struct.unpack( "f"*frame_count*CHANNELS, in_data )
	
	#To keep this function fast, just copy out to samples_rx
	samples_rx = in_data
	
	#Transmit/play samples_tx
	return (samples_tx, pyaudio.paContinue)

# instantiate PyAudio
p = pyaudio.PyAudio()

# open stream using callback
stream = p.open(format=pyaudio.paFloat32,
				channels=CHANNELS,
				rate=FS,
				output=True,
				# input=True,
				stream_callback=callback,
				frames_per_buffer=FRAME_SIZE)

# start the stream
stream.start_stream()

#Create a plot for animation
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	my_samples = samples_rx
	
	#Remove any DC-bias
	my_samples = my_samples - np.mean( my_samples )

	#Scale up amplitude for display
	my_samples = np.multiply( my_samples, VOLUME / np.max( my_samples ) )

	ax1.clear()
	if CHANNELS == 2:
		ax1.plot(samples_tx[0::2], label="TX")
		ax1.plot(my_samples[0::2], label="RX_L")
		ax1.plot(my_samples[1::2], label="RX_R")
	else:
		ax1.plot(samples_tx, label="TX")
		ax1.plot(my_samples, label="RX")

#Animate the wave-relationship until the user closes the window
#Try to draw at ~60Hz.
ani = animation.FuncAnimation(fig, animate, interval=16)
plt.show()
	
# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()