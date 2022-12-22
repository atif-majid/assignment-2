'''
3.9Write a program that calculates how much money you’ll end up with the invested amount of money at a fixed interest rate, 
compounded yearly. Have the user furnish the initial amount, the number of years, and the yearly interest rate in percent. 
Some interaction with the program might look like this:
Enter initial amount: 3000
Enter number of years: 10
Enter interest rate (percent per year): 5.5
At the end of 10 years, you will have 5124.43 dollars.
At the end of the first year you have 3000 + (3000 * 0.055), which is 3165. At the end of the second year you have 
3165 + (3165 * 0.055), which is 3339.08. Do this as many
times as there are years. A for loop makes the calculation easy.
'''

nAmount = float(input("Enter initial amount: "))
nYears = int(input("Enter number of years: "))
nInterest = float(input("Enter interest rate: "))
nAnnualReturn = nAmount

for i in range(0, nYears):
    nAnnualReturn = nAnnualReturn + (nAnnualReturn * nInterest/100)
    print(f"At the end of {i+1} years, the amount is {round(nAnnualReturn,2)}")
