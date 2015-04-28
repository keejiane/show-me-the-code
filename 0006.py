# -*- coding:utf-8 -*-
import os
import re

def getFile(path):
	f = os.listdir(path)
	Files = []
	for fp in f:
		fp_path = path + '\\' + fp
		if (os.path.isfile(fp_path)):
			Files.append(fp_path)
		elif(os.path.isdir(fp_path)):
			Files += getFile(fp_path)
	return Files

def getKeyWord(Files):
	worddict = {}
	for af in Files:
		f = open(af,'r+')
		s = f.read()
		words = re.findall(r'[a-zA-Z0-9]+',s)
		for w in words:
			if w in worddict:
				worddict[w] += 1
			else:
				worddict[w] = 1
		f.close()
		wordsort = sorted(worddict.items(),key = lambda e:e[1],reverse = True)
		print "In this article:'%s'" %af
		print "The Keyword Is '%s', It repeats %s times" %(wordsort[0][0],wordsort[0][1])
	return wordsort

if __name__ == '__main__':
	files = getFile('c:\\TextFile\\TextDic')
	print files
	wordsort = getKeyWord(files)
	maxnum = 1
	for i in range(len(wordsort) - 1):
		if wordsort[i][1] == wordsort[i + 1][1]:
			maxnum += 1
		else:
			break
	for j in range(maxnum):
		print wordsort[j]

