# Comments
# comments can be added with the help of "#" symbol or within triple quotes(''' hugrur''')or("""rggttr""")
""""kjgkfjjlfmkgknn
ggkgjkgjkgljfbmb,
kkgjkgjkgkghk"""
print("jhjxbnxnbjsk")
# ctrl+/ ....is a vscode shortcut key to make any line a comment.

# escape sequence characters
# "\n" this is character is to change the line,for example
print("hello  world\nWelcome to python programming")

#"\'" this is another sequence character which is used to implement multi-statement within a quote, for example:

# 'sep' character, for exp.

# type_function
'''a = 2
b="pihu"
c=  True
d= None
e= 8+2j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''

# Concatenation 
'''x=1
y=5
print(x+y)
a = "Hello "
# b=input("enter name:")
print(a+b)'''

# alt+shift+down arrow.....is a shortcut in vscode to replicate the above line
# alt+shift+down arrow.....is a shortcut in vscode to replicate the above line
# alt+shift+down arrow.....is a shortcut in vscode to replicate the above line

# TYPECASTING
'''string = "4"
number = "5"
print(string+number)
print(int(string)+int(number)) #this is an example of explicit typecasting
c=2.5
d=3
print("c+d=",c+d)''' #this is an exapmle of implicit typecasting,which means that the interper converts the one DT(here int) into another DT(here float)on its own
'''st= this is an exapmle of implicit typecasting,
which means that the interper converts
 the one DT(here int) into 
 another DT(here float)on its 
print(st)'''

# STRING OPERATIONS
# INDEXING ON STRINGS
# In Python the indexings starts with '0' from left to right
# & with -1 from right to left i.e inthe reverse direction
'''name="pihu"
print(name[0])
print(name[1])
print(name[2])
print(name[3])'''
# print(name[4]) # throws an error
# this can be done with the help of 'for loop' 
'''for i in name:
    print(i)'''

# Operations on strings
'''fruits ="apple,banana,fig,kiwi,mango"
print(fruits[0:5])
print(fruits[0:12])
print(fruits[6:21])'''
# indexing starts from 0 uptil n-1 
# print(fruits[0:n-1])

# len function : use to find the "length" of a string
'''print("the length of the string 'fruits' is :",len(fruits))'''

'''t="!!!seneeta!!!!!!!!!"
print(t)
print("length of t is : ",len(t))'''

# print(t[-1:-3])
'''print(t[-4:-2])
print(t.upper())
print(t.lower())
# strings are immutable
print(t.rstrip("!"))
print(t.replace("senita","praneeta"))
print(t.replace("!","$"))
print(t.split("!"))
v= 'xyzw'
print(v.capitalize())
str1="welcome to python programming"
print(len(str1))
print(len(str1.center(50)))
print(t.count("e"))
print(str1.endswith("!!!!"))
print(str1.endswith("to",4,10))
print(str1.find("to"))
print(str1.index("python"))
str2="welcomeToPythonProgrammig"
print(str2.isalnum()) #this method returns 'True' only if the entire string consists of alphanumeric characters(A-Z,a-z,0-9);if any other character or punctuation are present then it returns False
str3= "Gaddu369"
print(str3.isalnum())
print(str3.isalpha())
str4="welcome to python programming\n"
print(str4.isprintable())#returns false due toh the character '\n' is not printable
print(str1.isspace()) #using spacebar
str5="  "
print(str5.isspace()) #using spacebar
str6="World Health Organization"
print(str6.istitle())
print(str1.istitle())
print(str1.startswith("welcome"))
print(str4.swapcase())
print(str4.title())'''


# Matchcase statements :->
#  Matchcase statements :-> 
'''x=int(input("Enter value for x : "))
match x :
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _:
        print(x,": default")'''  # Underscore(_) denotes the default statements in the case statements


'''x=int(input("Enter value for x : "))
match x :
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,": is not 80")
    case _ :
        print(x,": default")'''

# LOOPS IN PYTHON
'''name ='Pranita'
for i in name:
    print(i)'''

# loops in List
'''colors=["red","blue","pink","purple"]
for color in colors:
    print(color)
    for i in color:
        print(i)'''

# range functions in loops
# it starts from zero and ends on n-1 of the given range
'''for i in range(5):
    print(i)'''

# it starts from zero and ends on n of the given range
'''for i in range(5):
    print(i+1)'''

'''for i in range(5):
    print(i+2)'''

# it starts from zero and ends on n-1 of the given range
'''for i in range(1,9):
    print(i) '''

'''for i in range(0,101):
    print(i)'''

# TASK :-> print odd numbers from 1-20
'''for i in range(1,20,2):
    print(i)'''


# TASK :-> print even numbers from 1-20
'''for i in range(2,21,2):
    print(i)'''
# WHILE LOOP IN PYTON

# this is an example of "Incrementing while loop"
'''i=0
while(i<=3):
    print(i)
    i=i+1
