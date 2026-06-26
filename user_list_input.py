user_input= input("Enter a list of numbers separated by commas: ")
list1 = [int(x) for x in user_input.split(",")]
st = 0;
for num in list1:
    st = st + num

print(st)
_hjd = 34
print(bool(1))
a = [3,4,5]
b = [3,4,5]
print(a == b)
print("is")
print(a is b)
djf =  20 and 20
print(djf)
print(10%3)
number_offletter = 0 
number_offword= 0 
number_off_intger = 0

user_input = input("Enter a string: ")
for i in  user_input:
    i = i.lower()
    if(i >= "a" and i<= "z"):
        number_offletter += 1
    elif(i >= "0" and i <= "9"):
        number_off_intger += 1
    elif(i == " "):
        number_offword += 1

print("Number of letters:", number_offletter)
print("Number of words:", number_offword)
print("Number of integers:", number_off_intger + 1)
print("Number of letters:", number_offletter)
print("Number of words:", number_offword)
print("Number of integers:", number_off_intger + 1)