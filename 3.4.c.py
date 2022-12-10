x = int(input("Enter a number: "))
ex = 1
for i in range(1, 10):
	fact = 1
	for j in range(1, i+1):
		fact = fact * j
	ex = ex + ((x**i)/fact)
print(f"Value of e^x = {ex}")
