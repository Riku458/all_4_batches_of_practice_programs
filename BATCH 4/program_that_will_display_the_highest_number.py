#Create a function that will get the numbers that the user wants and exits that program

numbers = []

while True:
    user_input = input("Enter a number (or a non-numerical character to exit the program): ")

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please put a valid input. Exiting the program.")

#Create a function that will determine the highest number