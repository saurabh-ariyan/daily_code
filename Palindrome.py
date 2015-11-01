#Check if Palindrome - Checks if the string entered by the user is a palindrome. 
#That is that it reads the same forwards as backwards like 'racecar'

a = input ("Enter the string: ")

b = a[::-1]

if (b == a):
	print("Yes, the string is a palindrome. ")
else :
	print ("Nope, this is not a palindrome. ")
