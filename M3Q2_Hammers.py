# Question M3Q2_A-M
# Mark Hammers
# 15 Oct 2017
#

def main():
    # This program tells the state of matter for Fahrenheit

    degree = float(input('Enter the temperature of the sample of water in Fahrenheit: '))

    if degree < 32:
        print('The state of matter is solid.')
    else:
        if degree > 32 and degree < 213:
            print('The state of matter is liquid.')
        else:
            print('The state of matter is gas.')
# program start
main()
