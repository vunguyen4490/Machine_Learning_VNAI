""""Ex1: Write a program to count positive and negative numbers in a list 
         data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
"""
import math
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

pos = 0
neg = 0

for x in data1:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
print("Positive: ", pos)
print("Negative: ", neg)