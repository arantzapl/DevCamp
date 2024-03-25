"""
Write a program that prints the numbers from 1 to 100. But for
multiples of three print "Fizz" instead of number and for the multiples
of five print "Buzz". For numbers which are multiiples of both three
and five print "FizzBuzz".
"""

import math

for num in range(1, 101):
    if(num % 3 == 0):
        print('Fizz\n')
    if(num % 5 == 0):
        print('Buzz\n')
    if(num % 15 == 0):
        print('FizzBuzz\n')
    else:
        print(f'{num}\n')