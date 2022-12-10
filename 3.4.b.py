e = 1
for i in range (1, 10):
	fact = 1
	for j in range(1, i+1):
		fact = fact * j
	e = e + (1/fact)
print(f"Value of e = {e}")
