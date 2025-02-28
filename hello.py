import numpy as np

from icepool import d

d6 = d(6)
# print(3 @ d6)

print(3 @ d6.reroll([6], depth=1))