numbers = list(map(int, input("Enter a list of integers (space-separated): ").split()))

result = []
for num in numbers:
    if num % 2 != 0:
        result.append(num)

print("List after removing even numbers:", result)
