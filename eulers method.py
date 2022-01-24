from math import *

def eulersmethod():
  n = int(input("Enter number of steps (n): "))
  stepSize = float(input("Enter step size (h): "))
  initY = float(input("Enter initial y value (y(0)): "))
  equation = input("Enter equation: ")
  
  currN = 0
  currX = 0
  currY = initY
  currYPrime = eval(equation, None, {'x':currX, 'y':currY})
  
  output = [{"n": currN, "x": round(float(currX), 3), "y": round(float(currY), 3), "y'": round(float(currYPrime), 3)}]
  
  for i in range(1, n + 1):
    currN += 1
    currX += stepSize
    currY += stepSize * currYPrime
    currYPrime = eval(equation, None, {'x':currX, 'y':currY})
    output.append({"n": currN, "x": round(float(currX), 3), "y": round(float(currY), 3), "y'": round(float(currYPrime), 3)})
  
  print("{:<4} {:<6} {:<6} {:<6}".format("n", "x", "y", "y'"))
  for entry in output:
    print("{:<4} {:<6} {:<6} {:<6}".format("{:0>2}".format(entry['n']), ("{:.3f}".format(entry['x'])), ("{:.3f}".format(entry['y'])), ("{:.3f}".format(entry["y'"]))))

eulersmethod()
