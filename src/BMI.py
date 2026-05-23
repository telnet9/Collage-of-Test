shengao=float(input("请输入以米为单位的身高"))
weight=float(input("请输入以千克为单位的体重"))
BMI=weight/(shengao**2)
if BMI<18.5:
    print("体重过低")
elif 24>BMI>=18.5:
    print("正常")
elif 28>BMI>=24:
    print("超重")
else :
    print("肥胖")
