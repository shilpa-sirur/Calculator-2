"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

token = ('none')


while token[0] != 'q':
  input = raw_input("Enter your string:")
  token = input.split(" ")
  
  if token[0] == 'q':
    break
    
  num1 = int(token[1])
  num2 = int(token[2])
  num2expo = float(token[2])

  if token[0] == '+':
    print(add(num1, num2))
    
  elif token[0] =="-":
    print(subtract(num1,num2))

  elif token[0] =="*" : 
    print(mutiply(num1,num2))

  elif token[0] == "/":
    print(divide(num1,num2)) 

  elif token[0] =="square": 
    print(square(num1)) 

  elif token[0] =="cube" :
    print(cube(num1))

  elif token[0] =="pow":
    print(power(num1,num2))

  elif token[0] =="mod":
    print(mod(num1,num2))
    
  elif token[0] =="expo":
    print(expo(float(num1),num2expo))