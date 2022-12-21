'''
c) Write a program that computes the value of ex by using the formula [Note: Your program can stop after summing 10 terms.]
e^x =1+ x/1! +x^2/2! + x^3/3! +...
'''
x = int(input("Enter a number: "))
ex = 1
for i in range(1, 10):
	fact = 1
	for j in range(1, i+1):
		fact = fact * j
	ex = ex + ((x**i)/fact)
print(f"Value of e^x = {ex}")
