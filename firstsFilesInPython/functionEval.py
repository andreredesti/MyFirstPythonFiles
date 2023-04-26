from math import *

"""def secret_function():
  return "Secret key is 1234"

def function_creator():
  expr = input("Enter the function(in terms of x):")

  x = int(input("Enter the value of x:"))

  y = eval(expr)

  print("y = {}".format(y))

if __name__ == "__main__":
  function_creator()
"""
####################################
def secret_function():
  return "Secret key is 1234"

def function_creator():
  expr = input("Enter the function(in terms of x):")

  x = int(input("Enter the value of x:"))


  safe_dict['x'] = x

  y = eval(expr, {"__builtins__":None}, safe_dict)
  print("y = {}".format(y))

if __name__ == "__main__":

  safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 
'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh'] 

safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])

function_creator()
