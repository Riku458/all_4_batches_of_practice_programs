#Create a function that will get the numbers that the user wants and exit if the input is not valid

numbers = []

while True:
    user_input = input("Enter a number (or a non-numerical character to exit the program): ")

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please put a valid input. Exiting the program.")
        break

#Create a function that will determine the lowest number

if numbers:
    lowest_number = min(numbers)
    print(f"The lowest number entered is: {lowest_number}")
else:
    print("No valid numbers were entered")

#I forget to commit the Pseudocode but here it is
#Pseudocode:
#Create a function that will get the numbers that the user wants
#Create a function that will determine the lowest number
