firstTerm = 1; secondTerm = 2; res = 2; currentFib = 3;
# for i in range(1, 4000000):
# 	currentFib = firstTerm + secondTerm
# 	if (currentFib % 2 == 0):
# 		res += currentFib
# 	firstTerm = secondTerm
# 	secondTerm = currentFib
# for i in range(2,10):
#     currentFib = firstTerm + secondTerm
#     if (currentFib % 2 == 0):
#         res += currentFib
#     firstTerm = secondTerm
#     secondTerm = currentFib
#     print(currentFib)
# print(res);

while currentFib < 4000000:
    if (currentFib % 2 == 0):
        res += currentFib
    firstTerm = secondTerm;
    secondTerm = currentFib
    print(currentFib)
    currentFib  =  firstTerm + secondTerm;

print(res)
