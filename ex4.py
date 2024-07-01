import math 

def prime(x):
    for i in x:
        i = int(i)
        if i < 1:
            continue 
        root = int(math.sqrt(i)) + 1
        is_prime = True
        for j in range(2, root):
            if i % j == 0:
                is_prime = False
                break
        if is_prime or i == 2:
            print(i)

ar = list(input().split())
prime(ar)
