letter=0
digit=0
space=0
others=0

s=input("请输入一个字符串")

for c in s:
    if c.isalpha():
        letter+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1
    else:
        others+=1

print("字母的个数{}".format(letter))
print("数字的个数{}".format(digit))
print("空格的个数{}".format(space))
print("其他字符的个数{}".format(others))