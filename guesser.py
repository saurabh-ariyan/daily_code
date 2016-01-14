import random
def main():
	print ("Guess a number between 1 and 100")
	#randomNumber = 34
	randomNumber = random.randint(1, 100)
	found = False	#Flag
	while not found:
		user = int(input("Your guess: "))
		if user == randomNumber:
			print("Got it")
			found = True
		elif user > randomNumber:
			print ("guess lower")
		else:
			print ("Guess higher")
	

if __name__ == "__main__":
	main()
