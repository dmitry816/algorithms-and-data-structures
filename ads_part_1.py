
# Fibonacci numbers
# F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2
def find_fibonacci_number():
	# numbers to start sum
	num1 = num2 = 1
	n = int(input())
	if n < 2:
		return n
	for i in range(2, n):
		num1, num2 = num2, num1 + num2
	print(num2)

find_fibonacci_number()