# Algorithmic Toolbox

## Table of Contents

- [Algorithmic Toolbox](#algorithmic-toolbox)
  - [Table of Contents](#table-of-contents)
    - [Programming Challenges](#programming-challenges)
      - [Solving Sum of Two Digits](#solving-sum-of-two-digits)
      - [Solving the Maximum Pairwise Product](#solving-the-maximum-pairwise-product)

### Programming Challenges

#### Solving Sum of Two Digits

- **Problem Statement**:

```text
Given two digits 0 <= a <= 9 and 0 <= b <= 9.

Input format: The first line of the input contains a, and b.
Output: a + b

Example:
    9 7
    16
```

- **Algorithm**:

```text
Read two numbers and print the sum of this two numbers.
```

- **Python Code**:  

```py
# map(type, iterable)
tokens = list(map(int, input("Enter two numbers: ").split()))

# extract numbers
a, b = tokens

# print the sum
sum_of_two_numbers = a + b
print(sum_of_two_numbers)
# 7 8
# 15
```

#### Solving the Maximum Pairwise Product

- **Problem Statement**:

```text
Given a sequence of non-negative integers 0 <= a <= 10^5, find the maximum pairwise product.

Input Format: 
First line contains number 2 <= n <= 2 * 10^5
The next line contains series of 'n' non-negative numbers.

Output Format:
Output a single number - the maximum pairwise product.

Example:
    # Input
    3
    1 2 3
    # Output
    6
```

- **Algorithm**:


- **Python Code**:

```py
# read n
n = int(input('Enter the n: '))
# read the sequence of numbers
nums = list(map(int, input("Enter n integers: ").split()))

# processing - iterative method
# initialize mx = 0
mx = 0
for i in range(n):
    for j in range(i+1, n):
      if nums[i] * nums[j] > mx:
          mx = nums[i] * nums[j] 

print(mx) 
```

