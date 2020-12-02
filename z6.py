def CountMutations(dna1 = str(input()), dna2 = str(input())):
    x = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            x = x + 1
    return x
print(CountMutations())
