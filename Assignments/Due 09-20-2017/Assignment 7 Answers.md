# Assignment 7 Answers

### 1.

	Located in code below.

### 2.

	x, y

	x = 2n + 1

	y = 2m + 1

	x + y <=> (2n + 1) + (2m + 1)

			   2m + 2n + 2

			   2(m + n + 1)

	z = (m + n + 1)
			   
			   2z

	2z = defintion of equal numbers

### 3.

	x, y

	x = 2n

	y = x^2

Prove x + y = even

	2n + (2n)^2 = even

	2n + 4n^2 = even

	2(n + 2n^2) = even

	z = (n + 2n^2)

	2z = definition of equal numbers

### 4.

	n = 2k + 1

	(2k + 1)(2k + 1) = even

	4k^2 + 4k + 1 = even

	2(2k^2 + 2k) + 1 = even

	2z + 1 = even = contradiction

	Proved by contradiction
	
	
### Answer to number 1 in code:

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