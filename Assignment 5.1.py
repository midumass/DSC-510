# DSC510-T301 Assignment 5.1
# Zachary Hill
# 13JAN2019
# This program requests and validates user input for an optical cable installation, calculates the cost based on the length 
# of the cable requested and returns the cost to the user.

# Request input from user
print("This is Zach Hill's Assignment 5.1 script")
userInputCompany = input('Enter your company name: ')
userInputFeet = input('Enter number of feet for installation: ')

# Calculate cost per foot based on user input
def priceFunction(numberOfFeet):
	costOfCable = 0.87
	if numberOfFeet > 100:
		costOfCable = 0.80
		if numberOfFeet > 250:
			costOfCable = 0.70
			if numberOfFeet > 500:
				costOfCable = 0.50
	return costOfCable;

# Take calculated cost and multiply by requested number of feet
# Write Company name and calculations to screen
def costFunction(feet,price):
	totalCost = feet * price
	print(userInputCompany + "'s cost of installation for " + str(feet) + ' feet of optical cable is: $' + f'{(totalCost):.2f}');

# Validate requested input. Rerequest if improper literal is entered.
# Complete calculations if successful
def userInput(receivedInputFeet):
	try:
		userInputFeet = float(receivedInputFeet)
		priceCalc = priceFunction(userInputFeet)
		costFunction(userInputFeet,priceCalc)
	except:
		print(receivedInputFeet + ' is not a number. Please enter a number')
		userInputFeet = input('Enter number of feet for installation: ')
		userInput(userInputFeet);
	
userInput(userInputFeet);