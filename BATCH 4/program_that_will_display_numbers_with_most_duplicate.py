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

if not numbers:                                 #Create a function that will get the numbers of duplicates

    print("Invalid input")
else:
    duplicates = len(numbers) != len(set(numbers))

    if not duplicates:                          #Create a function that will get the most duplicates number/s
        print("All numbers are unique.")
    else:
        most_duplicate_num = max(set(numbers),  key=numbers.count)
        max_count = numbers.count(most_duplicate_num)

#Display the output
