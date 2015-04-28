# -*- coding:utf-8 -*-
import os

def getFiles(path):
	fd = os.listdir(path)
	files = []
	for f in fd:
		fd_path = path + '\\' + f
		if (os.path.isfile(fd_path)):
			fd_split = fd_path.split('.')
			if fd_split[1] == "py":
				files.append(fd_path)
			else:
				continue
		else:
			files += getFiles(fd_path)
	return files 

def countLine(files):
	for af in files:
		line,blank,note = 0,0,0
		f = open(af,'rb')
		s = f.readlines()
		line = len(s)
		for i in s:
			if i[0] == '#' or i[0] == '/':
				note += 1
			elif i == " ":
				blank += 1
		f.close()
		print 'line:%s, blank:%s, note:%s' % (line,blank,note)
	return (line,blank,note)

files = getFiles('c:\\pytest')
print files
countLine(files)
	
