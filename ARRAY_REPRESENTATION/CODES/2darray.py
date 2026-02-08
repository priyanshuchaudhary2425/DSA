matrix = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f"Please enter value for {i}{j}: "))

print(f"{matrix}", end="\n")