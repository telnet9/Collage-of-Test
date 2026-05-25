s=input("请输入一个字符串：")
l=input("请输入一个字符：")
flag=0
for char in s:
    if char==l:
        flag=flag+1
print("{}在{}出现的次数是{}：".format(l,s,flag))