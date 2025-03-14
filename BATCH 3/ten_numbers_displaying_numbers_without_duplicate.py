#First is to get the 10 numbers from the user
def main():
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

    unique_numbers = []             #Create a function that will find the number/s with duplicate and disregarding that number/s
    for num in numbers:
        if numbers.count(num) == 1:
            unique_numbers.append(num)

    if unique_numbers:              #Printing the numbers without duplicate
        print("The numbers that don't have duplicates: ")              
        for num in unique_numbers:
            print(num)
    else:
        print(f"All numbers have duplicates")

if __name__ == "__main__":
    main()