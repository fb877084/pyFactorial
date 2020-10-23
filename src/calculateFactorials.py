import sys

parameter = sys.argv[1]
print ("You have input:", parameter)

#Check if user input is number or invalid value
try:
    intValue = int(parameter)
except ValueError:
    print("Please input digit number only.")
    sys.exit(0)
#Check if user input a valid number
if int(parameter) < 0:
    print ("Please input digit number equal or greater than 0 only.")
    sys.exit(0)
# define factorial ending case
intValue = int(parameter)
if intValue == 0 or intValue == 1:
    print ("Answer: 1")
else:
    result = intValue
    while intValue > 1:
        result = result * (intValue - 1)
        intValue = intValue - 1
    print ("Answer: ", result)