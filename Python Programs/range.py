  
   #range 
''' 
it is immutable sequence data type
After creating it u cant modify value. 
It is use to generate sequence of integer values.

Range also use to repeat for loop number of times.

1. start 
2. stop
3. step


       #syntax
1.   range(stop)
2.   range(start,stop,step)

eg.: range(stop)
range(10) -->  start = 0, step = 1
range(12) -->  start = 1, stop = 11, here step is +1   output will have 1,2,3,.....,11



r1 = range(20)
print(r1)

r1[4]             #how does it works for   i still dont know


r2 = range(20)
for value in r2:
  print(value)

'''

#range(start,stop,step)

'''
this syntax generate values in increment and decrement order

- if step is +ve the start < stop
- if step is -ve the start > stop              #what does it mean bruhhh    it mean when +ve is step integer sequence will on in increasing order, if -ve seq will be like (-1, -2,-3,-4,........)


'''

'''
  step is increment or decrement value

range (1,10)   --> start = 1, stop = 10, step =+1
 
'''


'''
range has 3 steps ( 1- start, 10- stop, +1 -->increment)
'''

# ques: write a program to print math table

#ask any number
num = int(input("Enter sny number: "))

#write for looop statement here
for i in range(1,11):         #this is how for syntax is 

#write formula or condition
 p = num *i      # p is new varible, num is the one we declared variable, i is from 'for' statement

#print with (f' {condition})
 print(f'{num} * {i} = {p}')   #here  p = num *i we write it inside curly bracket 




#ques: sum of n numbers

n = int(input("Enter the value of n "))    #it means how many numbers will be if 2 then it will ask enter 2 numbers
s = 0           #why this?
for i in range(n):
 num = int(input("Enter any number "))
 s = s+ num
print(f'Sum of numbers {s}')

