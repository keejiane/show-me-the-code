# -*- coding:utf-8 -*-

import os

f = open('filtered_words.txt','r')
data = f.read().split('\n')

def checkWord(words):
	flag = False
	for w in data:
		if words.find(str(w)) >= 0:
			flag = True
			ws = words.split(str(w))
			break
		else:
			pass
	if flag == True:
		print ws[0] + "*" + ws[1]
	else:
		print words

while True:
	words = str(raw_input('Please input:'))
	checkWord(words)
