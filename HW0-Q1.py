# Hw0 for MLFALL2017
with open('words.txt') as f1:
	f1 = f1.read()

word_list = f1.strip().split(' ')

with open('Q1.txt','w+') as f:
	word_count = dict()
	for i, word in enumerate(word_list):
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
		if i == len(word_list) - 1:
			f.write(word + ' '+ str(i) +' ' + str(word_count[word]))
		else:
			f.write(word + ' '+ str(i) +' ' + str(word_count[word]) + '\n')
