#Create a function that will get the numbers by what the user wants

numbers = []
while True:
    user_input = input("Enter a number (or any non-numerical character to exit the program): ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

#Create a function that will sort the numbers from highest to lowest