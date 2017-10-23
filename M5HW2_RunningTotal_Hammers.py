# CTI-110
# M5HW1 - Distance Traveled
# Mark Hammers
# 22 Oct 2017
#

def main():
    sum = 0
    number = float(input("Enter a number?"))
    while number > -1:
        sum = sum + number
        number = float(input("Enter a number?"))

    print("Total:", int(sum))

main()
