# Take array input
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)
key = int(input("Enter element to search: "))
linear_comparisons = 0
for i in range(len(arr)):
    linear_comparisons += 1
    if arr[i] == key:
        print("Linear Search: Element found at index", i)
        break
else:
    print("Linear Search: Element not found")

print("Linear Search Comparisons:", linear_comparisons)

sorted_arr = sorted(arr)
low = 0
high = len(sorted_arr) - 1
binary_comparisons = 0

while low <= high:
    mid = (low + high) // 2
    binary_comparisons += 1

    if sorted_arr[mid] == key:
        print("Binary Search: Element found at index", mid)
        break
    elif key < sorted_arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Binary Search: Element not found")

print("Binary Search Comparisons:", binary_comparisons)
