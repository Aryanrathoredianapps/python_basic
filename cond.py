#if else condition


x=input("please enter your age ")
x=int(x)

if x <=18:
    print("you are not eligibel for party")

elif x >=18:
    print("you are  eligibel for party")

elif x ==18:
    print("you have to ask your parents for party")

else:
    print("enter valid age")


#calculator


x= input('enter the first number')
y=input ('enter the operator')
z= input("enter the second number")

x=int(x)
z=int(z)

if y=='+':
    print(x+z)

elif y=='-':
    print(x-z)

elif y=='*':
    print(x*z)

elif y=='/':
    print(x/z)

elif y=='%':
    print(x%z)
else:
    print("invalid operator")