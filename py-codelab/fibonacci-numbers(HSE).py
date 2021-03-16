from math import sqrt
from math import floor

# def recursive solution


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# iterative solution
def fib_iterative(n):
    # create an array of size an with default value 0
    fib = [0] * (n + 1)

    # initialise zero and first fibonacci number
    fib[0] = 0
    fib[1] = 1

    # iteratively calculation
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]

    return (fib[n], fib)


def fib_using_formula(n):
    sqrt_5 = sqrt(5)

    return ((((1 + sqrt_5) / 2) ** n) - (((1 - sqrt_5) / 2) ** n)) / sqrt_5


def main():
    res1 = fib_recursive(10)
    res2, series = fib_iterative(10)
    res3 = floor(fib_using_formula(10))

    print(res1, res2, res3)


if __name__ == '__main__':
    main()
