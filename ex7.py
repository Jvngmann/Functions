
def is_33_7 (x):
    n = 1
    for i in x:
        if i == n and i == 3:
            return True
        n = i
    return False 

# def so(x):

#     for i in range(len(x) - 1):
#         if x[i] == 3 and x[i + 1] == 3:
#             return True
#     return False

l1 = [1, 32, 3, 4, 5, 6, 7, 8] 
print(is_33_7(l1))

