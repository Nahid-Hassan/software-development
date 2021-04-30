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
