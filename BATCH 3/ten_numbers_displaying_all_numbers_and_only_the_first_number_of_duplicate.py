#Create a function that will get the 10 numbers from the user
numbers = []
unique_numbers = []

print("Input 10 numbers: ")

for i in range(10):
    while True:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break

#Create a function that will get the first number of the duplicate number/s

for num in numbers:
      if num not in unique_numbers:
            unique_numbers.append(num)

#Display all the numbers and the numbers with only one duplicate number/s

print(unique_numbers)

