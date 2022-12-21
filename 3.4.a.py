'''
3.4 The factorial of a nonnegative integer n is written n! (pronounced “n factorial”) and is defined as follows:
n!=n·(n-1)·(n-2)·...·1 (forvaluesofngreaterthanorequalto1) and n!=1 (forn=0).
For example, 5! = 5 · 4 · 3 · 2 · 1, which is 120. Factorials increase in size very rapidly. 
What is the largest factorial that your program can calculate before leading to an overflow error?
a) Write a program that reads a nonnegative integer and computes and prints its factorial.
'''
num = int(input("Enter a positive number: "))
if(num<0):
	print("Invalid input")
	exit()
fact = 1
for i in range(1, num+1):
	fact = fact * i
print(f"Factorial of {num} = {fact}")