print("Done with the loop")'''


'''i=int(input("enter the value:"))
while(i<=30):
    i=int(input("enter the value:"))
    print(i)'''

# this is an example of "Decrementing while loop"
'''count=5
while (count>=0):
    print(count)
    count=count-1'''

# while loop can be used with 'else'
'''count=5
while (count>=0):
    print(count)
    count=count-1
else:
      print("I'm inside else")''' #when is loop is over it switches to 'else' conditiion as shown in this example

# this a table using for loop
'''for i in range(12):
    print("5 X",i+1,"=",5*(i+1))'''

# BREAK & CONTINUE STATEMENTS
'''for i in range(12):
    print("5 X",i+1,"=",5*(i+1))
    if (i==9):
        break'''  #Break statement skips the whole loop

'''i=1
for i in range(12):
    if (i==5):  
        continue   # Continue statements skips an iteration(a particular line)
        print("5 X",i+1,"=",5*(i+1))'''

# FUNCTIONS IN PYTHON
'''def CalculateGmean(a,b):
    gmean=a*b/(a+b)
    print(gmean)
a=9
b=8
CalculateGmean(a,b)
c=8
d=7
CalculateGmean(c,d)'''
#  in this waywe have defined a FUNCTION to calculate the Geometric mean of any given number. 'CalculateGmean' is a user defined function whereas '(a,b)' arguements.
#  As we can see in the code we didn't have to write the formula again for c,d ; this isnhow the "def" function works.


'''def CalculateGmean(a,b):
    gmean=a*b/(a+b)
    print(gmean)
def IsGreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater")  
def IsLesser(a,b):
    pass  # 'pass' means that I'll write this code later , don't need to do anything about it.
a=9
b=8
IsGreater(a,b)
CalculateGmean(a,b)
c=8
d=12
IsGreater(c,d)
CalculateGmean(c,d)'''

# FUNCTION ARGUEMENTS IN PYTHON
'''def average(a=9,b=1):
    print("The average is", (a+b)/2)
average(4,6)
print("\n")'''
# there are four types of arguements we can perform in a function they are: Deafault arg; Keyword arg; Variable Length arg; Required.
# the given values for a and b in the first line of code are my "Deafault arguements".
# but if I gave anothe values (as showm in third line of code, I gave the values '4,6') it will ignore the deafault values.
#  now if I give the value only for a :
'''def average(a=9,b=1):
    print("The average is", (a+b)/2)
average(5)
print("\n")'''

#  thus the output gives the value "3.0" which is the average : (5+1)/2 = 3.0
#  similarly I an give the value for b
'''def average(a=9,b=1):
    print("The average is", (a+b)/2)
average(b=9)
print("\n")'''
# the output is:(9+9)/2=9.0

'''def name(Fname,Mname="John",Lname="abc"):
    print("Hello!",Fname,Mname,Lname)
name("Eeta")'''

#  KEYWORD ARGUEMENTS - we can provide arguements in 'key-value' form, irrespective of the order, this way the interpreter recognizes the arguements by parameter name.
'''def average(a=9,b=1):
    print("The average is", (a+b)/2)
average(b=2,a=6)'''

#  REQUIRED ARGUEMENTS- in case if you dont give the default value , it is mandatory to pass the arguement in the corect positional order.
'''def average(a,b,c=1):
    print("The average is", (a+b+c)/3)
average(3,5)'''

#  If I want to calculate the average of many number:
'''def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))
average(4,5,6,7,5,3,45,56,7,8,9,0,7,5,4,3,2,4)'''
# *numbers is my iterable, i can gives as many values as i want ,(*numbers) becomes my tuple.

'''def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
A=average(4,5,6,7,5)
print(A)'''
#  return statement is used to return the value of the function back to the calling function.


# LISTS in python
# list is a funtion in python which helps us to multiple  data types within an entity/name, where it could be referred easily and altogether.
# listbis an oredered set of data elements. List items are enclosed within square brackets and seperated by comma. Lists are mutable.
#  for example:
'''A=["pihu", 19, 'third year',True,1,2,3,4,5,6,7,8,9,69,96,969,696,6969]
print(A)
print(type(A))'''

#  List also consists of imdexing as we saw in string,which begins with '0'
'''print(A[0])
print(A[1])
print(A[2])
print(A[-1])
print(A[:]) # this will also print the whole list.
print(A[0:2])
print(A[1:-5])
print(A[1:15:2]) # '2' given here is known is known as the 'jump index' that means it will jump directly with the provided spacing
print(len(A))'''


'''if "pihu" in A:
    print("yes")
