         #append

'''
This method is used to add an element/item at the end of list

syntax: 
   append(element)   --->  append(s)
'''

#write a program to read scores of n players and display

n = int(input("Enter how many players are: "))
players = [] #here the n (entered value) of player will display

for i in range(n):
    s = int(input("Enter score "))
    players.append(s)

print(players)


'''
logic for this program is 

START

 1st ask to enter n

 then declare list name (here players[] )

 then write for statement (for i in range(n)  ---> here n we asked the user in 1st line of code)

 then again declare one variable called as 's' and ask for scores
 
 then write .append()  as it is use to add, items in empty list or at the end of list

 then print the list

END
'''
