#cording utf-8
import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list1 = str.split()

for i in range(len(list1)):
    length = len(list1[i])
    print(length)
