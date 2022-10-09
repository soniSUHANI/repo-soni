#take input of age from 3 persons
#determine the oldest and youngest
first = int(input("enter first person age here: "))
second = int(input("enter second person age here: "))
third = int(input("enter third person age here: "))
 
if first>second and first>third:
    print("first is oldest")
elif second>first and second>third:
    print("second is oldest")
elif third>first and third>second:
    print("third is oldest")
elif first<second and second<third:
    print("first is youngest")
elif second<first and first<third:
    print("second is youngest")
elif third<first and third<second:
    print("third is youngest")
else: print("all have same age")