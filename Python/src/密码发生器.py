import os
import sys

def f(n):
  while len(str(n)) > 1:
    sum = 0
    for i in str(n):
      sum += int(i)
      n = sum
  return n

n = int(input())

for i in range(n):
  sum = [0]*(6)
  s = input()
  for j in range(len(s)):
    sum[j%6] += ord(s[j])
  for j in range(6):
    sum[j] = f(sum[j])
  for j in range(6):
    print(sum[j],end='')
  print()