import math
xie=float(input("请输入三角形斜边"))
zhi=float(input("请输入三角形的直角边"))

if xie<=zhi:
    print("斜边必须大于直角边")
else:
    zhi1=math.sqrt(xie**2-zhi**2)
    sum=xie+zhi+zhi1
    area=xie*zhi/2
    print(f"另一条直角边为{zhi1}")
    print(f"三角形周长为{sum}")
    print(f"三角形面积为{area}")