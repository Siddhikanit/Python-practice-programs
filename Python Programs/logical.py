#logical operator
# it is used to combine one or more conditons


'''
in python, logical operators are represented using 3 keywords:
1. AND
2. OR
3. NOT

#truth table of AND operator

operator 1/ operator 2 / result

1. true / true / true               #in AND only true true gives true else others are false
2. true / false / false            
3. false / true / false
4. false / false / false


#if any operands is false it returns false
'''


# que.: write a program to check result of student

#ask name
name = str(input("student name "))
# ask subject marks
subject1 = int(input("enter science marks "))
subject2 = int(input("enter python marks "))
subject3 = int(input("enter c marks "))

#put condition and print
if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
    print(name, "you are pass")
else:
    print(name, "you are failed")



'''
Assigment operator or Agumented assignment statements:


Augumented assignment is combination,
in a single statement
of binary operation and an assignment statement.

1. +=
2. -=
3. *=
4. /=
5. //=
6. %=
7. **=
8. >>=
9. <<=
10. &=
11. |=
12. ^=
'''