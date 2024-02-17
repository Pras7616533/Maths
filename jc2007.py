def eo(x):
    if x % 2 == 0:
        return 0  # Even
    else:
        return 1  # Odd

def main():
    num = int(input("Enter the number of elements: "))
    
    for k in range(3, -1, -1):
        passcode = int(input("\nEnter the password to see steps: "))
        n1 = num
        
        if passcode == 2007:
            i = 0
            c = 0
            
            while i < 1:
                if eo(num) == 0:
                    print(num)
                    num = num // 2
                else:
                    print(num)
                    num = (num * 3) + 1
                c += 1
                if num == 1:
                    break
            
            print(f"\nNumber ({n1}) took {c} steps to reach 1")
        else:
            print(f"\nWrong password. Try again to see steps. You have {k} more chance(s).")
        
        if k == 0 or num == 1:
            exit()

if __name__ == "__main__":
    main()
