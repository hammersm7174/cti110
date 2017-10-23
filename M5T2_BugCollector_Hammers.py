# CTI-110
# M5T2 - Bug Collector
# Mark Hammers
# 22 Oct 2017
#

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total = total + bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')

