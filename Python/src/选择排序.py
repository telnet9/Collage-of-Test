import os
import sys
user_input = input("请输入一些数字，用空格分隔：")
arr = [int(x) for x in user_input.split()]
print(arr)