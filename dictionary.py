dic = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
}
print(dic)
print(dic[1])
print(dic.keys())
print(dic.values())
print(dic.items())
for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)

for key, value in dic.items():
    print(f"{key} : {value}")


print(dic.get(1))
print(dic.get(6, "Not Found"))
print(dic.get(3, "Not Found"))