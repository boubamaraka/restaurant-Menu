from tkinter import *
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_Input = StringVar()
operator = ""
result = 0
#top frame
Tops = Frame(root,width = 1600, bg = "powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

#left content
f1 = Frame(root,width = 800, height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

#right content
f2 = Frame(root,width = 300, height = 700, bg = "powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

#current time 
localtime = time.asctime(time.localtime(time.time()))

# label info
labelInfo = Label(Tops,font=('arial',40,'bold'), text="Restaurant Management Systems", fg="Steel Blue", bd=10, anchor="w")
labelInfo.grid(row=0,column=0)

# Time display in label 
labelTime = Label(Tops,font=('arial',20,'bold'), text=localtime, fg="Steel Blue", bd=10, anchor="w")
labelTime.grid(row=1,column=0)

#================Calculator===================================
def btnClick(num):
	global operator , result
	operator = operator + str(num)
	#result += int(num) 
	text_Input.set(operator)
def btnResult():
	global operator , result
	result = str(eval(operator))
	#result += int(num) 
	text_Input.set(result)
def btnClear():
	global operator
	operator = ""
	text_Input.set("")
def btnTotal():
	x = random.randint(12000,299999)
	randomRef = str(x)
	rand.set(randomRef)
	# retrieve variable from input field
	CFries= float(Fries.get()) * 0.99
	CBurger= float(Burger.get()) * 1.00
	CFish= float(Fish.get()) * 1.23
	CCheese= float(Cheese.get()) * 0.23
	CChicken= float(Chicken.get()) * 3.67
	CDrinks= float(Drinks.get()) * 1.23
	costMeal ="£ "+ str((CFries + CBurger + CFish + CCheese + CChicken + CDrinks))
	paytax = ((CFries + CBurger + CFish + CCheese + CChicken + CDrinks) * 0.2)
	TotalCost = (CFries + CBurger + CFish + CCheese + CChicken + CDrinks + paytax)
	Service_charge  = TotalCost / 99
	Service_charges = "£ " + str(Service_charge)
	OverallCost = TotalCost + Service_charge
	Price.set(costMeal)
	Tax.set(paytax)
	SubTotal.set(TotalCost)
	Service.set(Service_charges)
	Total.set(OverallCost)

def btnReset():
	rand.set("")
	Fries.set("")
	Burger.set("")
	Fish.set("")
	Cheese.set("")
	Chicken.set("")
	Drinks.set("")
	Tax.set("")
	Price.set("")
	Service.set("")
	SubTotal.set("")
	Total.set("")
def btnExit():
	root.destroy()
textView = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,bg="powder blue", justify = "right")
textView.grid(columnspan=4)
#--------------------- calculator first row buttons--------------------------------------------------------------------------
btn7 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="7", bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="8", bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="9", bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)
#Calculator x Operators
Addition =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="+", bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)

#--------------------calculator second row buttons-----------------------------------------------------------------------------
btn4 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="4", bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="5", bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="6", bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)
#Calculator - Operators
Substraction =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="-", bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)

#------------------------------ calculator third row buttons--------------------------------------------------------------------------------------
btn1 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="1", bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="2", bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="3", bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=2)
#Calculator + Operators
Multiplication =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="x", bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)
#------------------------------ calculator last row buttons--------------------------------------------------------------------------------------
btn0 =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="0", bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="C", bg="powder blue",command=btnClear).grid(row=5,column=1)
# result 
result =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="=", bg="powder blue",command=lambda:btnResult()).grid(row=5,column=2)
Division =Button(f2,padx=16, pady=16, bd=8, fg="black",font=('arial',20,'bold'),text="/", bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)

