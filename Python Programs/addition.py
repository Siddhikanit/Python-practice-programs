'''
arithmatic operator
  typically use for additon and for contcatenation(addtion of string, list)



n1 = 10
n2 = 30

n3 = n1 + n2
print(n1,n2,n3)

s1 = "python"
s2 = "is"
s3 = "programming"

s4=s1+s2+s3
print(s4)

l1= [10,20,24,40]
l2=[40,45,50,60]
l3 = l1+l2
print(l3)

'''


# write a program to input name and 2 subjects marks



#declare input name
name= input("enter your name ")               #syntax - x=input("string")
 

#declare 2 subjects marks

maths = int(input("enter marks"))
science = int(input("enter marks"))

#add input and 2 subjects marks
total =  maths+ science

#print
print("student name", name)
print("maths marks is", maths)
print("science marks is", science)
print("total marks is",total)