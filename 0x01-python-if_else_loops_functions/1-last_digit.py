#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = number % 10

print("Last digit of", end = " ")
print("is", end = " ")
print(k, end=" ")

if k > 5:
    print("and is greater than 5")
elif k == 0:
    print("and is zero")
elif k < 6 and not 0:
    print("and is less than 6 and not 0")
    
