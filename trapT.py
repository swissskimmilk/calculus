from  math import * 

# Turns a csv value into an array without whitespace 
def toArray(csv):
    arr = csv.split(",")
    arr = [int(x.strip(' ')) for x in arr]
    return arr

A = float(input("Lower bound (a): "))
B = float(input("Upper bound (b): "))
N = float(input("Sub intervals (n): "))
yRow = input("Enter y row, separated by commas: ")

yArray = toArray(yRow)

stepSize = (B-A)/N

i = A 

# Multiply the middle values by 2 
for i in range(1, len(yArray) - 1):
    yArray[i] = yArray[i] * 2

# Multiply everything in yArray by the multiplier 
multiplier = (B - A) / (2 * N)
sum = 0
for y in yArray: 
    sum += y * multiplier 

# Print out the values being multiplied 
print(f"Math: {round(multiplier, 2)}[{yArray[0]}", end="")
for i in range(1, len(yArray)): 
    print(f" + {round(yArray[i], 2)}", end="")
print("]")

# Print total sum 
print(f"Total sum: {round(sum, 4)}")