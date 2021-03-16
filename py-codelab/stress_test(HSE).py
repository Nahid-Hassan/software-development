from random import randint

def maximum_pairwise_product(nums):
    # Iterative solution
    result = 0
    # calculate maximum pairwise of multiplication
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # if new pair multiplication is greater than previous result
            # then this block of code is work.
            if nums[i] * nums[j] > result:
                result = nums[i] * nums[j]
    return result

def maximum_pairwise_product_fast(seq):
    largest = float("-inf")
    second_largest = float("-inf")

    for elt in seq:
        if elt > largest:
            second_largest = largest
            largest = elt
        elif elt > second_largest:
            second_largest = elt
    return second_largest * largest


def main():
    while True:
        n = randint(2, 60)

        nums = [randint(1,10000) for _ in range(n)]
        # for _ in range(n):
        #     nums.append(randint(1,10000))

        res1 = maximum_pairwise_product(nums)
        res2 = maximum_pairwise_product_fast(nums)

        print(n)
        print(nums)
        if res1 != res2:
            print('Wrong!!!', res1, res2)
            break
        else:
            print("Ok", res1, res2)


if __name__ == '__main__':
    main()
