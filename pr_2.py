# Ask the user to enter age,gender(M or F), mrital status(Y or N)
#and then using following rules print their place of service
#if employee is female thrn she will work only in urban areas
# if enployee is male and age is between 20 to 40 then he may work anywhere
# if employee is male and age is between 40 to 60 then he will work in urban areas only 
# if age is anything else the print "ERROR" 
age= int(input("enter your age here: "))
mar = str(input("enter your marital status: "))
gen = str(input("enetr your gender here: "))
M = "male"
F = "female"
Y = "yes"
N= "no"
if gen == F: 
    print("will work only in urban areas")
elif gen == M and age > 20 and age <= 40:
    print("may work anywhere")
elif gen == M and age > 40 and age<= 60:
    print("will work in urban areas only")
else:
    print("ERROR")