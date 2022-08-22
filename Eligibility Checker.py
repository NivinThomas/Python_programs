age=int(input("Enter your age ?\n"))
lmt=18
if age>lmt:
    print("Eligible !"+" "+"Your age is : ",age)
    print("Age linit is : ",lmt)
else:
    print("Not Eligible ! under age limit"+" ",lmt)
    print("Enterd age is ",age)
