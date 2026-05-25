num1=float(input("请输入第一个数"))
num2=float(input("请输入第二个数"))
cal=str(input("请输入要进行的运算"))
if cal=='+':
    print(f"两数之和为{num1+num2}")
elif cal=='-':
    print(f"两数之差为{num1-num2}")
elif cal=='*':
    print(f"两数之积为{num1*num2}")
elif cal=='/':
    print(f"两数之商为{num1/num2}")
