list=[1,23,45,-2,99,35]
list.sort()
print("最小值为{}".format(list[0]))
len1=len(list)
print("最大值为{}".format(list[len1-1]))
sum=0
for i in list:
    sum+=i
avg=sum/len1
print("平均值为{}".format(avg))