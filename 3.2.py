'''
3.2 A palindrome is a number or a text phrase that reads the same backwards or forwards. 
For example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611. 
Write a program that reads in a five-digit integer and determines whether it is a palindrome. 
(Hint: Use the division and modulus operators to separate the number into its individual digits.)

'''
num = int(input("Enter a 5 digit number: "))
if(num<10000 or num>99999):
	print("Number not in range")
	exit()

num2 = num
reverse = 0
while(num2>0):
	digit = num2 % 10
	reverse = reverse * 10 + digit
	num2 = num2//10

if(num==reverse):
	print(f"{num} is a Palindrome")
else:
	print(f"{num} is not a palindrome")
