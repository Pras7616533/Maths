def nth_power_sum(a, b, n):
    # Initialize the list to store the terms
    terms = []

    # Iterate from 0 to n to generate n+1 terms
    for i in range(n + 1):
        # Calculate the binomial coefficient
        coefficient = comb(n, i)
        # Calculate the term and append it to the list
        term = coefficient * (a ** (n - i)) * (b ** i)
        terms.append(term)

    return terms

def comb(n, k):
    # Calculate the binomial coefficient
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    return numerator // denominator

def factorial(n):
    # Calculate the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sum(list):
    temp = 0
    for i in list:
        temp = temp + i
    print(f"Total Term:{temp}")

def main():
    try:
        # Take input for a, b, and n
        a = int(input("Enter the value of 'a': "))
        b = int(input("Enter the value of 'b': "))
        n = int(input("Enter the value of 'n' (a non-negative integer): "))

        if n < 0:
            raise ValueError("n must be a non-negative integer.")

        # Calculate the nth power sum
        result = nth_power_sum(a, b, n)

        # Print the result
        print(f"The expression for ({a} + {b})^{n} as the sum of {n+1} terms is:")
        for i, term in enumerate(result):
            print(f"Term {i}: {term}")
        # sum of list
        sum(result)

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

