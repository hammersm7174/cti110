# CTI-110
# M5HW3 - Factorial
# Mark Hammers
# 22 Oct 2017
#

def main():
    number = int(input("Enter a nonnegative integer?"))
    factorial = 1
    if number < 0:
        print("Can't do that!")
    elif number == 0:
        print("The factorial of 0 is 1!")
    else:
        for i in range(1,number+1):
            factorial = factorial * i
        print("The factorial of", number, "is", factorial)

main()
