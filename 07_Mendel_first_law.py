#k is homozygous dominant(XX)
#m is heterozygous(Xx)
#n is homozygous recessive(xx)
#The offspring should be dominant
k=23
m=22
n=19
#offspring can be recessive in case of only xx:
#(k*k=0),(m*m=0.25),(n*n=1),(k*m=0),(m*n=0.5),(k*n=0)
total_population=k+m+n
probablity_of_recessive_offspring=float((m/total_population)*((m-1)/(total_population-1))*0.25+(n/total_population)*((n-1)/(total_population-1))+(m/total_population)*(n/(total_population-1)))
#Since probablity of dominant offspring and probablity of recessive offspring are complimentary 
probablity_of_dominant_offspring=1-probablity_of_recessive_offspring
print(f"{probablity_of_dominant_offspring:.5f}")