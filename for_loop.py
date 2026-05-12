num = [10,20,30,40,50]
index = 0 
while index < len(num):
    print(num[index])
    index += 1


print("Using for loop")
sum = 0
for i in num:
    sum = sum +i
    print(i)
print(f"Sum of the numbers is {sum}")