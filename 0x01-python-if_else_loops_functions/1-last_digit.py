#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = abs(number) % 10
k *= -1 if number < 0 else 1

print("Last digit of", number, "is", k, end=" ")

if k > 5:
    print("and is greater than 5")
elif k == 0:
    print("and is 0")
elif k < 6 and not 0:
    print("and is less than 6 and not 0")
