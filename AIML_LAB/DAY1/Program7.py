numbers = []

try:
    with open("data.txt", "r") as file:
        for line in file:
            parts = line.strip().split()   # split line into words/numbers
            for item in parts:
                try:
                    num = int(item)
                    numbers.append(num)
                except ValueError:
                    print(f"Ignored invalid data: {item}")

except FileNotFoundError:
    print("File not found!")
    exit()

if len(numbers) == 0:
    print("No valid integers in the file.")
    exit()

count = len(numbers)
mean = sum(numbers) / count
maximum = max(numbers)
minimum = min(numbers)

print("\nFile Data Summary:")
print("Count :", count)
print("Mean  :", mean)
print("Max   :", maximum)
print("Min   :", minimum)
