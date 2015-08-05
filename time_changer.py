#!/usr/bin/python

import sys
import os
from time_check import parse


def main(argv):

	directory = argv[0]
	filetype = argv[1]
	moddate = argv[2]
	modtime = argv[3]

	try:
		parse(directory, filetype, moddate, modtime)
		
	except BaseException as e:
		print('Error', e)

if __name__ == "__main__":
	main(sys.argv[1:])