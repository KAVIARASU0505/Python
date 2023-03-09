print("Welcome to Ecart!!!!!!!!!\n")
txt="Admin or User"
print(txt.center(100,"-"))
print("If admin,type Yes else type No for User")
ipt=input()
if ipt=="Yes":
 active=True
else:
  active=False
if active:
  class admin_areana:
    print("Enter the Login-id:")
    input1=int(input())
    print("Enter the Password:")
    input2=input()
    print("You are successfully logined!")
    print("Type Yes to add products")
    input3=input()
    if input3=="Yes":
      pass