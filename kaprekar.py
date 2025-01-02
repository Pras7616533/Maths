def is_palindrome3(num):
    num_str = f"{num:03d}"
    return num_str == num_str[::-1]

def kaprekar_routine3(num):
    kaprekar_constant = 495
    steps = 0
    print(f"Starting number: {num}")
    while num != kaprekar_constant:
        if is_palindrome3(num):
            descending = 0
            ascending = 0
            num = 495
            print(f"Step {steps}: {descending} - {ascending} = {num} (Palindrome)")
        else:
            num_str = f"{num:03d}"
            descending = int("".join(sorted(num_str, reverse=True)))
            ascending = int("".join(sorted(num_str)))
            num = descending - ascending
            steps += 1
            print(f"Step {steps}: {descending} - {ascending} = {num}")

    print(f"\nKaprekar's constant 6174 reached in {steps} steps.")

def is_palindrome4(num):
    num_str = f"{num:04d}"
    return num_str == num_str[::-1]

def kaprekar_routine4(num):
    kaprekar_constant = 6174
    steps = 0
    print(f"Starting number: {num}")
    while num != kaprekar_constant:
        if is_palindrome4(num):
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
    while True:
        n = input("0 for exit\n1 for 4digit\n2 for 3digit\n")
        if  n == '0':
            break
        if n == '1':
            initial_number = int(input("Enter a four-digit number with at least two different digits: "))
            if 1000 <= initial_number <= 9999:
                kaprekar_routine4(initial_number)
        elif  n == '2':
            initial_number = int(input("Enter a three-digit number with at least two different digits: "))
            if 100 <= initial_number <= 999:
                kaprekar_routine3(initial_number)
        else:
                print("ok boss")
