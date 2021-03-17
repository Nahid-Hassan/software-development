# Calculate Greatest Common Divisors

def GCDNaive(a, b):
    """
    Runtime: O(a + b)
    """
    best = 0

    for d in range(2, a + b):
        if not a % d and not b % d:
            best = d
    return best


def GCDGood(a, b):
    """
    Runtime: O(min(a, b))
    """
    best = 0

    min_value = min(a, b)
    for d in range(2, min_value):
        if not a % d and not b % d:
            best = d
    return best


def GCDBest(a, b):
    """
    Runtime: O(log(a*b))
    """
    if not b:
        return a

    _a = a % b
    return GCDBest(b, _a)


def main():
    a = 357
    b = 234
    _gcd_naive = GCDNaive(a, b)
    _gcd_good = GCDGood(a, b)
    _gcd_best = GCDBest(a, b)
    # print(_gcd_naive)
    # print(_gcd_good)
    # print(_gcd_best)

    if _gcd_naive == _gcd_good == _gcd_best:
        print(_gcd_best)


if __name__ == '__main__':
    main()
