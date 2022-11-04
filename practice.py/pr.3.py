#take 3 user inputs nad check the all 3 inputs can form a triangle or not
s1 = int(input("enter first side of triangle: "))
s2 = int(input("enter second side of triangle: "))
s3 = int(input("enter third side of triangle: "))
if s1+s2>s3:
    print("it is a triangle")
elif s1+s3>s2:
    print("it is a triangle")
elif s2+s3>s1:
    print("it is a triangle")
else:
    print("it is not a triangle")