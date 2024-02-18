def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        if num1 < 0 or num2 < 0:
            raise ValueError("Both integers must be non-negative.")
        result = gcd(num1, num2)
        print(f"The greatest common divisor of {num1} and {num2} is: {result}")
    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()
