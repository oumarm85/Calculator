#Calculator
import art

#Add
"""add two numbers together"""
def add(n1, n2):
  return n1 + n2

#Subtract
"""subtract one number from the other"""
def subtract(n1, n2):
  return n1 - n2

#Multiply
"""Multiply two numbers together"""
def multiply(n1, n2):
  return n1 * n2

#Divide
"""Divide one from the other"""
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,

}

def calculator():
  print(art.logo)

  calculating = True
  num1 = float(input("What's the first number?: "))
  for operator in operations:
    print(operator)

  while calculating == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    operation_function = operations[operation_symbol]
    answer = operation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start afresh: ").lower()

    if continue_cal == "n":
      calculating = False
      calculator()
    elif continue_cal == "y":
      num1 = answer

calculator()
