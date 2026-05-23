password = input("请输入字符串：")
has_upper = False
has_lower = False
has_digit = False
has_special = False
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True
if has_upper and has_lower and has_digit and has_special:
    print("密码强度：强")
else:
    print("密码强度：弱")
    if not has_upper:
        print("缺少大写字母")
    if not has_lower:
        print("缺少小写字母")
    if not has_digit:
        print("缺少数字")
    if not has_special:
        print("缺少特殊符号")