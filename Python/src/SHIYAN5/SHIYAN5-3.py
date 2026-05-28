list=[1,23,45,-2,99,35]
MAX_V=list[0]
MIN_V=list[0]
total=0
for num in list:
    if num > MAX_V:
        MAX_V=num
    if num < MIN_V:
        MIN_V=num
    total+=num

avg=total/len(list)
print("最小值为{}".format(MIN_V))
print("最大值为{}".format(MAX_V))
print("平均值为{}".format(total))
