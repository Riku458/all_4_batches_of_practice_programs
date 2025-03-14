#First is to get the 10 numbers from the user

numbers = []
print("Input 10 numbers:")
for i in range(10):
    while True:
        num = float(input(f"Number {i + 1}: "))
        numbers.append(num)
        break
        
#Create a function that will find the number/s with duplicate and disregarding that number/s

unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

#Printing the numbers without duplicate

print(unique_numbers)