'''
Global Menus 
'''
l= ["Chicken Satay","Epyptian Spring Roll","Humus", "Samboosa",
    "Shish Tawooq - Chicken Kabab","Shish Kabab - Beef Kabab","Fatta Bel Mooza","Koshary - vegetarian","Koshary - woth meat sauce",
    "Tea with mint","Turkish Coffee","Soda",
    "Rice Pudding - with rose water","Basboosa - 2 pieces","Mango Pudding"]

p=["7.50","6.50","5.50","5.50",
   "13.50","16.50","17.25","10.25","12.25",
   "2.25","2.25","2.00",
   "6.00","4.50","6.00"]

n=["Appetizers ","Appetizers ","Appetizers ","Appetizers ",
    "Entrees ","Entrees ","Entrees ","Entrees ","Entrees ",
    "Drinks "," Drinks "," Drinks ",
    "Desserts ","Desserts ","Desserts "]
'''
Global Registers 
'''
L=[]            #item
sub=0           #sub total
tax=0           #tax fee
tips=0          #tips
total=0         #total

'''
Interfaces 
'''
def displaymenu():
    print("\t\tWelcome To  The  Miami  Favorites   Meal   Builder")
    print("\t\t==================================================\n")
    print("\t\tNewMeal (n)                                Quit(q)\n")
    print("                               Appetizers                 \n")
    for i in range(0,4):
        print(i+1," ".ljust(5),l[i].ljust(30),"$".rjust(30),p[i].rjust(0))
    print("\n                                Entrees                 \n")
    for i in range (4,9):
        print(i+1," ".ljust(5),l[i].ljust(30),"$".rjust(30),p[i].rjust(0))
    print("\n\n                                Drinks                \n")
    for i in range(9,12):
        print(i+1, " ".ljust(5), l[i].ljust(30), "$".rjust(30), p[i].rjust(0))
    print("\n                                Desserts                \n")
    for i in range(12,15):
        print(i+1, " ".ljust(5), l[i].ljust(30), "$".rjust(30), p[i].rjust(0))
    print("\n\n")
    
displaymenu()

def select(pic):
    displaymenu()
    global sub,tax,tips,total
    L.append(pic)
    for pick in L:
        sub += float(p[pick  -  1])
        tax = sub * 0.07
        tips = sub * 0.15
        total = sub + tax + tips
        print()
    print("=========================================================================================")
    print("You current meal has",len(L),"item(s).")
    for pick in L:
        print(pick,"  ",n[pick - 1]," ".ljust(5), l[pick - 1].ljust(30), "$".rjust(30),p[pick - 1].rjust(0))

    print("=========================================================================================")
    print("Subtotal:  $".rjust(81),round(sub,2))
    print("Tax(7%):  $".rjust(81),round(tax,2))
    print("Tips(15%):  $".rjust(81), round(tips,2))
    print("Total:  $".rjust(81),round(total,2))
    print()


def main():
    while (True):
        command=input("Please enter item[1 - 15]:")
        global L,sub,tax,tips,total
        if command=="n":
            L=[]
            sub = 0
            tax = 0
            tips = 0
            total = 0
        elif command=="q":
            break
        else:
            pick=eval(command)
            if(pick not in range(1,16)):
                print("error: unknown item id")
            else:
                select(pick)

main()