#Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
#0th generation has genotype Aa Bb
#kth generation
#N organisms having Aa Bb organisms
import math

def independent_alleles(k, n):
    total_organisms = 2 ** k
    p = 0.25
    
    # Calculate P(X < N)
    prob_less_than_n = 0
    for i in range(n):
        # Binomial coefficient: nCr
        comb = math.comb(total_organisms, i)
        prob_less_than_n += comb * (p ** i) * ((1 - p) ** (total_organisms - i))
        
    # P(X >= N) = 1 - P(X < N)
    return round(1 - prob_less_than_n, 3)


print(independent_alleles(5, 7))  
