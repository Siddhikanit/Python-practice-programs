'''

There are 3 types of formatting output

1. old style string formatting   (use in c language)
2. New style string formatting
3. F-string (use in python 3.8)


# Old style formatting

formatting characters or specifiers are
1. %d - decimal integer
2. %o - octal integer
3. %x - hexadecimal integer
4. %s - string
5. %f - float in fixed
6. %e - float in exponent
7. %c - character


#syntax is:
"formatting string"%(value,value,value)

"&" here this shi is called string interpolation operator

'''


'''
# que: write a program to find area of triangle

#ask base
base = int(input("Enter the base of traingle "))
#ask height
height = int(input("Enter the height of traingle "))
#put formula to find area'
#ask area (area= 0.5*length*height)
area = 0.5* base * height
#print by using"f string method (%)"
print("Area of trainle is %f"%(area))
print("Area of traingle is %2f"%(area))

'''

# ques 2
#write a program to input roll no, name , 2 subject marks
#calculate total , average , result


#ask roll no
roll_no = int(input("Enter your roll no. "))
#ask name
name = str(input("Enter your name "))
#ask subj 1
subject1 = int(input("Enter your python marks"))
#ask subj 2
subject2 = int(input("Enter your java marks "))
#write total( subj1 + subj2)
total = subject1 + subject2
#write average formula (average = subj 1 + subj 2 /2)
average = subject1 + subject2 / 2
#write result (result is pass by using comparision (>=,) and (if else))
result = "pass" if subject1 >= 20 and subject2 >= 20 else "fail"
#print all inputs
print("roll no.: %d"% roll_no)
print("name:  %s"%name)
print("subject1: %d" %subject1)
print("subject2: %d"%subject2)       #this is kinda like c language 
print("total: %d"%total)             #first write print("") like usual
print("average: %2f"%average)        #then inside print declare formatting sting (%) 
print("result: %s"%result)           # print("string &d,&s")%(already declared varible)
      