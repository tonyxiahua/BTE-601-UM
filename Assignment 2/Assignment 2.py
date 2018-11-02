'''
Question 2
Write a program that prompts the user to enter an amount of change (between 0 and
99) and
prints out how many coins of each denomination are needed to make that
change. The program
should always try to make change using the higest denomination
coin possible. ex. 25 should
be 1 quarter rather than 2 dimes and 1 nickel.
'''

'''
coin = [1,5,10,25]
change = int(input("Enter an amount of change (between 0 and 99)\n"))
if change > 99:
    print("Error")
else:    
    quater = change//coin[3] 
    dime = (change-quater*25)//coin[2]
    nickel = (change-quater*25-dime*10)//coin[1]
    penny = (change-quater*25-dime*10-nickel*5)
    print("You need",quater,"quater",dime,"dime",nickel,"nickel",penny,"penny")

'''

'''
Write a program that prompts the user to enter the price and weight of an item in
pounds and ounces. Prompt the user to enter pounds and ounces as seperate
numbers. If the user enters a value larger than 15 for ounces, remind them that there
are 16 ounces in 1 pound, $0.00. HINT: There are 16 ounces in 1 pound. and any values 
greater than 15 should be entered as pounds. 
Then, calculate and display the price per ounce of the item in the format.
'''

'''
price = float(input("Please enter price\n"))
pounds = float(input("Please enter pounds\n"))
ounces = float(input("Please enter ounces\n"))
if ounces > 15:
    print("There are 16 ounces in 1 pound.")
    pounds+=ounces//16
    ounces-=16*pounds 
print("Price per ounce of the item:$",'%.2f'%(price/(ounces+pounds*16)))
'''

'''
Write a program that prompts the user to enter the amount of money invested
in four different stocks: SPY, QQQ, EEM, VXX. Print the name of the stock
and what percentage of the user's total portfolio that stock represents.
Format all percentages to two places after the decimal. Finally, print the
total amount of money invested in stocks.
'''

'''
stocks = ('SPY','QQQ','EEM','VXX')
money = []
percentage = []
for i in range(len(stocks)):
    money.append(float(input("Money in your "+stocks[i]+"\n")))
print("Your stocks total portfolio: \n",stocks[0],'%.2f'%(money[0]/sum(money)*100),"%\n",stocks[1],'%.2f'%(money[1]/sum(money)*100),"%\n",stocks[2],'%.2f'%(money[2]/sum(money)*100),"%\n",stocks[3],'%.2f'%(money[3]/sum(money)*100),"%")
print("Your total money: ",sum(money))
'''

'''
Write a program that prompts the user for a length in miles, yards, feet, and inches
and converts it to the metric system (kilometers, meters, and centimeters). To
accomplish this, first convert everything to inches. Then, convert inches to meters.
Use the int() function to break the total number of meters into a whole number of
kilometers and meters. Format the remaining centimeters to one decimal place.
 Formulas:
 total inches = 63,360 * miles + 36 * yards + 12 * feet + inches
 Submission:
total meters = inches/39.37
 1 kilometer = 1000 meters
 1 meter = 100 centimeters
'''

'''
miles = float(input("Enter miles\n"))
yards = float(input("Enter yards\n"))
feet = float(input("Enter feet\n"))
inches = float(input("Enter inches\n"))

inches = 63360*miles+36*yards+12*feet+inches

meters = inches/39.37
kiloMeters = int(meters/1000)
meter = int(meters%1000)
centimeters = int((meters*100)%100)
print("Equal to: ",kiloMeters,"kiloMeters",meter,"meters",centimeters,"centimeters")
'''

'''
numberOfRows = int(input("Enter a number from 1 through 20:"))
#numberOfRows = 5

for i in range(numberOfRows):
    for j in range(i+1):
        print("*",end="")
    print()
print()

for i in range(numberOfRows):
    for j in range(numberOfRows-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
print()

for i in range(numberOfRows):
    for j in range(numberOfRows-i):
        print("*",end="")
    for k in range(i+1):
        print(" ",end="")
    print()
print()

for i in range(numberOfRows):
    for j in range(i):
        print(" ",end="")
    for k in range(numberOfRows-i):
        print("*",end="")
    print()
print()

for i in range(numberOfRows):
    for j in range(numberOfRows-1-i):
        print(" ", end="")
    for k in range(i*2+1):
        print ("*", end="")   
    print()
for i in range(numberOfRows):
    for j in range(i+1):
        print(" ", end="")      
    for k in range((numberOfRows-i-1)*2-1):
        print ("*", end="")  
    print()
'''

'''
def finalPrice(prices):
    #place your code here
    for elem in prices:
        number = 
def main():
    prices = [5,1,3,4,6,2]
    finalPrice(prices)
    # output should be 
    #[4,1,3,4,6,2]
    #[4,1,3,4,6,2]
'''