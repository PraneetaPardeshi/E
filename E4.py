# Matchcase statements :->
#  these statements are used to match a certain cases such as given below.
x=int(input("Enter value for x : "))
match x :
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _:
        print(x,": default")  # Underscore(_) denotes the default statements in the case statements


print('\n')
x=int(input("Enter value for x : "))
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
        print(x,": default")
        #hi