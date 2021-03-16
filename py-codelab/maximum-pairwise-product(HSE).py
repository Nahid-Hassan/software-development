"""
Using a heap data structure (from collections import heap) is the theoretical
best way to find the n largest items, but you'd likely need to have 100,000's
of items to make it worth your while.

>>> 3
>>> 1 2 3
6
"""

_ = int(input())

# read numbers
nums = list(map(int, input().split()))

# Iterative solution
result = 0
# calculate maximum pairwise of multiplication
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        # if new pair multiplication is greater than previous result
        # then this block of code is work.
        if nums[i] * nums[j] > result:
            result = nums[i] * nums[j]

print(result)

# Using sorting
nums.sort(reverse=True)
print(nums[0] * nums[1])

# find


def product_of_two_largest(seq):
    largest = float("-inf")
    second_largest = float("-inf")

    for elt in seq:
        if elt > largest:
            second_largest = largest
            largest = elt
        elif elt > second_largest:
            second_largest = elt
    return second_largest * largest


print(product_of_two_largest(nums))
