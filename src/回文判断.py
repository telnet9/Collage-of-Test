s=input("请输入一个字符串：")
r_s=s[::-1]
if s==r_s:
    print("{}是回文数".format(s))
else:
    print("{}不是回文数".format(s))