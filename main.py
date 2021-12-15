#!/usr/bin/env python3
#Calculator
from art import logo

def add(n1,n2):
	return n1 + n2

def subtract(n1,n2):
	return n1 - n2

def multiply(n1,n2):
	return n1 * n2

def divide(n1,n2):
	return n1 / n2

operations = {
	'+':add,
	'-':subtract,
	'*':multiply,
	'/':divide
}

def calculator():
	print(logo)
	num1 = float(input("First number: "))
	for symbol in operations:
		print(symbol)
	should_continue = True
	while should_continue:
		operation_symbol = input("Pick an operation: ")
		num2 = float(input("Next number: "))
		answer = operations[operation_symbol](num1,num2)
		print(f'{num1} {operation_symbol} {num2} = {answer}')
		if input(f"type 'y' to continue to continue calculating with {answer} or 'n' to start a new calculation") == 'y':
			num1 = answer
		else:
			should_continue = False
			calculator()

calculator()
	
