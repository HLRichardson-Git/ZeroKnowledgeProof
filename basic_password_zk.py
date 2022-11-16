# By Hunter Richardson

import random
import math

r = random.randrange(0, 500)

x = input('Enter your x: ')
x = int(x)
g = 3
p = 5

c = (g**r) % p
print('C is: ' + str(c))

w = (x + r) % (p - 1)

print('W is: ' + str(w))

y =(g**x)%p

test = (y*c)%p
test2 = (g**w)%p

if test == test2:
    print('wow')
else:
    print('fuck math')
