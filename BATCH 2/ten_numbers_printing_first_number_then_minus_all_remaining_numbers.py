#I'll just use my previous code here

numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = numbers [0] - sum(numbers[1:])
print("The result is:", result)

#WORKING