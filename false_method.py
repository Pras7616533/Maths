def find_initial_interval(f, guess=0, step=1):
    """
    Finds an initial interval for the False Position method by expanding
    from an initial guess until f(a) and f(b) have opposite signs.

    Args:
    - f: The function for which the initial interval is to be found.
    - guess: An initial guess for the root.
    - step: The step size for expanding the interval (default is 1).

    Returns:
    - The initial interval [a, b].
    """
    a = guess
    b = guess + step
    while f(a) * f(b) >= 0:
        b += step
    return a, b

def false_position_method(f, a, b, epsilon=1e-6, max_iterations=3):
    """
    Implements the False Position method to find the root of a function.

    Args:
    - f: The function for which the root is to be found.
    - a: The left endpoint of the interval.
    - b: The right endpoint of the interval.
    - epsilon: The desired level of precision (default is 1e-6).
    - max_iterations: The maximum number of iterations allowed (default is 1000).

    Returns:
    - The approximate root of the function.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at endpoints must have opposite signs")

    iteration = 0
    while (b - a) > epsilon and iteration < max_iterations:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"Iteration {iteration + 1}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {f(c):.4f}")
        if abs(f(c)) < epsilon:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2

if __name__ == "__main__":
    import sympy as sp

    # Ask user to input the function expression
    expression = input("Enter the function expression in terms of x: ")
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(expression))

    # Ask user for an initial guess
#    guess = float(input("Enter an initial guess for the root: "))

    # Find the initial interval
    a, b = find_initial_interval(f)
    if b - a != 1:
        while True:
            if b - a == 1:
                break
            a += 1
    print (f"f(a)={f(a)} f(b)={f(b)}")
    # Call the False Position method
    root = false_position_method(f, a, b)

    print(f"Approximate root: {root:.4f}")
