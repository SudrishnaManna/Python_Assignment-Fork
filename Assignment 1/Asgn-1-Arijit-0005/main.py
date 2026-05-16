from VectorOperation import Vector
import numpy as np
import sys

in1 = input("Enter vector1: ").split(" ")
in2 = input("Enter vector1: ").split(" ")
mat1 = np.array(list(map(lambda x: int(x), in1)))
mat2 = np.array(list(map(lambda x: int(x), in2)))
v = Vector(mat1, mat2)

print("""Menu:
1. Vector Addition
2. Scalar Multiplication
3. Dot Product
4. Cross Product
5. Orthogonality Check
6. Parallelism Check
7. Exit""")
while True:
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter by number...\n")
    match choice:
        case 1:
            print(f"Addition: {v.add}")

        case 2:
            print(f"Scalar Multiplication: {v.mul}")

        case 3:
            print(f"Dot Product: {v.dot}")

        case 4:
            print(f"Cross Product: {v.cross}")

        case 5:
            print("Orthogonal." if v.isOrthogonal else "Not Orthogonal")

        case 6:
            print("It's Parallel." if v.isParallel else "It's not Parallel")

        case 7:
            sys.exit("App closed.")
        
        case _:
            print("The option not exsist!!Please try from the list.")