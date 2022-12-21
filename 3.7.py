'''
3.7 Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
'''
int_array = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(0, rows):
    temp_array = []
    for j in range(0, cols):
        val = int(input(f"Enter value for {i} {j}: "))
        temp_array.append(val)
    int_array.append(temp_array)
print(int_array)