#=====================================Restaurant Meal Info ====================================================
rand = StringVar()
#rand.set(random.randint(0,299999))
Fries = StringVar()
Burger = StringVar()
Fish = StringVar()
Cheese = StringVar()
Chicken = StringVar()
Drinks = StringVar()
Tax = StringVar()
Price = StringVar()
Service = StringVar()
SubTotal = StringVar()
Total = StringVar()
# --------------------------referance ----------------------
labelReferance = Label(f1,font=('arial',16,'bold'),text="Reference", bd=16, anchor="w")
labelReferance.grid(row=0,column=0)
textReferance = Entry(f1,font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textReferance.grid(row=0,column=1)

# --------------------------Fries ----------------------
labelFries = Label(f1,font=('arial',16,'bold'),text="Fries", bd=16, anchor="w")
labelFries.grid(row=1,column=0)
textFries = Entry(f1,font=('arial',16,'bold'),textvariable=Fries, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textFries.grid(row=1,column=1)

# --------------------------Burger ----------------------
labelBurger = Label(f1,font=('arial',16,'bold'),text="Burger", bd=16, anchor="w")
labelBurger.grid(row=2,column=0)
textBurger = Entry(f1,font=('arial',16,'bold'),textvariable=Burger, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textBurger.grid(row=2,column=1)

# --------------------------Fish ----------------------
labelFish = Label(f1,font=('arial',16,'bold'),text="Fish", bd=16, anchor="w")
labelFish.grid(row=3,column=0)
textFish = Entry(f1,font=('arial',16,'bold'),textvariable=Fish, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textFish.grid(row=3,column=1)

# --------------------------Cheese ----------------------
labelCheese = Label(f1,font=('arial',16,'bold'),text="Cheese", bd=16, anchor="w")
labelCheese.grid(row=4,column=0)
textCheese = Entry(f1,font=('arial',16,'bold'),textvariable=Cheese, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textCheese.grid(row=4,column=1)

# --------------------------Chicken ----------------------
labelChicken = Label(f1,font=('arial',16,'bold'),text="Chicken", bd=16, anchor="w")
labelChicken.grid(row=5,column=0)
textChicken = Entry(f1,font=('arial',16,'bold'),textvariable=Chicken, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textChicken.grid(row=5,column=1)

#=====================================Restaurant Management meal info ====================================================

# --------------------------Drinks ----------------------
labelDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks", bd=16, anchor="w")
labelDrinks.grid(row=0,column=2)
textDrinks = Entry(f1,font=('arial',16,'bold'),textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textDrinks.grid(row=0,column=3)

# --------------------------Tax ----------------------
labelTax = Label(f1,font=('arial',16,'bold'),text="Tax", bd=16, anchor="w")
labelTax.grid(row=1,column=2)
textTax = Entry(f1,font=('arial',16,'bold'),textvariable=Tax, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textTax.grid(row=1,column=3)

# --------------------------Price ----------------------
labelPrice = Label(f1,font=('arial',16,'bold'),text="Meal Price", bd=16, anchor="w")
labelPrice.grid(row=2,column=2)
textPrice = Entry(f1,font=('arial',16,'bold'),textvariable=Price, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textPrice.grid(row=2,column=3)

# --------------------------Service ----------------------
labelService = Label(f1,font=('arial',16,'bold'),text="Service Charge", bd=16, anchor="w")
labelService.grid(row=3,column=2)
textService = Entry(f1,font=('arial',16,'bold'),textvariable=Service, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textService.grid(row=3,column=3)

# --------------------------SubTotal ----------------------
labelSubTotal = Label(f1,font=('arial',16,'bold'),text="Sub Total", bd=16, anchor="w")
labelSubTotal.grid(row=4,column=2)
textSubTotal = Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textSubTotal.grid(row=4,column=3)

# --------------------------Total ----------------------
labelTotal = Label(f1,font=('arial',16,'bold'),text="Total", bd=16, anchor="w")
labelTotal.grid(row=5,column=2)
textTotal = Entry(f1,font=('arial',16,'bold'),textvariable=Total, bd=10, insertwidth=4, bg="powder blue", justify = "right")
textTotal.grid(row=5,column=3)
#=========================buttons ==================================
btnTotal =Button(f1,padx=16, pady=8, bd=16, fg="black",font=('arial',20,'bold'),text="Total", width=10, bg="powder blue",command=btnTotal).grid(row=7,column=1)
btnReset =Button(f1,padx=16, pady=8, bd=16, fg="black",font=('arial',20,'bold'),text="Reset", width=10, bg="powder blue",command=btnReset).grid(row=7,column=2)
btnExit =Button(f1,padx=16, pady=8, bd=16, fg="black",font=('arial',20,'bold'),text="Exit", width=10, bg="powder blue",command=btnExit).grid(row=7,column=3)

root.mainloop()