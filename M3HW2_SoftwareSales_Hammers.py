# CTI-110
# M3HW2 - Software Sales
# Mark Hammers
# 15 Oct 2017
#


def main():
    #This program is to dicover discounts for bulk packages and provide total.

    
    packages = float(input('Enter the number of packages purchased: '))
    before_discount = packages*99

    if(packages<9):
        discount = before_discount*0
        total = before_discount - discount
        print("If you buy", int(packages), "package(s), your discount is $", format(discount, ",.2f"), "and your total is $", format(total, ",.2f"), ".") 
    
    elif(packages>9 and packages<20):
        discount = before_discount*.10
        total = before_discount - discount
        print("If you buy", int(packages), "package(s), your discount is $", format(discount, ",.2f"), "and your total is $", format(total, ",.2f"), ".")

    elif(packages<19 and packages<50):
        discount = before_discount*.20
        total = before_discount - discount
        print("If you buy", int(packages), "package(s), your discount is $", format(discount, ",.2f"), "and your total is $", format(total, ",.2f"), ".")

    elif(packages<49 and packages<100):
        discount = before_discount*.30
        total = before_discount - discount
        print("If you buy", int(packages), "package(s), your discount is $", format(discount, ",.2f"), "and your total is $", format(total, ",.2f"), ".")

    elif(packages<99):
        discount = before_discount*.40
        total = before_discount - discount
        print("If you buy", int(packages), "package(s), your discount is $", format(discount, ",.2f"), "and your total is $", format(total, ",.2f"), ".")


main()
