# Age classifier
# 02 July 2017
# CTI-110 M3HW1 - Age Classifier
# Mark Hammers
#

# User inputs age
age = int(input('Enter your age: '))

# Determine if you are an infant, child, teenager, or an adult.
if age <= 1:
    print('You are an infant.')
elif age < 13:
    print('You are a child.')
elif age < 20:
    print('You are a teenager.')
else:
    print('You are an adult')
    
