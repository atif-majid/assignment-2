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
