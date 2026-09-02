import calculator
a=float(input("Enter first number:")) 
b=float(input("Enter second number:"))  
print("\nAddition:",calculator.add(a,b))
print("\nSubtraction:",calculator.subtract(a,b))
print("\nMultiplication:",calculator.multiply(a,b))
print("\nDivision:",calculator.divide(a,b))
print("\nPower:",calculator.power(a,b))
print(f"\nSquare Root of {a}:",calculator.square_root(a))