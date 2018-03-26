# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:05:00 2017

@author: tanw
"""

#Practice Problems

# Problem 1
def convert_to_km(miles):
    km=1.6*miles
    return km

assert(convert_to_km(0) == 0)
assert(convert_to_km(1) == 1.6)
assert(convert_to_km(2) == 3.2)
assert(convert_to_km(1.25) == 2.0)

#Problem 4
def fib_value(numb):
    '''returns the nth numb in fibonaci sequence'''
    if numb <= 0 or isinstance(numb, float) : return 0
    if numb == 1 : return 1
    if numb == 2 : return 1
    return (fib_value(numb - 2) + fib_value(numb - 1))

assert(fib_value(1) == 1)
assert(fib_value(5) == 5)
assert(fib_value(6) == 8)
assert(fib_value(7) == 13)

#Problem 8
def is_palindrome(word):
    reverseword=word[::-1]
    print reverseword
    if reverseword==word:

        return True
    else:
        return False
    
assert(is_palindrome('radar') is True)
assert(is_palindrome('civic') is True)
assert(is_palindrome('honda') is False)
print is_palindrome('kenneth')

#Problem 6
def find_max(seq):
    return max (seq[-1],max(seq[0:-1]))
    
assert(find_max([1,3,2]) == 3)
