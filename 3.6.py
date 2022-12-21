for i in range (1, 20):
    for j in range(1, 20):
        for k in range(1, 20):
            if(i**2 + j**2 == k**2):
                print(f"Pythagorean Triples:\n Side 1: {i},\n Side 2: {j}, \nHypotenuse: {k}")
                print("\n\n")
