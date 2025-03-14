#First is to get the 10 numbers from the user
def main():
    numbers = []
    print("Input 10 numbers:")
    for i in range(10):
        while True:
            num = float(input(f"Number {i + 1}: "))
            numbers.append(num)
            break

    unique_numbers = []             #Create a function that will find the number/s with duplicate and disregarding that number/s
    for num in numbers:
        if numbers.count(num) == 1:
            unique_numbers.append(num)

    if unique_numbers:              #Printing the numbers without duplicate
        print(f"Numbers that don't have duplicate: {unique_numbers}")
    else:
        print(f"All numbers are duplicate")

if __name__ == "__main__":
    main()