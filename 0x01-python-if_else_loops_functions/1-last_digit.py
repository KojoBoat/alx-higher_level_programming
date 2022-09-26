#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
output = f"Last digit of {number} is"
last = number % 10
if last < 6 and last != 0:
    print(output + last + " and is less than 6 and not 0")
elif last > 5:
    print(output + last + " and is greater than 5")
elif last == 0:
    print(output + last + " and is 0")
