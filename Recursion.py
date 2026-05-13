# 4! what do tha hell is that? 4! = 4 * 3 * 2 * 1 = 24
def fat(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*fat(n-1)
    
print(fat(4))