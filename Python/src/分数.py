score=int(input("请输入你的分数："))
if 90 <= score:
    print("你的等级为A")
elif 80 <= score<90:
    print("你的等级为B")
elif 70 <= score<80:
    print("你的等级为C")
elif 60<= score <70:
    print("你的等级为D")
else:
    print("你的等级为E")