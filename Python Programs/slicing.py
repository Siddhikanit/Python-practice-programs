'''
              silicing

index - use for reading one value
silicing - use for reading more than one value

how its done
here how:

 1. using slicing operator
 2. using slice object


syntax 1:

 # sequence-name[::]  

        OR
 
 # sequence-name[:]

 
syntax 2:

 # sequence-name[::step]
   in this syntax start, stop vlaues are taken based on step value.

if step is +ve:   start = 0, stop = len(sequence)

if step is -ve: start = -1, stop = -(len(sequence) +1)


# if sidd, len is n = 4  s(0),i(1),d(2),d(3)
     (0:4)  
     sid (only 3 letter will print and 4th letter wont)
     [len(n)-2: 3]= [-2:3]   print: 2,3 = dd

'''


'''
#like append slicing is use to add more than one value

list = [1,34,5,6,7,8,4,56,3,5,63,64,2,3,88,524,6]

evenList = []
oddList = []

for value in list:
    if value%2 == 0:
        evenList.append(value)
    else:
        oddList.append(value)

print(f'List is{list}')
print(f'Even list is {evenList}')
print(f'OddList is {oddList}')

'''

#write a program to read name and n subject marks, calculate total average and result

#(heere we will use for loop, append)

#answer:
#ask name and declare one variable(ask n subjects) then one more variable which will print/show list
name = input("Enter name: ")
n = int(input("Enter number of subjects "))
marks = []

#use for loop here
for i in range(n):
    m = int(input("Enter marks "))          #here we will ask user for marks (if n = 2, m will execute 2 times to ask marks)
    marks.append(m)    #marks[] and m = int(input("enter marks ")) will store the value in marks[] list.
  

#write total,aveg,result
total = sum(marks)
average = total/n
result = 'pass'
for m in marks:        #use for statement here
    if m <40:
        result = 'fail'


#print
print(f'Name: {name}')
print(f'Marks: {marks}')
print(f'Total marks is: {total}')
print(f'Average marks is: {average: 2f}')
print(f'Result of {name} is: {result}')