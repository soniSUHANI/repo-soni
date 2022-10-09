#take inputs from user(int/float)
#print the greatest number

a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a>b:
    print("a is greatest")
elif b>a:
    print("b is greatest")
else:
    print("both are same")