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

