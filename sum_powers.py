# Sum of Powers
"""
File: <sum_powers.py>

Copyright (c) 2016 <Rachel Benavente>

License: MIT

<This code prompts the user for two numbers and adds one number raised to the
second number.>

"""

user_input = raw_input("Enter a natural number: ")
n = int(user_input)
user_input = raw_input("Enter a floating number: ")
b = float(user_input)

i = 0

while i <= b:
    t = (b**(n+1)-1)/(b-1)
    i += 1

print t
