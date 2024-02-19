def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def cal(n, r):
    numa = fact(n)
    deno = fact(r) * fact(n - r)
    return numa // deno

def main():
    try:
        n = int(input("Enter total number of events: "))
        r = int(input("Enter the number of successful events: "))
        p = float(input("Enter the probability of success for each event: "))
        q = 1 - p
        c = cal(n, r)
        X = c * (p ** r) * (q ** (n - r))
        print(f"the value of binomial Coefficient is {c}")
        print("successful event to the power of probability of each success is",p ** r)
        print("thetotal number of events -number of successful events whole to the power of unsuccessful event",q ** (n - r))
        print(f"The total probability of the event is {X}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

