#Goal: Find the sum of all multiples of 3 or 5 below 1000

number = 0
for x in range (1,1000):
	#print x
	if x%3 == 0 and x%5 ==0:
		number+=x
	#	print number
	elif x%3 == 0:
		number+=x
	#	print number
	elif x%5 == 0:
		number+=x
	#	print number
		
print number