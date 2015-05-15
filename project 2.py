fibo = [1,2]
fiboCounter = 1
fibonumber = 0
sum = 2
while fibonumber < 4000000:
	fibonumber = fibo[fiboCounter] + fibo[fiboCounter-1]
	fiboCounter+=1
	fibo.append(fibonumber)
	if fibonumber % 2 == 0:
		sum += fibonumber
		
print sum