number = 600851475143
factor = 2

while factor*factor < number:
	while number % factor == 0:
		number = number/factor
	factor = factor + 1

print number