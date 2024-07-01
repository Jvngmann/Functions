def SG(nums):
    a = [0, 0, 7]
    index = 0
    
    for num in nums:
        if num == a[index]:
            index += 1
        if index == len(a):
            return True            
    return False

print(SG([1,2,4,0,0,7,5]))
print(SG([1,0,2,4,0,5,7]))
print(SG([1,7,2,0,4,5,0])) 
