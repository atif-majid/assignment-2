'''
3.1 Drivers are concerned with the mileage obtained by their automobiles. 
One driver has kept track of several tankfuls of gasoline by recording miles driven and gallons used for each tankful. 
Develop a Python program that prompts the user to input the miles driven and gallons used for each tankful. 
The program should calculate and display the miles per gallon obtained for each tankful. 
After processing all input information, the program should calculate and print the combined miles per gallon 
obtained for all tankful (= total miles driven divided by total gallons used).
Enter the gallons used (-1 to end): 12.8
Enter the miles driven: 287
The miles / gallon for this tank was 22.421875 Enter the gallons used (-1 to end): 10.3
Enter the miles driven: 200
The miles / gallon for this tank was 19.417475 Enter the gallons used (-1 to end): 5
Enter the miles driven: 120
The miles / gallon for this tank was 24.000000 Enter the gallons used (-1 to end): -1
The overall average miles/gallon was 21.601423
'''
galons = float(input("Enter the gallons used (-1 to end): "))
totalgalons = 0
totalmiles = 0

while (galons!=-1):
	miles = float(input("Enter the miles driven: "))
	totalgalons = totalgalons + galons
	totalmiles = totalmiles + miles
	avg = miles/galons
	print(f"The miles / gallon for this tank was {avg:.6f}")
	galons = float(input("Enter the gallons used (-1 to end): "))

if(totalgalons>0):
	overallavg = totalmiles/totalgalons
	print(f"The overall average miles/gallon was {overallavg:6f}")
else:
	print("No data provided")	
