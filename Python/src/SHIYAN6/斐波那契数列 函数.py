def fib(n):
    list=[]
    a=b=1
    for _ in range (n):
        list.append(a)
        a,b=b,a+b
    return list

n=int(input("请输入一个整数"))
result=fib(n)
print(result)