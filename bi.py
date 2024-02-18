"""This program first defines a function extended_gcd(a, b) 
that implements
the Extended Euclidean Algorithm to find
the greatest common divisor of a and b,
along with the integers x and y such that
ax+by=gcd(a,b).

Then, in the main() function,
it prompts the user to input two integers a and b,
calls the extended_gcd() function to compute the GCD and the correspondin x and y values,
and prints the results as per the given instructions.


"""

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def main():
    try:
        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))

        gcd, x, y = extended_gcd(a, b)

        print(f"GCD of {a} and {b} is:", gcd)
        print(f"x = {x}, y = {y} such that {a}x + {b}y = {gcd}")
        print(f"Integers of the form ax + by are exactly the multiples of {gcd}")
    except ValueError:
        print("Error: Invalid input. Please enter integer values.")

if __name__ == "__main__":
    main()

