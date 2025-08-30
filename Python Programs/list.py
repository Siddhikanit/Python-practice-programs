#write a program to swap twp elements in a list

list1 = [10,20,30,40,50,60,70,80,90]  #here we declared the list and its elements 
print(f'before swaping the list {list1}')  #here we wrote print(f'sring') because its syntax is like this, when we use print with f we use single string

#now asking user where to swap 
#1st element
p1 = int(input("Enter position1 "))
#2nd element
p2 = int(input("Enter position 2 "))

#heres big deal
temp = list1[p1]  #idk what this shi is
list1 [p1] = list1 [p2]   #ig this use for swapping
#its saying that, we asked 1st element is equal to 2nd asked element

list1 [p2] = temp #now this 

#print using new formatting string [f' {} ']
print(f'after swaping{list1}')