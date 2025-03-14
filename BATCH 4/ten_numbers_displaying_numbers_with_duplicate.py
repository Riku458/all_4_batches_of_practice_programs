#First is to get the 10 numbers from the user

numbers = []
print("Input 10 numbers:")
for i in range(10):
    while True:
        try:    
            num = float(input(f"Number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Please put a valid input")

#Create a function that will find the number/s with duplicate
#Printing the numbers with duplicate