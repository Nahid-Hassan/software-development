from functools import lru_cache


@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci1(n):
    if n <= 1:
        return n
    return fibonacci1(n-1) + fibonacci1(n-2)


def main():
    print("call fibonacci(n): ")
    for i in range(400):
        print(i, fibonacci(i))
    print("call fibonacci1(n): ")
    for i in range(100):
        print(i, fibonacci1(i))
    print("Done")


if __name__ == '__main__':
    main()
