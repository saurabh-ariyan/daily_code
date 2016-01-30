import math
def sumdiff(n):
	return (math.pow(n,4)/4 + math.pow(n,3)/6 - math.pow(n,2)/4 - n/6)

print (sumdiff (10));
print (sumdiff(100));