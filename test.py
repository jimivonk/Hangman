from random import randint

def random_word():
	han = open('words.txt', 'r')
	lst = []

	for line in han:
		word = line.strip()
		#word = line.split()
		word = line.split(', ')
		lst.append(word)
		words = lst[0]

	return words[randint(0,177)].upper()

for i in range(10):
    x = random_word()
    print("the word is", x, sep="")
