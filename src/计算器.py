num1=float(input("请输入第一个数"))
num2=float(input("请输入第二个数"))

sum=num1+num2
diff=num1-num2
prod=num1*num2

if num2!=0:
    chu=num1/num2
    print(f"两个数的和为{sum}")
    print(f"两个数的差为{diff}")
    print(f"两个数的积为{prod}")
    print(f"两个数的商为{chu}")
else:
    print(f"两个数的和为{sum}")
    print(f"两个数的差为{diff}")
    print(f"两个数的积为{prod}")
    print("错误，除数不能为0")
