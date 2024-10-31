def is_palindrome(num):
    num_str = f"{num:04d}"
    return num_str == num_str[::-1]

def kaprekar_routine(num):
    kaprekar_constant = 6174
    steps = 0
    print(f"Starting number: {num}")
    while num != kaprekar_constant:
        if is_palindrome(num):
            descending = 0
            ascending = 0
            num = 6174
            print(f"Step {steps}: {descending} - {ascending} = {num} (Palindrome)")
        else:
            num_str = f"{num:04d}"
            descending = int("".join(sorted(num_str, reverse=True)))
            ascending = int("".join(sorted(num_str)))
            num = descending - ascending
            steps += 1
            print(f"Step {steps}: {descending} - {ascending} = {num}")

    print(f"\nKaprekar's constant 6174 reached in {steps} steps.")

if __name__ == "__main__":
    initial_number = int(input("Enter a four-digit number with at least two different digits: "))
    if 0 < initial_number <= 9999:
        kaprekar_routine(initial_number)
    else:
        print("Please enter a valid four-digit number.")
