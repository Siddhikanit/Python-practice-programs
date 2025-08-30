'''
For Loop 

 it is use to read elements or values from iterable.     #what it means broo

for loop is "Iterator"


#syntax

for variable in iterable:
   statement -1
   statement -2
'''

'''

#write a program to find length of list

list = [10,30,40,50,60,50,50,640]
c= 0
for num in list:
    c = c + 1          #ig this use to find lenth (c = c+1)
print(f'List is{list}')
print(f'count is{c}')       #for count {c} is use


'''


#program to print the sum of elements of list

list = [10,20,30,40,50]

s = 0           #declaring the s for a sum, (but y gave it 0 value??)


for value in list:
  s = s+value 

print(f'list is{list}')         #it prints the list elements
print(f'sum of elements are {s}')   #it shows the sum



#write program to find the smallest value within list

list1 = [10,50,20,404,40,20,60]

minvalue = list1[0]      #here we declared the minimum or smallest value

for value in list1:         # always write for then in  "declared item" , and it must end with :
  
   if  value < minvalue:               #remember this thaat alwwayss give ':' after if statement
      minvalue = value


print(f'list is {list}')
print(f'smallest value is {minvalue}')




'''
note---------
remember 

first we write
for______in (variable declared):   ':' is important
  if value in ():     here ':' is imp tooo


Syntax:
for variable in iterable:
	statement-1
	statement-2

'''