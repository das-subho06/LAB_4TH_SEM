def matrixInput():
    m, n = map(int, input("Enter the values of m and n for m×n matrix: ").split())

    arr = []   # 2D array
    for i in range(m):
        row = []
        for j in range(n):
            val = int(input(f"Enter element of row {i+1} column {j+1}: "))
            row.append(val)
        arr.append(row)

    return arr, m, n


def transpose(arr, m, n):
    arr2 = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(arr[j][i])
        arr2.append(row)

    print("Transpose:")
    for r in arr2:
        print(r)
    return arr2


def matrix_add(arr, brr, m, n):
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(arr[i][j] + brr[i][j])
        result.append(row)

    print("Sum of matrices:")
    for r in result:
        print(r)
    return result



print("Enter first matrix:")
arr, m, n = matrixInput()

print("\nEnter second matrix:")
brr, m2, n2 = matrixInput()

if m != m2 or n != n2:
    print("Matrix addition not possible. Dimensions must be same.")
else:
    matrix_add(arr, brr, m, n)
transpose(arr, m, n)
transpose(brr, m, n)

