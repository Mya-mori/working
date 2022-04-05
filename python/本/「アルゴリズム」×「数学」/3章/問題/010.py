import random
import math

N = 10000
#mean = p
#std = sqrt(p(1-p)/n)

mean = math.pi/4
std = math.sqrt(mean*(1-mean)/N)

low = mean - 3*std
high = mean + 3*std

print(mean)
print(std)
print(low, "<= u <= ",high)