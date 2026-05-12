# 1 + 2 + 3 + 4 + 5 = 15
number = int(input("Enter a number: "))
sum = 0
for i in range(2, number+1 , 2):
    print(i)
    sum = sum + i
print(f"Sum of the numbers is {sum}")


sum = 0
for i in range(2, number+1 , 2):
    print(i)
    sum = sum + i*i
print(f"Sum of the squares of the numbers is {sum}")