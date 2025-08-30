'''

New style string formatting
-It is done using format method provided by string data types or class

#syntax: "formatting string".format(value,value,value)
NEW-STYLE : {name: d}  for decimal integer
            {name: s}  for string
            {name: f}  for float

            
# note:   position starts with 0
          here, {name(replaced by (0)): d} = {0: d}

eg. 
a= 10
b =12
print("{0: d}, {1:d}").format(a,b))
'''

#ques 1 write a program to find simple interest
#simple intrest = p*t*r (p= amount,t =time, r = rate)

#ask amount
amount = int(input("Enter amount "))
#ask time
time = int(input("Enter time "))   
#ask rate
rate = int(input("Enter rate"))  # also write it as [float(input(""))]
#formula of simple intrest (si = p*t*r)
si = amount * time * rate
#print using new formatting        method 1 ( {0: d},{1: d}, {2:d}.format(si))   nooooooo  
                                #  method 2 {:.2f}.format(simple intrest or   whatver its written in formula
# idk why we used .2f
print("simple intrest is {:.2f}".format(si))



'''
d = decimal integer
o = octal integer
s = string
f = float
c = character
e = float in exponent
b = binary

'''