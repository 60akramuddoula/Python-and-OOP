def count_combinations(K, S):
    count = 0
    for X in range(K + 1):
        for Y in range(K + 1):
            Z = S - X - Y
            if 0 <= Z <= K:
                count += 1
    return count

# Reading input
K, S = map(int, input().split())

# Counting combinations
result = count_combinations(K, S)

# Printing the result
print(result)
