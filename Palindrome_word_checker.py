def pal(inp):
    if inp==inp[::-1]:
            print(inp," : is palindrome")
    else:
        print(inp," : Is a palindrome")
pal(inp=input("Enter the word tho check ?"))