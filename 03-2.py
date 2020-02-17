#cording utf-8
import re

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = re.split(r"[,. ]",sentence)
words = list(filter(lambda w: w != "", words))

word_len = list(map(len, words))

print(word_len)
