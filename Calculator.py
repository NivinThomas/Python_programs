def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def mod(n1,n2):
    return(n1%n2)
print("SELECT AN OPERATION")
print("\n1.Addition\n")
print("\n2.Substraction\n")
print("\n3.Multiplication\n")
print("\n4.Division\n")
print("\n5.Reminder\n")
while True:
    inp=int(input("\nEnter your choice number\n"))
    if inp in('1','2','3','4','5'):
        n1=float(input("\nEnter the 1st number ?\n"))
        n2= float(input("\nEnter the 2nd number ?\n"))
        if inp=='1':
            print(n1, "+", n2, "=", add(n1, n2))
        elif inp=='2':
            print(n1,"-",n2,"=",sub(n1,n2))
        elif inp=='3':
            print(n1,"*",n2,"=",mul(n1,n2))
        elif inp =='4':
            print(n1, "/", n2, "=",div(n1, n2))
        elif inp == '5':
            print(n1, "%", n2, "=", mod(n1, n2))
else:
    print("Invalid Entry!")