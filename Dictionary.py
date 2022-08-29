dic={
    0:10,
    1:20
}
inp=input("Enter a key ?")
val=input("Enter a value ?")
if inp in dic:
    print("Key exists !")
else:
    dic[inp]=val
    print("Dictonry updated !",inp,val)