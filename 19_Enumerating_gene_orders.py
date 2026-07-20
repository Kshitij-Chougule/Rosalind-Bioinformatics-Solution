numbers=[]
m=5
# Function used to find factorial of n using recursion
def total_cases(n):
    if n==1:
        return 1
    return n*total_cases(n-1)
# Makes a list of numbers so that we can rearrange them
def numbers_list(n):
    for i in range(1,n+1):
        numbers.append(i)
    return numbers
# Defined a function named permute to get different permutations
def permute(nums,start=0):   
    if start==len(nums):
# The print function is written in such a way to just help write output neatly
        print(' '.join(map(str,nums)))
        return
    for i in range(start,len(nums)):
        nums[start],nums[i]=nums[i],nums[start]
# Used the logic of recursion. Also used a parameter called start to fix numbers one by one i.e. to help build a permutation
        permute(nums,start+1)
        nums[start],nums[i]=nums[i],nums[start]
nums=numbers_list(m)
print(total_cases(m))
permute(nums)