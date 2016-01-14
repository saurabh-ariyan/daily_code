class pet:
	number_of_legs = 0
	def sleep(self):
		print("zzz")

	def count_leg(self):
		print("I have %s legs "%self.number_of_legs)

# doug = pet()
# doug.sleep()

# doug.number_of_legs = 4
# print ("Doug has %s legs." % doug.number_of_legs )
# doug.count_leg()

class dog(pet):
	def bark(self):
		print("woof")		

doug = dog()
doug.bark()
doug.count_leg()
