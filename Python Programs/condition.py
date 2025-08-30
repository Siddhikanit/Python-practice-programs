'''Conditional Operator
Conditional operator is a ternary(thrice maybe?) operator. This operator required 3
operands. This operator is used to create conditional expression.
1. if
2. else
'''


'''
## write a program to find max of 2 numbers

#declare 2 inputs
x = int(input("enter first number "))
y = int(input("enter second number "))

#write conditional statement  
z = x if x>y else y

#print
print("maximum number is", z)
'''



#write a program to find if person is eligible to vote or not

#declare inputs
#ask name
name = str(input("enter your name "))

#ask age
age = int(input("enter your age "))

#write condition and print  -this time print and condition at the same time

print(name, "you are elegible to vote") if age > 18  else print(name, "you are not elegible to vote")
