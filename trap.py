from  math import * 

A = input("Lower bound (a): ")
A = eval(A)
B = float(input("Upper bound (b): "))
B = eval(B)
N = float(input("Sub intervals (n): "))
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

# Multiply the middle heights by 2 
for i in range(1, len(heights) - 1):
    heights[i] = heights[i] * 2

# Multiply everything is heights by the multiplier 
multiplier = (B - A) / (2 * N)
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