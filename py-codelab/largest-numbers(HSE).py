from math import inf

def largest_number_greedy(nums):
    largest_number = []

    for _ in range(len(nums)):
        max_num = -inf

        for num in nums:
            if num > max_num:
                max_num = num

        nums.remove(max_num)
        largest_number.append(max_num)

    # list to number
    num = int(''.join(map(str, largest_number)))
    # return largest number
    return num


def main():
    nums = list(
        map(int, input("Enter the list of numbers in one line: ").split()))
    largest_number = largest_number_greedy(nums)
    print(largest_number)


if __name__ == '__main__':
    main()
