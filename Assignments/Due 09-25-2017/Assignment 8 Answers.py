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

def main():
	number = input("\nEnter a number: ")
	result = guessGame(number)
	print("\nThere are " + str(result) + " prime numbers in between 1 and " + str(number) + "\n")

main()

