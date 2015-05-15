number1 = 1001
number2 = 1000

#check for palindrome
def checkpal(number):
	#convert int to string
	number = str(number)
	#reverse the string
	newnumber = number[::-1]
	
	if number == newnumber:
		return True
	else:
		return False

#checkpal(number1)
#checkpal(number2)
pal = 0

for x in range (100, 1000):
	for y in range (100, 1000):
		product = x*y
		if checkpal(product):
			if product > pal:
				pal = product
print pal