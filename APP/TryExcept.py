'''
Exception Handling: When an error occurs, or exception as we call it, 
Python will normally stop and generate an error message. 
These exceptions can be handled using the try statement.
Since the try block raises an error, the except block will be executed.
'''
# try:
#   print(x)
# except:
#   print("An exception occurred")

# a = int(input("enter value to a: ")) 
# b = int(input("enter value to b: "))
# print(a / b)

# try:
#     a = int(input("enter value to a: ")) 
#     b = int(input("enter value to b: "))
#     print(a / b)

# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Result =", a / b)

# except ValueError:
#     print("Please enter valid integer values")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# Multiple exception blocks: to execute a special block of code for a special kind of error
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# handle multiple exceptions together
# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(result)

# except (ValueError, ZeroDivisionError) as error:
#     print("Error:", error)

# else keyword to define a block of code to be executed 
# if no errors were raised
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result =", result)

# try:
#   f = open("students.txt")  
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# raise – Explicitly Raising an Exception
# age = int(input("Enter age: "))
# if age < 0:
#     raise ValueError("Age cannot be negative")
# print("Age =", age)

# raise an exception if marks are not between 0 and 100
# marks = int(input("Enter marks: "))
# if marks < 0 or marks > 100:
#     raise ValueError("Marks must be between 0 and 100")

# assert statement is used to test if a condition is true. 
# If the condition is false, an AssertionError exception is raised.
# age = 20
# assert age >= 18
# print("Eligible")

# def calculate_average(marks):
#     assert len(marks) > 0, "Marks list cannot be empty"
#     return sum(marks) / len(marks)
# marks = [85, 90, 78, 92, 88]
# print("Average marks:", calculate_average(marks))

# user-defined exception
# class InvalidMarksError(Exception):
#     pass
# marks = int(input("Enter marks: "))
# try:
#     if marks < 0 or marks > 100:
#         raise InvalidMarksError("Marks must be between 0 and 100")
#     print("Marks accepted:", marks)
# except InvalidMarksError as error:
#     print("Error:", error)

# keyword finally is used to define a block of code that will be executed regardless of whether an exception was raised or not.
employee = {
    "name": "Anita",
    "salary": 50000
}

try:
    key = input("Enter key to search: ")
    print(key, "=", employee[key])
except KeyError:
    print("Invalid key.")