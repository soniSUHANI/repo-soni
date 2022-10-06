a = int(input("enter the first side of  triangle: "))
b = int(input("enter the second side of triangle: "))
c = int(input("enter the third side of triangle: "))
s = (a +b +c)/2
ar = (s*(s-a)*(s-b)*(s-c))**(0.5)
print("the area of the triangle is: ",ar)
