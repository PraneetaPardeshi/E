# Mini Calculator
print("Welcome to mini calculator")
print("select_calculation_type:Simple Arithematic(A)\n                        Number coversion(N)\n                        Assignment Operators(ASG):")
select_calculation_type=input("enter from the above options :")
print("select_calculation_type=",select_calculation_type)
if select_calculation_type == 'A':
    print("Simple Arithematic Calculations")
    a=int(input("Enter value for a :"))
    opr=input("Select arithematic operator from= '+','-','*','/','//','%': ")
    b=int(input("Enter value for b :"))
    print(a,opr,b)
    if opr== '+' :
        print("ANS:",a,opr,b,"=",a+b)
    elif opr== '-' :
        print("ANS:",a,opr,b,"=",a-b)
    elif opr== '-' :
        print("ANS:",a,opr,b,"=",a-b)
    elif opr== '*' :
        print("ANS:",a,opr,b,"=",a*b)
    elif opr== '/' :
        print("ANS:",a,opr,b,"=",a/b)
    elif opr== '//' :
        print("ANS:",a,opr,b,"=",a//b)
    elif opr== '%' :
        print("ANS:",a,opr,b,"=",a%b)        
    else:
        print("Invalid syntax")
elif  select_calculation_type == 'ASG':
    print("Assignment Operators")
    a=int(input("Enter value for a :"))
    opr=input("Select arithematic operator from= '==','!=','>','<','>=','<=': ")
    b=int(input("Enter value for b :"))
    print(a,opr,b)
    if opr =='==':
        print(a==b)
    elif opr =='!=':
        print(a!=b)
    elif opr =='<':
        print(a<b)
    elif opr =='>':
        print(a>b)
    elif opr =='>=':
        print(a>=b)
    elif opr =='<=':
        print(a<=b)
    else:
     print("Invalid syntax")
elif select_calculation_type == 'N':
    print("Number Conversion")
    print("Enter select_conversion_type : ")
    print("Options:B-D,B-O,B-H\n        D-B,D-O,D-H\n        O-B,O-D,O-H\n        H-B,H-D,H-O")
    select_conversion_type = input("Enter select_conversion_type : ")
    if select_conversion_type == 'B-D':
        print("Binary to Decimal")
    elif select_conversion_type== 'B-O':
        print("Binary to Octal")
    elif select_conversion_type== 'B-H':
        print("Binar to Hexadecimal")
    elif select_conversion_type== 'D-B':
        print("Decimal to Binary")
    elif select_conversion_type== 'D-O':
        print("Decimal to Octal")
    elif select_conversion_type== 'D-H':
        print("Decimal to hexadecimal")
    elif select_conversion_type== 'O-B':
        print("Octal to Binary")
    elif select_conversion_type== 'O-D':
        print("Octal to Decimal")
    elif select_conversion_type== 'O-H':
        print("octal to Hexadecimal")
    elif select_conversion_type== 'H-B':
        print("Hexadecimal to Binary")
    elif select_conversion_type== 'H-D':
        print("Hexadecimal to Decimal")
    elif select_conversion_type== 'H-O':
        print("Hexadecimal to Octal")
    else:
     print("Invalid syntax")   

      
          
    


       
else:
     print("Invalid syntax")            