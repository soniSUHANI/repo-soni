#name = input("enter your name: ")
#print("good night " + name)
letter = '''Dear  <|NAME|>,
Greatings from us.You are selected in our company.
You are selected!
Have a nice day ahead!
Thanks and Regards.
Google
<|DATE|>'''
name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)