
#Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

a = int(input("Enter a number: "))
count = 0
while (a > 1):
	if (a % 2 == 0):
		a /= 2
	else :
		a  = a*3 + 1
	count +=1

print('The count is',count)

