if __name__ == '__main__':
	ori = open('/home/cyno/corpus/ap/ap.txt')
	outi = open('/home/cyno/corpus/ap/applain.txt','w')
	i = 0
	flag = 0
	for line in ori:
		if line == '<TEXT>\n':
			flag = 1
			i += 1
			continue
		if flag == 1:
			if line != ' </TEXT>\n':
				outi.writelines(line)
			elif line == ' </TEXT>\n':
				flag = 0
	ori.close()
	outi.close()
	print i
