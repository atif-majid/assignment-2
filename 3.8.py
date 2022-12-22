'''
3.8 Suppose you give a dinner party for six guests, but your table seats only four. 
In how many ways can four of the six guests arrange themselves at the table? 
Any of the six guests can sit in the first chair. Any of the remaining five can sit in the second chair. 
Any of the remaining four can sit in the third chair, and any of the remaining three can sit in the fourth chair. 
(The last two will have to stand.) So the number of possible arrangements of six guests in four chairs is 6*5*4*3, 
which is 360. Write a program that calculates the number of possible arrangements for any number of guests and any number of chairs. 
(Assume there will never be fewer guests than chairs.) Don’t let this get too com- plicated. A simple for loop should do it.
'''

nGuests = int(input("Enter number of guests: "))
nChair = int(input("Enter number of chairs: "))

if nChair<nGuests:
    nArrangements = 1
    for i in range(0, nChair):
        nArrangements = nArrangements * (nGuests-i)
    print(f"Possible arrangements for {nGuests} with {nChair} = {nArrangements}")
else:
    print(f"There are plenty of chairs for {nGuests} guests")