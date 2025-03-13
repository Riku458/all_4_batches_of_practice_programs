#I'll just use my previous code here

even_num = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    
    if num % 2 == 0:
        even_num += 1

print(f"The odd number/s in the given numbers are: {even_num}")

#WORKING