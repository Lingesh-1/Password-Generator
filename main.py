#Password Generator

import random as r
print("Welcome To Password Generator!!!")
# a1l=list(string.printable)
# print(a1l)
al=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
num=['1','2','3','4','5','6','7','8','9','0']
sy=[ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

al1=int(input("How many letters would you like in your password:\n"))
num1=int(input("How many numbers would you like in your password:\n"))
sy1=int(input("How many Symbols would you like in your password:\n"))

#easy level
# passw=""
# for i in range(1,al1+1):
#     # r1=r.randint(0,al1-1)
#     passw+= r.choice(al)

# for i in range(1,num1+1):
#     r2=r.randint(0,num1-1)
#     passw+=num[r2]

# for i in range(1,sy1+1):
#     r3=r.randint(0,sy1-1)
#     passw+=sy[r3]

# print(f"Your Password is:{passw}")

passw=[]
for i in range(1,al1+1):
    # r1=r.randint(0,al1-1)
    passw.append(r.choice(al))

for i in range(1,num1+1):
    r2=r.randint(0,num1-1)
    passw.append(num[r2])

for i in range(1,sy1+1):
    r3=r.randint(0,sy1-1)
    passw.append(sy[r3])

r.shuffle(passw)

password=""
for i in range(len(passw)):
    password+=passw[i]
print(f"Your password is:{password}")
