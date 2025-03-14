#Create a function that will get the numbers of what the user wants

numbers = []

while True:
    user_input = input("Enter a number (or any non-numerical charater to exit the program): ")

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Exiting the program.")
        break

#Create a function that will get the numbers of duplicates



#Create a function that will get the most duplicates number/s
