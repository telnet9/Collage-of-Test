def is_prime(n):
    if n<2:
        return False
    for i in range (2,n):
        if n % i ==0:
            return False;
    return True;
def count10000():
    prime=[]
    for num in range (1,10001):
        if is_prime(num):
            prime.append(num)
    return prime
list=count10000()
print("1-10000素数的个数是")
print(len(list))

