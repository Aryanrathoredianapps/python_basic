
# x=input("enter number")
# x=int(x)
# def my_fun(x):
#       return 5*x

# print(my_fun)
a =input("enter the first num")
b =input("enter the second num")
z = input("enter the operator")

a=int(a)

b=int(b)
def cal(x,y):
    if z=='+':
     return (x+y) 

    elif z=='-':
        return (x-y)
    
    elif z=='*':
        return (x*y)
    elif z=='/':
        return(x/y)
    else:
        print("enter valid operator")


print(cal(a,b))





