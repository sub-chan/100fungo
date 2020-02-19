#cording utf-8

def n_gram(word, n):
    result = []
    for i in range(len(word)):
        if i + n > len(word):
            return result
        result.append(word[i: i + n])

def word_n_gram(sentence, n):
    words = sentence.split()
    result = []

    for i, c in enumerate(words):
        if i + n > len(words):
            return result
        result.append(words[i: i + n])

target = u"I am an NLPer"

result1 = n_gram(target, 2)
result2 = word_n_gram(target, 2)

print(result1)
print(result2)

