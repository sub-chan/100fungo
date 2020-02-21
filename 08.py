#cording utf-8

def cipher(target):
    result = ""
    for c in target:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result

target = input("文字列を入力してください")

result = cipher(target)
print("暗号化:" + result)

result2 = cipher(result)
print("複合:" + result2)

if result2 != target:
    print("元に戻っていない")
