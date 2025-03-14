#Create a function that will get the number from the user

numbers = []

while True:
    user_input = input("Enter a number (or a non-numerical character to exit): ")

    try:                                    #Check if the number is valid or not
        number = int(user_input)
    except ValueError:
        print("Invalid input. Exiting the program.")
        break

    if number in numbers:                   #Check if the number is unique or duplicate as its output
        print(f"{numbers} - Duplicate")
    else:
        print(f"{numbers} - Unique")
        numbers.append(number)



