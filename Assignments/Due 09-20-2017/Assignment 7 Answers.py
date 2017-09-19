import math

def squareChecker(number):
	status = False

	simplifiedN = math.sqrt(number)

	if (number % simplifiedN) == 0 :
		print("\nIt's a perfect square\n")

	else:
		print("\nIt's not a perfect square\n")


def main():
	while True:
		number = raw_input("\nEnter a number: ")
		try:
			number = int(number)
			break
		except ValueError:
			print("\nThat's not a valid option!  Enter a number!")
	squareChecker(number)

main()