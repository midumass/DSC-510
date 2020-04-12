# DSC510-T301 Assignment 6.1
# Zachary Hill
# 20JAN2019
# This program calculates simple arithmetic equations based on user input or totals and averages numbers in a 
# user defined set.  

import math

# Takes input argument and validates that its an operator
def validateOperatorInput(userOperatorInput):
	if userOperatorInput in ['+', '-', '*', '/']:
		return userOperatorInput
	else:
		return validateOperatorInput(input(userOperatorInput + ' is not valid. Please enter a valid operator (+,-,*,/): '))

# Takes input argument and validates that its a number
def validateNumberInput(userNumberInput):
	try:
		float(userNumberInput)
		return float(userNumberInput)
	except:
		return validateNumberInput(input(userNumberInput + ' is not a valid number. Please enter a number: '))

# On call with validated input operator argument, prompts user for 2 numbers and performs calculations
# based on the operator input. If dividing by zero, re-requests valid input.
def performCalculation(operatorParameter):
	inputNumberOne = validateNumberInput(input('Please enter the first value for your equation: '))
	inputNumberTwo = validateNumberInput(input('Please enter the second value for your equation: '))
	if (operatorParameter=='/' and inputNumberTwo==0):
		print('Please enter a non-zero denominator')
		performCalculation(validateOperatorInput(operatorParameter))
	else:
		print('Your equation is: ')
		if operatorParameter=='+':
			print(inputNumberOne, operatorParameter, inputNumberTwo, '=', (inputNumberOne + inputNumberTwo))
		elif operatorParameter=='-':
			print(inputNumberOne, operatorParameter, inputNumberTwo, '=', (inputNumberOne - inputNumberTwo))
		elif operatorParameter=='*':
			print(inputNumberOne, operatorParameter, inputNumberTwo, '=', (inputNumberOne * inputNumberTwo))
		elif operatorParameter=='/':
			print(inputNumberOne, operatorParameter, inputNumberTwo, '=', (inputNumberOne / inputNumberTwo))
		else:
			print("Error encountered while processing. Please contact your system administrator")
	
# Requests user to input how many numbers they want to average and total then displays the two calculations. 
# rounds any non-whole number down. 
def calculateAverage():
	numberOfInputs = math.floor(validateNumberInput(input('How many numbers do you wish to input? ')))
	total = 0
	for i in range(numberOfInputs):
		total += validateNumberInput(input('Please enter a number: ')) 
	print('Your total value of numbers in the range is: ', total)
	print('Your average value of numbers in the range is: ', (total/numberOfInputs))

# Main section of program. Asks user to decide which type of calculation they wish to use and repeats that process 
# until user exits.
print('Enter 1 for arithmetic calculations')
print('Enter 2 for totaling and averaging values in a set')
print('Enter anything else to exit')
functionInput = input('Please chose which calculation you wish to use: ')
while functionInput=='1' or functionInput=='2':
	if functionInput=='1':
		performCalculation(validateOperatorInput(input('Please enter the algebraic operator you wish to use for this calculation (+,-,*,/): ')))
	elif functionInput=='2':
		calculateAverage()
	functionContinue = input('Press [Enter] to continue or any key to exit: ')
	if functionContinue.lower()!='':
		break	
