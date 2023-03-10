#from goto import goto, label
from functools import reduce
import re
import sys
mylist = ["123", "456", "789"]
mylist = list(map(int, mylist))
def Login():
        try:
            print("Enter the Login-id:")
            inputs = int(input())
            for inp in mylist:
                if inputs == inp:
                    pass
        except:
            print("Please enter int")
            Login() 
def pword():
      try:
            print("Enter the Password:")
            password = input()
            flag = 0
            while True:
             if (len(password)<=8):
              flag =1
              break
             elif not re.search("[a-z]",password):
              flag =1
              break
             elif not re.search("[A-Z]",password):
              flag =1
              break
             elif not re.search("[0-9]",password):
              flag =1
              break
             elif not re.search("[_@$]",password):
              flag =1
              break
             else:
              flag = 0
              print("It is a Valid Password")
              break
            if flag==1:
                raise KeyError()
      except:
           print("Enter the Valid Password!")
           pword() 
def addproducts():
            print("Type Yes to add products")
            ipt = input()
            if ipt=="Yes" or ipt=="yes" or ipt=="YES":
               print("How many Products do you want to add?")
               ipt1 = int(input())
               print("Enter the Electronic product details")
               d = {}
               lambda ipt1: {input("Enter the name of child dictionary:"): {"Product_Name": input("Enter the product name: "), "Version": input("Enter Version: "), "Price": int(input("Enter Price: "))} for _ in range(ipt1)}
            print("Your Products are :")
            print(d) 
def Logout():
   exit()   
ulist = ["Kaviarasu", "Noname", "Newname"]
ulist = list(map(str.lower, ulist))
plist=["Kaviarasu@002","Noname@002","Newname@002"]
def UserLogin():
        try:
            print("\n\nEnter the Username:")
            Uinputs = input()
            for inp in ulist:
                if Uinputs == inp:
                    print("Success")
                    break
                else:
                    raise ValueError
        except:
            print("Please enter the correct Username")
            UserLogin()  
def password():
      try:
            print("\n\nEnter the Password:")
            Pinputs = input()
            for pwor in plist:
                if Pinputs == pwor:
                    txt="You are successfully Loginned"
                    print(txt.center(100,"-"))
                    break
                else:
                    raise ValueError
      except:
           print("Enter the Valid Password!")
           password() 
Fullproducts=[{'Si.no':'1','ProductName:':'Computer','Version:':'Windows 11','Price:':50000},
              {'Si.no':'2','ProductName:':'Oven','Version:':'7th Version','Price:':4000},
              {'Si.no':'3','ProductName:':'Electric Grill','Version:':'4th Version','Price:':2000},
              {'Si.no':'4','ProductName:':'Washing Machine','Version:':'2nd Version','Price:':10000}]
def viewproducts():
            print("Type yes to view products")
            confirm = input()
            if confirm=="Yes" or confirm=="YES" or confirm=="yes":
                print("\n\n{:<10} {:<20} {:<15} {:<10}".format('Si.no', 'Product Name', 'Version', 'Price'))
                for product in Fullproducts:
                    print("{:<10} {:<20} {:<15} {:<10}".format(product['Si.no'], product['ProductName:'], product['Version:'], product['Price:'])) 
                list1=[]
                for product in Fullproducts:
                    list1.append(product["Price:"])
                print("The total value of the product in the given products is:",reduce(lambda x, y: x+y, list1))
            else:
                print("You are exited.......due to pressed other characters.Please Relogin..")
                sys.exit()
class Payment:
    def __init__(self,amount):
        self.amount=amount
    def process_payment(self):
        print(f"""
               Your Payment is processing...... 
               The total amount is {self.amount}
              """)
class Cart:
           def __init__(self):
            self.items=[]
           def add_to_cart(self, product):
            self.items.append(product)
            print("\n\nProduct added to cart")
           def view_cart(self):
             if self.items:
              print("\n\nYour cart contains:")
             for product in self.items:
                print(product)
             print("\n\npress 1 to redirect to payment page........")
             confirm=int(input())
             if confirm==1:
                 payment=Payment(price)
                 payment.process_payment()
             else:
                 print("You are exited.....")
def orderproducts():
            print("\n\nType Si.No to Add your product to cart")
            confirm = int(input())
            if confirm < len(Fullproducts):
                  print("\n\nProduct Name :",Fullproducts[confirm]['ProductName:'])
                  print("Version :",Fullproducts[confirm]['Version:'])
                  print("Price :",Fullproducts[confirm]['Price:'])
                  product = {
                   'Product Name': Fullproducts[confirm]['ProductName:'],
                   'Version': Fullproducts[confirm]['Version:'],
                   'Price': Fullproducts[confirm]['Price:']
                   }
                  global price 
                  price = product['Price']
                  new=product.copy()
                  add=Cart()
                  add.add_to_cart(new)
                  add.view_cart()
            else:
                print("Please type the correct Si.no in the given product items")
                orderproducts()
print("Welcome to Ecart!!!!!!!!!\n")
txt="Admin or User"
print(txt.center(100,"-"))
print("If admin,type Yes else type No for User")
ipt=input()
if ipt=="Yes" or ipt=="yes" or ipt=="YES":
    Login()
    pword()
    addproducts()
    Logout()
elif ipt=="No" or ipt=="NO" or ipt=="no":
    UserLogin()
    password()
    viewproducts()
    orderproducts()
else:
  exit()
