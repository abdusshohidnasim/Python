def sum (*a):
    total = 0
    for i in a:
        total += i
    return total
sum1 = sum(10, 20, 30, 40)
# ai khana lokhto rakbta hoba ja fris bracked ar modha as a parameter gulo ke sum function ar modha pathano hoba

print(sum1)

def detail (*a):
    print(a)
print(detail("Naiem", 22, "Dhaka", "Python Developer"))


def student3 (**a):
    print(a)
student3(name="Naiem", age=22, city="Dhaka", profession="Python Developer")
# **a mane hocche keyword argument gulo ke dictionary akare pathano hoba