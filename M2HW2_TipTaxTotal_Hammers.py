# Calculate the tip, tax, and total of a meal.
# 02 July 2017
# CTI-110 M2HW2 - Tip Tax Total
# Mark Hammers
#

# Meal price
meal = float(input('Enter price of meal:'))

# Calculate meal total.
total_ticket = (meal + meal * .18 + meal * .07)

# Display the meal total.
print('Your meal total is $', format(total_ticket, ',.2f'))
