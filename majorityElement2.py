# O(n) time / O(n) space
def majorityElement(nums):
    freq, res = {}, []
    
    for num in nums:
        freq[num] = 1 + freq.get(num, 0) 
        
    for key in freq:
        if freq[key] > len(nums) // 3:
            res.append(key)
    return res

# O(n) time / O(1) space
def majorityElement(nums):
    num1 = num2 = -1
    count1 = count2 = 0
    
    for num in nums:
        if num1 == num:
            count1 += 1
        elif num2 == num:
            count2 += 1
        elif count1 == 0:
            num1 = num
            count1 = 1
        elif count2 == 0:
            num2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    count1 = count2 = 0
    res = []
    
    for num in nums:
        if num1 == num:
            count1 += 1
        elif num2 == num:
            count2 += 1
            
    if count1 > len(nums) // 3:
        res.append(num1)
    if count2 > len(nums) // 3:
        res.append(num2)
    return res