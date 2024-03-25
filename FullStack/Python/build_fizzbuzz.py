"""
Write a program that prints the numbers from 1 to 100. But for
multiples of three print "Fizz" instead of number and for the multiples
of five print "Buzz". For numbers which are multiiples of both three
and five print "FizzBuzz".
"""

import math

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)