# BMI calculator
# 02 July 2017
# CTI-110 M3HW1 - Age Classifier
# Mark Hammers
#

# User inputs weight
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

# Calculate BMI
bmi = 703/(height**2) * weight

# Determine if you are optimal weight, underweight, or overweight.
if bmi < 25: 
    print('You are optimal weight.')
elif bmi < 18.5:
    print('You are underweight.')
else:
    print('You are overweight.')
    
