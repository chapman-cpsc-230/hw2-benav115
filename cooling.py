"""
File: <cooling.py>

Copyright (c) 2016 <Rachel Benavente>

License: MIT

"""

t = 0
T_tea = 100.0
L = 20

while t <= L:
    T_tea -= 0.055*(T_tea-L)
    t += 1
print "%d, %f" % (t,T_tea)
