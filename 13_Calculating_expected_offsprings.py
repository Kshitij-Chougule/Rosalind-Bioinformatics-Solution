# 1. AA-AA
# 2. AA-Aa
# 3. AA-aa
# 4. Aa-Aa
# 5. Aa-aa
# 6. aa-aa
def expected_offspring(Data):
#prob is the probablity of 1. 2. 3. 4. 5. 6. respectively
    prob=[1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    expected_value=0
    for count,p in zip(prob,Data):
# Used a formula to find expected value of dominant offsprings and multiplied by two since the question says that every couple has exactly two offspring.
        expected_value+=p*count*2
    return expected_value
Data=[18869,17033,16455,17313,19389,17436]
print(expected_offspring(Data))
