def login():
    usernameInput=input("Username :")
    passwordInput=input("Password :")
    if usernameInput == "admin" and passwordInput == "1234" :
       print("Done")  
       return Showmenu() 
    else:
       return login()
def inputparameter():
    price1 = int(input("Price1 (THB) :"))
    price2 = int(input("Price2 (THB) :"))
    total = price1+price2
    return PriceCal(total)
def menuSelect(price01,price02):
    print("----PinkShop----")
    print("1.VAT Calculator")
    print("2.Price Calculator")
    userSelected=int(input(">>"))
    if userSelected==1:
       return VATcal(price01+price02)
    elif userSelected==2:
       return PriceCal(price01+price02)
    else:
        return menuSelect(price01,price02)

def Showmenu():
    price1 = int(input("Price1 (THB) :"))
    price2 = int(input("Price2 (THB) :"))
    return menuSelect(price1,price2)

def VATcal(total1):    
    VAT =7
    result= total1 + (total1*VAT/100)
    print(result)
    print(Showmenu())

def PriceCal(total2):
    print(total2)
    print(Showmenu())



#login()
#Showmenu()
#menuSelect()
#VATcal()
print(login())
