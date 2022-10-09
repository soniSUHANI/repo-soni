# a company decided to give bonus of 1000rs to employee if his/her service is more than 
# 5 years ask user  their salary and year of service and print the net bonus amount

a = int(input("enter your salary here: "))
b = int(input("enter your year of service: "))

if b>5 :
    print("the net bonus amount: ",a+1000)
     
else:
    print("no bonus received")

