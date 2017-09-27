import math

def squareChecker(number):
	status = False

	simplifiedN = math.sqrt(number)

	if (number % simplifiedN) == 0 :
		return True

	else:
		return False

def guessGame(number):
	test = 0
	for x in xrange(1, number + 1):
		if squareChecker(x) == True:
			test = test + 1

	return test


def guessPrompt(number):
	while True:
		attempt = raw_input("\nHow many prime numbers are between 1 and " + str(number) + ": ")
		try:
			if attempt == 'q':
				print("\nProgram Ended\n")
				exit()
			number = int(attempt)
			return number
			break
		except ValueError:
			print("\nThat's not a valid option!  Enter a number!\n")
	

def main():
	number = input("\nEnter a number: ")
	result = guessGame(number)	
	userPrompt = guessPrompt(number)

	if(userPrompt > result):
		print("\nYou chose a number too high!\n")
	elif(userPrompt < result):
		print("\nYou chose a number too low!\n")
	elif(userPrompt == result):
		print("\nCongrats!  You chose the right number!")

	print("There are " + str(result) + " prime numbers in between 1 and " + str(number) + "\n")


main()

