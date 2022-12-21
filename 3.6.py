'''
3.6 (Pythagorean Triples) A right triangle can have sides that are all integers.
The set of three integer values for the sides of a right triangle is called a Pythagorean triple. 
These three sides must satisfy the relationship that the sum of the squares of two of the sides 
is equal to the square of the hypotenuse. Find all Pythagorean triples for side1, side2 and hypotenuse 
all no larger than 20. Use a triple-nested for-loop that tries all possibilities. This is an example 
of “brute force” comput- ing. You will learn in more advanced computer science courses that there 
are many interesting prob- lems for which there is no known algorithmic approach other than sheer brute force.
'''
for i in range (1, 20):
    for j in range(1, 20):
        for k in range(1, 20):
            if(i**2 + j**2 == k**2):
                print(f"Pythagorean Triples:\n Side 1: {i},\n Side 2: {j}, \nHypotenuse: {k}")
                print("\n\n")
