#!/usr/bin/python

import time
import datetime
import sys
import os
import glob
from pandas import DataFrame
 

def parse(dirpath, filetype, moddate, modtime):

	dirpath = ' '.join(dirpath.split())

	fullpath = dirpath + '/*.' + filetype

	modtime = moddate + ' ' + modtime

	if os.path.isdir(dirpath) == True:
		
		try:
			# current times
			modified_times = []
			for f in glob.glob(fullpath):
				mtime = os.path.getmtime(f)
				modified_times.append(datetime.datetime.fromtimestamp(mtime))
				
			# files in directory
			current_files = [f for f in glob.glob(fullpath)]

			# changed times
			changed_times = []
			for f in glob.glob(fullpath):
			    t = time.mktime(time.strptime(modtime,\
			     							  '%d.%m.%Y %H:%M:%S'))
			    os.utime(f,(t,t))
			    changed_times.append(datetime.datetime.fromtimestamp(t))


			data = {'Files in directory': current_files,
					'Modified times': modified_times,
					'Changed times': changed_times }

			frame = DataFrame(data, columns=['Files in directory',\
											 'Modified times','Changed times'])

			print frame

		except BaseException as e:
			print('Something when wrong', e)

		finally:
			print('program end')
			

