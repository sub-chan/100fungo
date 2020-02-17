#cording utf-8

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
initials = [1, 5, 6, 7, 8, 9, 15, 16, 19]
count = 0

words = sentence.split()

#print(words)

element_symbol={}

for i , word in enumerate(words, 1):
    if i in initials:
        element_symbol[count + 1] = word[0]
    else:
        element_symbol[count + 1] = word[:2]
    count = count + 1

print(element_symbol)
