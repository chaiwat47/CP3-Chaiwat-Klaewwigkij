usernameInput=input("Username :")
passwordInput=input("Password :")
if usernameInput == "admin" and passwordInput == "1234" :
	print("---Welcome to Pink Shop---")
	print("1.Shirt 120 THB/unit")
	print("2.Dress 100 THB/unit")
	print("3.Plant 240 THB/unit")
	NumbChoose=int(input("Please Choose Item:"))
	CountItem=int(input("Please Count Item:"))
	if NumbChoose==1 :
		print("Price:",120*CountItem,"THB")
		print("---Thank You----")
	elif NumbChoose==2 :
		print("Price:",120*CountItem,"THB")
		print("---Thank You----")
	elif NumbChoose==3 :
		print("Price:",240*CountItem,"THB")
		print("---Thank You----")
	else:
		print("Don't have any item")
else:
	print("Incorrect")
