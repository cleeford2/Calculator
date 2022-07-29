#Calculator
from art import logo
print(logo)

#ADD
def add(n1, n2):
  """Takes two numbers and return the sum"""
  return n1 + n2

#Substract 
def substract(n1, n2):
  """Takes two numbers and return the difference"""
  return n1 - n2

#Multiply
def multiply(n1, n2):
  """Takes two numbers and return the product"""
  return n1 * n2

#Divide
def divide(n1, n2):
  """Takes two numbers and return the remainder"""
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("What is the first number?: "))
  
  #Print operation Sysmbols
  for symbol in operations:
    print(symbol)
  
  continue_calculate = True
  
  operation_symbol = input("Pick an operation symbol from above: ")
  num2 = int(input("What is the next number?: "))
  
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  while continue_calculate:
    
    old_answer = answer
    
    continue_calc = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation.: ")
    
    if continue_calc == 'n':
      continue_calculate = False
      calculator()
    else:
      operation_symbol = input("Pick an operation symbol: ")
      new_num = float(input("What is the next number?: "))
  
      calculation_function = operations[operation_symbol]
      answer = calculation_function(answer, new_num)
  
      print(f"{old_answer} {operation_symbol} {num2} = {answer}")

calculator()