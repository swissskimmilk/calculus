# TODO: check that n is even

from math import * 

A = input("Lower bound (a): ")
A = eval(A)
B = input("Upper bound (b): ")
B = eval(B)
N = float(input("Subintervals (n): "))
equation  = input("Enter equation: ")

stepSize = (B-A)/N

i = A 
heights = []
xValues = []

# Calculate the height at all needed points and store them in heights
while A <= i <= B:
    heights.append(eval(equation, None, {'x':i}))
    xValues.append(i)
    i += stepSize

# Multiply the middle heights by 4 and 2
for i in range(1, len(heights) - 1):
    if i % 2 == 1:
        heights[i] = heights[i] * 4
    else:
        heights[i] = heights[i] * 2
                   
# Multiply everything in heights by the multiplier 
multiplier = (B - A) / (3 * N)
sum = 0
for height in heights: 
    sum += height * multiplier 

# Print out the values being multiplied 
print(f"Math: {round(multiplier, 2)}[{heights[0]}", end="")
for i in range(1, len(heights)): 
    print(f" + {round(heights[i], 2)}", end="")
print("]")

# Print out the x values 
print(f"X values: [{xValues[0]}", end="")
for i in range(1, len(xValues)):
    print(f", {xValues[i]}", end="")
print("]")

# Print total sum 
print(f"Total sum: {round(sum, 4)}")