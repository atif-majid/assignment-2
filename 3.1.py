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
