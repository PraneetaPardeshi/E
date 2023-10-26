# STRING OPERATIONS
# INDEXING ON STRINGS
# In Python the indexings starts with '0' from left to right
# & with -1 from right to left i.e inthe reverse direction
name="pihu"
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# print(name[4]) # throws an error
# this can be done with the help of 'for loop' 
for i in name:
    print(i)

# Operations on strings
fruits ="apple,banana,fig,kiwi,mango"
print(fruits[0:5])
print(fruits[0:12])
print(fruits[6:21])
# indexing starts from 0 uptil n-1 
n=len(fruits)
print(n)
print(fruits[0:n])

# len function : use to find the "length" of a string
print("the length of the string 'fruits' is :",len(fruits))


t="!!!praneeta!!!!!!!!!"
print(t)
print("length of t is : ",len(t))
# print(t[-1:-12])
print(t[-4:-2])
print(t.upper())
print(t.lower())

# strings are immutable
print(t.rstrip("!"))  #removes the characters only from behind.
print(t.replace("senita","praneeta"))
print(t.replace("!","$"))
print(t.split("!")) # ?????

v= 'xyzw'
print(v.capitalize())
# O/P: Xyzw  // thus it capitalizes only the first letter.

print("\n")
str1="welcome to python programming"
print(str1)
print(len(str1))
print(len(str1.center(50)))
print(str1.count("e"))
print(str1.endswith("!!!!"))
print(str1.endswith("to",4,10))
print(str1.find("to"))
print(str1.index("python"))
print(str1.index("ing"))
print(str1.index("p")) #gives the index value at the first occurance.

str2="welcomeToPythonProgrammig"
print(str2.isalnum()) #this method returns 'True' only if the entire string consists of alphanumeric characters(A-Z,a-z,0-9);
#if any other character or punctuation are present then it returns False
print("\n")

str3= "pihu369"
print(str3)
print(str3.isalnum())
print(str3.isalpha())  # returns 'True'  if there are alphabets only; otherwise 'False' .

print("\n")
str4="welcome to python programming\n"
print(str4.isprintable())#returns false due toh the character '\n' is not printable
print(str1.isspace()) #using spacebar

str5="  "
print(str5.isspace()) #using spacebar

print('\n')
str6="World Health Organization"
print(str6)
print(str6.istitle())
print(str1.istitle())
print(str1.startswith("welcome"))
print(str4.swapcase()) 
print(str4.title())