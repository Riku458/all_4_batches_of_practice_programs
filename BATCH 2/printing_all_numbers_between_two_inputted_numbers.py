#I'll just use my previous code here

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

start = min(num1, num2) + 1
end = max(num1, num2)

for i in range(start, end):
    print(i, end = " ")

#WORKING