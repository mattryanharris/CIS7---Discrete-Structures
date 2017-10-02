import math

def ask():
	attempt = raw_input("Enter a number: ")
	try:
		number = int(attempt)
		return int(number)
	except ValueError:
		print("\nThat's not a valid option!  Enter a number!\n")

def primeFinder(numOne, numTwo):

	if numOne < numTwo:
		highNum = numOne

	else:
		highNum = numTwo

	answer = 0

	for x in xrange(1,highNum + 1):
		if (numOne % x == 0) and (numTwo % x == 0):
			answer = x
	return answer
def main():
	numOne = ask()
	numTwo = ask()

	print(primeFinder(numOne, numTwo))


main()