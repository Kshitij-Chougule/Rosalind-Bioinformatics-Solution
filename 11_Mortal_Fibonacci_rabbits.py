#n months if all rabbits live for m months
#Every rabbit reproduces twicw before dying
n=93
m=20
def rabbit_population(n,m):
    #Making a list to easily delete the mortal rabbits
    Total_rabbits= [] 
    #Since i-2 will be out of range so we added first two cases
    Total_rabbits.append(1)
    Total_rabbits.append(1)
    for i in range(2,n):
        Total_rabbits.append(Total_rabbits[i-1]+Total_rabbits[i-2])
# For first case where the oldest pair dies
        if i==m:
            Total_rabbits[i]-=1
        if i>m:
            Total_rabbits[i]-=Total_rabbits[i-m-1]
    return Total_rabbits[i]
print(rabbit_population(n,m))
