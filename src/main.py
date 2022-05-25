#!/usr/bin/env python3
import sys, getopt

def	filter_track(f):
	lines = f.readlines()
	for line in lines:
		if (line[0] != '#' or line[0] != '\n'):
			print (line, end="") # Remove all new lines
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

