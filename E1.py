# Topics: COMMENTS , TYPE_FUNCTION , CONCATENATION ,

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



# TYPE_FUNCTION
a = 2
b="pihu"
c=  True
d= None
e= 8+2j
f=("a","b","c","d")
g=[1,2,3,4,5]
h={69,79,89,99}
print("2 is:",a,type(a))
print("pihu is:",b,type(b))
print("True is:",c,type(c))
print("None is:",d,type(d))
print("8+2j is:",e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))


# CONCATENATION 
# it joins two or more strings together.
x=1
y=5
print(x,y,"x+y",x+y)

a = "Hello "
b=input("enter name:")
print(a,b,"a+b:",a+b)

s='2'
t='3'
print(s,t,"s+t:",s+t)

# TYPECASTING
string = "4"
number = "5"
print(string+number)
print(int(string)+int(number)) #this is an example of explicit typecasting
c=2.5
d=3
print("c+d=",c+d) #this is an exapmle of implicit typecasting,which means that the interper converts the one DT(here int) into another DT(here float)on its own
st= '''this is an exapmle of implicit typecasting,
which means that the interper converts
 the one DT(here int) into 
 another DT(here float)on its''' 
print(st)