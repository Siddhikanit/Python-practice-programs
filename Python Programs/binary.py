#write a program to add two binary numbers

a=int(input("enter integer in binary format"),base=2)  #mistake = braket was missing after format"
# learn syntax
# a= int(input("string"), base=2)   ---use for converting binary string to integer

b=int(input("enter integer in binary format"),base=2)
c=a+b
print(a,b,c)
print(bin(a),bin(b),bin(c))  #dont forget to use bin() to convert integer to binary string



