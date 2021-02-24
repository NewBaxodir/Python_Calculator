# www.itfuture.fun
# Python Calculator +, -, *, /, %, **, //

def addition(a,b):
	r = (a + b)
	print(r)
	
def subtraction(a,b):
	r = (a - b)
	print(r)

def multiplication(a,b):
	r = (a * b)
	print(r)

def division(a,b):
	r = (a / b)
	print(r)

def modulus(a,b):
	r = (a % b)
	print(r)

def exponentiation(a,b):
	r = (a ** b)
	print(r)

def floor_division(a,b):
	r = (a // b)
	print(r)

a = float(input("Enter number = "))
operation = str(input("Enter op = "))
b = float(input("Enter number = "))


if operation == "+":
	addition(a,b)
elif operation == "-":
	subtraction(a,b)
elif operation == "*":
	multiplication(a,b)
elif operation == "/":
	division(a,b)
elif operation == "%":
	modulus(a,b)
elif operation == "**":
	exponentiation(a,b)
elif operation == "//":
	floor_division(a,b)
else:
	print("Invalid operation")



