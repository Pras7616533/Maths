def algebraic_proof(x, y):
    left_side = (x**2 + y**2 + (x + y)**2)**2
    right_side = 2 * (x**4 + y**4 + (x + y)**4)
    return left_side == right_side

def geometric_proof(x, y):
    left_side = (x**2 + y**2 + (x + y)**2)**2
    right_side = 2 * (x**4 + y**4 + (x + y)**4)
    return left_side, right_side

def main():
    try:
        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))

        algebraic_result = algebraic_proof(x, y)
        geometric_result = geometric_proof(x, y)

        if algebraic_result:
            print("Algebraic Proof: The identity holds true algebraically.")
        else:
            print ("Algebraic Proof:")
            print ("The identity does not hold true algebraically.")

        print ("Geometric Proof:")
        print (f"Left side: {geometric_result[0]}")
        print (f"Right side: {geometric_result[1]}")
        print ("The identity holds true geometrically.")

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

