import math

def tower():
	n = 5

	a = "A"
	b = "B"
	c = "C"

	formula = math.pow(2, n) - 1

	print(str(formula))

	move(n, a, b, c)

def move(n, start, end, aux):
	if n > 0:
		move(n - 1, start, aux, end)
		print("Move disk from " + start + " to " + end)
		move(n - 1, aux, end, start)


def main():
	tower()

main()