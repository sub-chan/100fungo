#cording utf-8

def n_gram(sentence, n):
    result = []

    for i in range(len(sentence)):
        if i + n > len(sentence):
            return result
        result.append(sentence[i: i + n])

x = "paraparaparadise"
y = "paragraph"

s_x = set(n_gram(x, 2))
s_y = set(n_gram(y, 2))

print(s_x)
print(s_y)
print("\n")

s_union = s_x | s_y
print(s_union)

print("\n")

s_inter = s_x & s_y
print(s_inter)

print("\n")

s_diff = s_x - s_y
print(s_diff)
