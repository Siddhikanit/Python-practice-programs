# OR operator 

#it returns false when only 2 operator are false   eg.: false / false / result will be false

'''
# truth table of OR operator

operator 1 / operator 2 / result

1. true / true / true
2. true / false / true
3. false / true / true
4. false / false / false    #returns false only when false - false


# we use "==" to declare or operator
'''

'''
# write a program to find alphabet is vowel or not

# ask input (alphabet)
alphabet = str(input ("Enter alphabet: "))

# condtion and print
print("Alphabet is vovel") if alphabet== 'a'or alphabet == 'i' or alphabet == 'o' or alphabet == 'e' or alphabet== 'u' else print("Alphabet is not vowel") 

#here syntax 

#if x =='a' or x=='b' or.......so on
# we cant use it like this:   if x == 'a' or 'b' else print(x is not equal to a)    if we write it like this else statement wont print


# using multiple condition operator

#write a program to find a number is -,+ or equal to 0

num = int(input("enter number "))
print("Number is +ve") if num > 0 else print("Number is -ve") if num < 0 else print("Number is Zero")   #syntax to compare multiple conddtion is >, < else



'''

#write a program to find if element is alphabet, digit, special character

#(write condition to write print if alphabet  or  digit  else special char    --this is wrong)
#remember always declare the input then apply print with condtion

#declare input
ch = input("enter any character ")
#condition and print
#print for alphabet                      #here syntax: (<=), ( >=) --use for comparison

print("alphabet") if(ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') else print("digit") if ch>='0' and ch <='9' else print("special character")
 
# we used here >= (for camparison), 'and' operator for comparing 2 operations 
# in alphabet function 2 operations are 1. ch >= 'a' , 2. ch <='z' 
#then we used 'else' to print digit and again use "and" to compare 2 operation 
# remember syntax >= 