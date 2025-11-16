size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    # Inner loop using for to print asterisks in a row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
