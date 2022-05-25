#!/usr/bin/env python3
import sys, getopt

class Person:
	def __init__(self, name, age):
    	self.pitch = pitch
   	 	self.volume = volume
		self.


class track:
	def __init__(self, str, index):
    	self.str = str
		self.index = index


def	filter_track(f):
	lines = f.readlines()
	tempo = 'tempo'
	class track:
		tempo = 0
		tracks = ''
	for line in lines:
		if (line[0] != '#' or line[0] != '\n'):
			print (line, end="") # Remove all new lines
		if tempo in line:
			for word in line.split():
				if word.isdigit():
					track.tempo = int(word)

		
	# print (line)
	# print (line[0])

def main(argv, argc):
	#//print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)
	if argc == 2:
		f = open(argv[1], "r")
		filter_track(f)	
		print(f.read())
	else:
		print("Usage: ./minisynth /path/to/file")

if __name__ == "__main__":
	main(sys.argv, len(sys.argv))

