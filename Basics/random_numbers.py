#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers

import random

x = 1
equalto = '='

for x in range(6):
    print(str(x) + equalto + str(random.randrange(1,100)))
