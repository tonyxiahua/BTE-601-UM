'''
Global Registers 
'''
n=[]
p=[]
l=[]
L=[]            #item
sub=0           #sub total
tax=0           #tax fee
tips=0          #tips
total=0         #total

'''
Restaurant Object 
'''
class Restaurant(object):
    def __init__ (self,name,menu):
        self.restName  =   name
        self.menu      =   menu
    def __str__(self):
        menuString = " "
        for mi in self.menu.menuItem:
            menuString = menuString + '\t' + mi.name + '\n'
        return self.restName
'''
Menu Object 
'''
class MenuItem(object):
    def __init__(self,categ,name,price):
        self.category =   categ
        self.name     =   name
        self.price    =   price
    def __str__(self):
        return self.categ + '\t' + self.name +'\t' +str(self.price)
    
class Menu(object):
    def __init__(self):
        self.menuItem=[]
        
'''
Order Status Object
'''
class Order(object):
    def __init__(self,rest):
        self.rest= rest.menu
        self.orderItems=[]
        
'''
File IO Object
'''
def readData(filename,restaurants):
    ifile = open(filename,'r')
    restSet = set()
    lines=[]
    temp=[]
    
    for line in ifile:
        temp = line.split(',')
        rest = temp[0] 
        categ = temp[1]
        name = temp[2]
        price = float(temp[3]) 
        restSet.add(rest)
        lines.append([rest,categ,name,price])
        #append as list list for ouput data 
        
    for r in restSet:
        m = Menu()
        for line in lines:
            if(line[0]==r):
                mi = MenuItem(line[1],line[2],line[3])
                m.menuItem.append(mi)
        restObject= Restaurant(r,m)
        restaurants.append(restObject)
        

'''
Interface init
'''
def displayMenu(restaurants):

    print("\tWelcome to UberEats")
    print("\t====================")
    print("\t press (q) to quit        (n)new")
    print()
    for i in range (len(restaurants)):
        print(str(i+1)+ " -  " + restaurants[i].restName)
    print()
    restChoice = eval(input(">>>"))
    if restChoice == 'q':
        return
    if 1 <= restChoice <= len(restaurants):
        displayRestMenu(restaurants[restChoice-1])
    else:
        print("Invalid Choice. Program will exit")
        
'''
Interface after select the restaurant
'''
def displayRestMenu(rest):

    print("\tUberEats")
    print("\t==========???==========")
    print("\t(q)quit        (n)new")
    print('\t' + rest.restName)
    categ=set()
    for mi in rest.menu.menuItem:
        categ.add(mi.category)
    i=0
    for c in categ:
        print(c)
        for mi in rest.menu.menuItem:
            if c == mi.category:
                print(str(i+1),"_",mi.name,mi.category,mi.price)
                p.append(mi.price)
                n.append(mi.category)
                l.append(mi.name)
                i += 1
                
def select(pic):
    global sub,tax,tips,total
    L.append(pic)
    for pick in L:
        sub += float(p[pick-1])
        tax = sub * 0.07
        tips = sub * 0.15
        total = sub + tax + tips
        print()
    print("=========================================================================================")
    print("You current meal has",len(L),"item(s).")
    for pick in L:
        print(pick,"  ",n[pick - 1]," ".ljust(5), l[pick - 1].ljust(30), "$",p[pick - 1])

    print("=========================================================================================")
    print("Subtotal:  $".rjust(81),round(sub,2))
    print("Tax(7%):  $".rjust(81),round(tax,2))
    print("Tips(15%):  $".rjust(81), round(tips,2))
    print("Total:  $".rjust(81),round(total,2))
    print()
    
def main():
    filename='menu.txt'
    restaurants=[]
    readData(filename,restaurants)
    displayMenu(restaurants)
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