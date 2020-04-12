print("This is Zach Hill's Assignment 4.1 script")
userInputCompany = input('Enter your company name: ')
userInputFeet = input('Enter number of feet for installation: ')

def costFunction(numberOfFeet):
	costOfCable = 0.87
	if numberOfFeet > 100:
		costOfCable = 0.80
		if numberOfFeet > 250:
			costOfCable = 0.70
			if numberOfFeet > 500:
				costOfCable = 0.50
	totalCost = (userInputCompany + "'s cost of installation for " + str(numberOfFeet) + ' feet of optical cable is: $' + f'{(costOfCable * numberOfFeet):.2f}')
	print(totalCost)

def requestInput(receivedInputFeet):
	try:
		userInputFeet = float(receivedInputFeet)
		# print(userInputFeet)
		costFunction(userInputFeet);
	except:
		print(receivedInputFeet + ' is not a number. Please enter a number')
		userInputFeet = input('Enter number of feet for installation: ')
		# print(userInputFeet)
		requestInput(userInputFeet);

requestInput(userInputFeet);
