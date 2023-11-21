import math
x = 0.067
y = 3.017

sum = 137*(math.pow(x, 3)) + math.cos(math.pow(y, 3) / math.pow(x, 4)) + math.tan(14 * y) - 7 *math.pow(x, 6)
print(sum)