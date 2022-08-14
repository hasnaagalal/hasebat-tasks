#Create a Boolean variable named x
x = False
#Create an integer variable named y
y = 3
#Create a float variable named z
z = 5.3
# Create a string variable names s

s = 'hasnaa'
#Convert the int variable to float

y = float(y)
# Can we convert the str to int ?
'yes'
#Create a list of numbers from 1 to 5

numbers = [1,2,3,4,5]
#Create a tuple from 10 to 15

t = (10,11,12,13,14,15)
# Convert the list to tuple
numbers = tuple(numbers)
#Create a dict of 3 values
dic = {'name':'hasnaa','age':21}
# Can we use semi colon ; with python

'''yes , if there more than one statement in a line '''
#Python is interpreted or compiled ?
'python is interpreted'
#What is the differences between low level & high level

'''low level is machine language , it is tough to understand 
high level is programer friendly language , easy to understand  '''
#What is the differences between = , ==
'''= is an assignment operator
but == is a comparison operator'''
#What do we mean by using !=
'not equal'
#What is the operator precedence
'''the order of operations.'''
# Create a variable x with value of 10

x = 10
#Increase x value by 15 using assignment operators
x += 15
# Divide the x value by 5 using assignment operators

x /= 5
#Multiply the x value by 10 using assignment operator

x *= 10
#Get module of x on 3 using assignment operators
x %=3
#Using python print the module of 11 to 4
print(11%4)
#Print the exponent of 2,3
print(2**3)
#Divide 11 by 3 using python division
print(11/3)
#Can we divide 11 by 3 and get an integer number ?
print(int(11/3))
#Check if 10 is bigger than 15 or not

print(10>15)
# If 10 is not bigger than15 print x is smaller than 15
if 10 < 15:
    print('x is smaller than 15')
#In which cases we will use all
''' it returns True if all items in an iterable are true, otherwise it returns False , we use it in multiple statement of and'''
#What is the differences between all , and
''' all is a multiple statement of and , and is for one condition but all for a lot of and conditions'''
#What is the differences between any , or
''' any is multiple statement of or , any for a lot of or conditions but or is for one condition '''
# If we need all the conditions to be true we will use ….
'''all'''
#What is the differences between if , elif

''' if : it finds one condition that is True, it stops and doesn't evaluate the rest.
but elif is used when the conditions are mutually exclusive.'''
# What is the differences between elif else
'''elif is used when the conditions are mutually exclusive
but else is uesd in the last case of all in the if statement '''
#Can we use more than one elif

'yes'
# Can we use more than one else
'no'
#write s simple ternary operator
name = 'hasnaa' 
print ("welcome") if name == 'hasnaa' else print ("who you are")
#in elif , python will check all the conditions no matter what ?

'no'
#in elif we use else for ... ?
'for the last condition'
#if we have this list [2,4,6,8,10] :

l=[2,4,6,8,10]
# ○ check to see if 4 in this list or not
if 4 in l :
    print ('true')
else :
    print('false')
# ○ check to see if 4 and 6 in this list on not
if 4 in l and 6 in l :
    print('true')
else :
    print('false')
# ○ check to see if 3 or 6 in this list
if 3 in l or 6 in l :
    print('true')
else :
    print('false')
# ○ check to see if 2 , 4 and 5 in this list
if all ([2 in l,4 in l ,5 in l]):
    print('true')
else :
    print('false')


    

