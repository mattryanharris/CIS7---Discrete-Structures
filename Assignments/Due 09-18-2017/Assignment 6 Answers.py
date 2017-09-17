def intCheck():


	while True:
		attempt = raw_input("Enter a number: ")
		try:
			if attempt == 'q':
				print("\nProgram Ended\n")
				exit()
			number = int(attempt)
			break
		except ValueError:
			print("\nThat's not a valid option!  Enter a number!\n")
	if (number % 2) == 0:
		print("\nThe number is even\n")
	else:
		print("\nThe number is odd\n")


def main():
	while True:
		intCheck()

main()
