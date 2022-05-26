#!/usr/bin/env python3
import sys, getopt
import pyaudio
import numpy as np


class track:
	pitch = 'c'
	

def	sound():
	p = pyaudio.PyAudio()
	volume = 0.5     # range [0.0, 1.0]
	fs = 44100       # sampling rate, Hz, must be integer

	duration = 1.0   # in seconds, may be float
	pitch = 440.0    # sine frequency, Hz, may be float

	# generate samples, note conversion to float32 array
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*pitch/fs)).astype(np.float32)	
	for test in samples:
		print (samples)

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

def	filter_track(file):
	lines = [line for line in file.readlines() if line.strip()]
	# for line in lines:
		# print (line)


def main(argv, argc):
	#//print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)
	if argc == 2:
		f = open(argv[1], "r")
		# filter_track(f)
		sound()
		# print(f.read())
	else:
		print("Usage: ./minisynth /path/to/file")

if __name__ == "__main__":
	main(sys.argv, len(sys.argv))

