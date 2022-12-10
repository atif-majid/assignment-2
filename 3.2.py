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
