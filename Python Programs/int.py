#write program to write a program to add two integers

a= input("enter first number:")
b = input("enter second number:")

c= int(a) + int(b)  # 
print(a,b, "sum is:", c)

c = int("ab", base=16)  # converting hexadecimal string to integer
print(type(c))
d = int("0xab", base=16)  # converting hexadecimal string with '0x' prefix to integer
print(type(d))
