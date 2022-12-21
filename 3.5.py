'''
3.5 Write a program that prints the following patterns separately, one below the other 
each pat- tern separated from the next by one blank line. Use for loops to generate the
patterns. All asterisks (*) should be printed by a single statement of the form
print '*',
(which causes the asterisks to print side by side separated by a space). (Hint: The last two 
patterns require that each line begin with an appropriate number of blanks.) Extra credit: 
Combine your code from the four separate problems into a single program that prints all four 
patterns side by side by making clever use of nested for loops. For all parts of this program—minimize 
the numbers of asterisks and spaces and the number of statements that print these characters.
a) Half pyramid
b)Left Half Pyramid
c) Inverted half pyramid 
d)Full inverted Pyramid
'''
rows = 7
for i in range (1, rows+1):
	for j in range(1, i+1):
		print('*', end = " ")
	print("")

print("")
for i in range(rows+1, 1, -1):
	for j in range(i, 1, -1):
		print("*", end=" ")
	print("")
print("")
nline=0
for i in range(rows+1, 0, -1):
	for j in range(1, i):
		print(" ",end=" ")
	for j in range(1, nline+1):
		print("*",end=" ")
	nline = nline+1
	print("")
print("")
nline=0
for i in range(rows+1, 0, -1):
	for j in range(1, nline+1):
		print(" ", end=" ")
	nline = nline+1
	for j in range(1, i):
		print("*", end=" ")
	print("")

