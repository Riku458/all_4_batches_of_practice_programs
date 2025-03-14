#Create a function that will get the 10 numbers from the user

def main():
    numbers = []
    unique_numbers = []

    print("Input 10 numbers: ")

    for i in range(10):
        while True:
                try:
                    num = float(input(f"Enter number {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                     print("Please put a valid input")

    for num in numbers:                 #Create a function that will get the first number of the duplicate number/s
        if num not in unique_numbers:
                unique_numbers.append(num)

    print("\nAll inputted numbers:")    #Display all the numbers and the numbers with only one duplicate number/s
    print(numbers)

    print("\nNumbers with duplicates removed (only the first entry)")
    print(unique_numbers)

if __name__ == "__main__":
      main()

