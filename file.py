
file = open("student.txt","r+")



print("size")
print(len(file.read()))
print(file.read())
print("readline")
print("readlines")
print(file.readlines())

file.close()


fi = open("student.txt","r")
for line in fi:
    print(line) 
fi.close()
fi2 = open("student.txt","a")

print("write")
fi2.write("\nThis is a new line")



fi2.close()

fi3 = open("student2.txt","w")


print("write")
fi3.write("\nThis is a new line")
fi3.close()