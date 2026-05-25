
def input_num():
    num = []
    while True:
        s = input("请输入一个数 (输入 Q 退出): ")
        if s.lower() == 'q':
            break
        try:
            nums = float(s)
            num.append(nums)
        except ValueError:
            print("输入无效，请输入数字或 Q。")
    return num

def sum_num(lst):
    return sum(lst)

number = input_num()
total = sum_num(number)

print("输入的列表:", number)
print("总和:", total)