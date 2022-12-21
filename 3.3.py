'''
3.3 Input an integer containing 0s and 1s (i.e., a “binary” integer) and print its decimal equiva- lent. 
Appendix C, Number Systems, discusses the binary number system. (Hint: Use the modulus and division operators 
to pick off the “binary” number’s digits one at a time from right to left. Just as in the decimal number system, 
where the rightmost digit has the positional value 1 and the next digit leftward has the positional value 10, 
then 100, then 1000, etc., in the binary number system, the right- most digit has a positional value 1, 
the next digit leftward has the positional value 2, then 4, then 8, etc. Thus, 
the decimal number 234 can be interpreted as 2 * 100 + 3 * 10 + 4 * 1. 
The decimal equiv- alent of binary 1101 is 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1.)
'''
binary = int(input("Enter a binary number (containint 0 and 1 only): "))
temp = binary
power = 0
decimal = 0
while (temp>0):
	digit = temp % 10
	decimal = decimal + (digit * (2 ** power))
	power = power + 1
	temp = temp//10
print(f"{binary} in binary is equal to {decimal} in decimal")
