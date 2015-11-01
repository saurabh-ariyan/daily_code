#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found.

a = input ("Enter the stirng: ")
print ('No of a in the string:', a.count('a'))
print ('No of e in the string:', a.count('e'))
print ('No of i in the string:', a.count('i'))
print ('No of o in the string:', a.count('o'))
print ('No of u in the string:', a.count('u'))
z= a.count('a') + a.count('e') + a.count('i')+ a.count("o")+a.count('u')
print ('No of vowels in the string:',z )