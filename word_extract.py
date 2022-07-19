from random import randint

#Run through the  word list and select random word
han = open('words.txt', 'r')
lst = []

for line in han:
	word = line.rstrip()
	word = line.split()
	word = line.split(',')
	lst.append(word)
	words = lst[0]
for word in words:
        bigword = word
        if len(word) > len(bigword):
                bigword = word

print(bigword, len(bigword))

#chosen = words[randint(0,177)]
#print(words[chosen])
#print(chosen)