else:
    print("no")'''

# List Comprehension
'''list1=[i for i in range(9)]
list2=[i*i for i in range(5)]
list3=[i*i for i in range(9) if i%2==0]
print(list1)
print(list2)
print(list3)'''


# LIST METHODS 
l=[1,21,34,45,2,3,4,5,6,1]
print(l)

'''l.append(69)  # append help to add an element in the end of the list.
print(l)'''

'''l.sort()''' # sort helps us to arrange the elements in the ascending or descending order.
# print(l)

'''l.sort(reverse=True)''' # with the help of these we can arrange the elements in the descending order.
# print(l)

'''l.reverse
print(l)'''

'''print(l.index(69))'''  # index gives the index value that is the position of the index where the element is.
'''print(l.index(1))''' # this method returns the firt occurancr the first occurance of the index element.

'''print(l.count(1))''' #this method helps to count the number of times the element occurs on a list.

'''m=l
m[0]= 25  # as m=l; thus if we change anything in m it'll be changed in l too. as m is nothing but the reference of l.
print(l)'''

'''n=l.copy() # it copies the list, n now if you change anything in n  it will not be changed in l.
print(n)'''

'''l.insert(1,699) #it helps you to insert an element at the given index(here 1 is the given idex and 699 is the elements alloted to the index in the list)
print(l)'''
p=[100,200,300,400,500]

'''print(p)
# extend function helps to join two or more lists together 
l.extend(p)
print(l)'''
# Another way to concatenate the two lists are :
'''k= l+p
print(k)'''



# TUPLES IN PYTHON. 
# always remember that tuples are immutable. 
# tuples are represented by parenthesis and the elements are seperated by comma.

'''tup=(12,23,34,45,56,"abcd",True)
print(type(tup),tup)
print(len(tup))'''

'''print(tup[0]) # it helps to find the elements at the given index position.
print(tup[1])
print(tup[2])
print(tup[3])'''
# tuples also support positive and negative indexing.
'''print(tup[-4])''' # total length=7; 7-4 =3; it will print the element at index '3'.

'''if 69 in tup:
    print("yes")   #in this way the conditions could be checked in the tuple.
else:
    print("no")'''

'''tup2=tup[2:6]
print(tup2)''' # slicing can be done in a tuple.


# new topic : f-Strings in python.
# f-Strings in python.
#  "##" means to un-comment the points while running the points.

str1="Hey my name is {} and I am from {}"
name="Pihu"
country="India"
## print(str1.format(name,country)) ##
# O/P : Hey my name is Pihu and I am from India

str1="Hey my name is {} and I am from {}"
name="Pihu"
country="India"
## print(str1.format(country,name))##
# O/P: Hey my name is India and I am from Pihu
# Position of the variable matters here.

str1="Hey my name is {1} and I am from {0}"
name="Pihu"
country="India"
# #print(str1.format(country,name))##
# O/P: Hey my name is Pihu and I am from India
# this method is not convienient in formatting huge programs. 
# Therefore we use a technique known as "f-strings".

## print(f"Hey my name is {name} and I am from {country}")##
# O/P: Hey my name is Pihu and I am from India
# thus f-strings populates the values of name and country in this way.


##txt="for only {price:.2f}rupees"
## print(txt.format(price=69.6969696969))##
# O/P: for only 69.70rupees  # thus it gives a round_figure or first two values after a decimal point
##txt="for only {price:.4f} rupees"
## print(txt.format(price=69.6969696969))##
# O/P:for only 69.6970 rupees

# lets try it f-strings
price= 69.696969
txt=f"for only {price:.2f} rupees"
## print(txt)
# O/P:for only 69.70 rupees

##print(f"{2*6}")
# O/P: 12 # thus it can be evaluated then n there by f""

##print(type(f"{2*6}"))
#O/P: <class 'str'>

##print(f"we use f-strings in this way: Hey my name is {{name}} and I am from {{country}} ")
#O/P: we use f-strings in this way: Hey my name is {name} and I am from {country} 
# in this way we can print the raw string.



# DOCSTRING IN PYTHIN
# Python docstrings are the string literals that appear right after the definition of a function, method, class or module.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

print(square.__doc__)
# O/P: Takes in a number n, returns the square of n
#  thus { '''Takes in a number n, returns the square of n'''}this is not a normal string, python gives a special treatment to such strings ,
# it just needed to be written under some def function.
# the main difference between comments and docstring is that python completely ignores the comments but not the docstrings.
# VIP: Docstrings can be written right above the function definition. to make it a valid docstring


# VIP: PEP8 (Python Enhancement Proposal)
#  - it is a document that provides guidance and best pratice on how to write the python code.
#    the primary focus of PEP8 is to grow consistency and readability in python.

#  The Zen of Python
# Terminal -> python -> import this -> 
# O/P: The Zen of Python, by Tim Peters

'''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


# RECURSION IN PYTHON.
# is the process of defining something in terms of  itself


# ###factorial###
'''n=int(input("n:"))
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))'''
#  here we use python recurrsion 


# ####FIBONACCI SERIES###
#  write a program to print the fibonacci sequence
''' def Fibonacci(n):
 
    if n < 0:
        print("Incorrect input")
 
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
print(Fibonacci(8))'''


'''n = int(input("n:"))
a = 0
b = 1
next_number = b
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    a , b = b, next_number
    next_number = a + b
print()'''

























































