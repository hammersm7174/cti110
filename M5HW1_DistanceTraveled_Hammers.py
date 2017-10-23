# CTI-110
# M5HW1 - Distance Traveled
# Mark Hammers
# 22 Oct 2017
#

speed = float(input("What is the speed of the vehicle?"))
time = int(input("How many hours has it traveled?"))

print("\nHour","\tDistance Traveled")
for hour in range(1, time + 1):
    distance = speed * hour
    print(hour,"\t",int(distance))
