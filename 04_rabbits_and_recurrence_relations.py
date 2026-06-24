# To find the total number of rabbit pairs in n months
def rabbits(n,k):  
#Here n is months and k is pair of rabbits produced in a month
    if n==1 or n==2:
        return 1
# Using recurrsion logic(Factorial Logic)
    total=rabbits(n-1,k)+(rabbits(n-2,k)*k)
    return total
n=32
k=2
answer=rabbits(n,k)
#printing answer
print(answer)