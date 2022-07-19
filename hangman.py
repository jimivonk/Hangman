#Hangman game. Player must make guesses of letters to choose random word before man is hanged.
import time
from random import randint

#Add option to keep playing, keeping same name and score of wins and losses

def main():
	count = 8
	correct = []
	incorrect = []
	name = intro()
	word = random_word()
	word_list = list(word)
	print(word)

	while len(incorrect) < 8:
		print(word_hide(word_list, correct))
		
		letter = guess(input('guess a letter: ').upper())
		if letter in word_list:
			if letter not in correct:
				print("true")
				correct.append(letter)
				print(f"Well done! You chose {letter}\n CORRECT ATTEMPTS: {correct}\n INCORRECT ATTEMPTS {incorrect}")
				print(word_hide(word_list, correct))
				if word == word_hide(word_list, correct):
					print(f"How partner, you just goddam won the game. It turns out you are a hero afterall\n I name thee {name} the saviour!!!")
					quit()
			else:
				print(f"Howdy cowboy! You guessed {letter} already")
				
		else:
			incorrect.append(letter)
			print(f"Bad choice! you guessed {letter}\n CORRECT ATTEMPTS: {correct}\n INCORRECT ATTEMPTS {incorrect}")
			print(word_hide(word_list, correct))


	print(name, word, letter)

# Use input section
def intro():
	print('Welcome to this game of life and death. A game where each wrong step, sends an innocent man closer to his doom, Will you be a hero or a failure?')
	time.sleep(2)
	user = input("Tell me your name wanna be hero: ")
	user = user.strip().title()
	time.sleep(1)
	print('Hello %s, let the game commence!!'%user)
	return user

#Run through the  word list and select random word
def random_word():
	han = open('words.txt', 'r')
	lst = []

	for line in han:
		word = line.strip()
		word = line.split(', ')
		lst.append(word)
		words = lst[0]

	return words[randint(0,177)].upper()

#return user guess. accept only a single letter guess. prompt to reguess if answer invalid
def guess(shot):
    if len(shot) != 1 or shot.isupper() is False:
        print('Please type ONLY one LETTER!!No Numbers, no grammar!!!')
        return guess(guess(input('guess a letter: ').upper()))
    else:
        return shot

# provide up to date graphic of positioned correct letters and missing letters
def word_hide(wordlist, cor):
    letters = []
    for letter in wordlist:
        if letter not in cor:
            letters.append('*')
        else:
            letters.append(letter)
            continue
    return "".join(letters)

main()