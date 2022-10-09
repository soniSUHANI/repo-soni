#company will give bonus based on foolowing criteria 

#time spent in company                        bonus
#  greater then 10 years                       10%
#  more than 6 and less than 10                8%
#  less than 6                                  5%

#ask the salary and time spent from the user 
#print the net bonus ammount accordingly

salary = int(input("ener your salary: "))
time = int(input("enter your time spent: "))
if time >= 10:
    print(salary+(10/100)*salary)
elif time >=6 and time <10 :
    print(salary+ (8/100)*salary)
elif time < 6:
    print(salary+(5/100)*salary)