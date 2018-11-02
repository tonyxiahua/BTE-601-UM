'''
Write a program that calculates and displays the depreciation in value of a given item. Given the following formulas:

straight-line depreciation = each year the item depreciates by (1/n)th of its original value

double-declinging depreciation = each year the item depreciates by (2/n)ths of its value at the beginning of that year. 

In the final year it is depreciated by its value at the beginning of the year.

Write a program that prompts the user to enter the name of the item, the year it was
purchased, the cost of the item, the estimated life of the item in years, and the method of depreciation. 

Then print out the given information and display the value at the beginning
of the year, the amount the item depreciated during the year, and the total amount of
deprciation up to the current year in a table for each year of the item's estimated lifetime.
'''
def calDepreciation():
    name = input("Please enter the name:\n")
    year = int(input("Please enter the year it was purchased:\n"))
    price = float(input("Please enter the cost of the item:\n"))
    estlife = int(input("Please enter the estimated life of the item in years:\n"))
    method = int(input("Please select the method of depreciation: \n 1. straight-line depreciation\n 2. double-declinging depreciation\n"))
    print("The value at the purchase date:",price)
    if method == 1:
        sld = price*(1/estlife)
        print("The amount the item depreciated during the year",sld)
        for i in range(estlife):
            price -= sld
            print("At the same purchase date of",i+1+year,"year, value is ",price)
        exit()
    elif method == 2:
        for i in range(estlife):
            ddd = price*(2/estlife)
            price -=ddd
            print("At the same purchase date of",i+1+year,"year, value is ",price)
            exit()
    else:
        exit()
'''
Question 7
 Write a program that prompts the user for a word and displays whether or not
 that word contains three succesive letters in consecutive alphabetical order.
 For example, THIRSTY does (RST) and GOODBYE does not. Your program should
 implement a function isTripleConsecutive(word) that returns a Boolean value.
 HINT: Use the ord function.
'''
def isTripleConsecutive(word):
    crusor = 1
    while(crusor<len(word)):
        if len(word) <3 or ord(word[crusor-1])==ord(word[crusor]):
            return False
        if( ord(word[crusor-1]) == (ord(word[crusor])-1) and ord(word[crusor])==(ord(word[crusor+1]))-1):
            return True
        crusor+=1
    return False

'''
Main
'''
def main():
    
    # Question 4
    
    # Question 6
    calDepreciation()
    # Question 7
    word = input("Please enter a word,contains three succesive letters in consecutive alphabetical order.\n")
    print(isTripleConsecutive(word))
    
main()