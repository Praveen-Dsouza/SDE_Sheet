# O(nlogn) + O(n) time / O(1) space
def fractionalknapsack(W, Items):
    Items.sort(key=lambda x: x.value/x.weight, reverse=True)
    res = 0
    
    for i in Items:
        if i.weight <= W:
            res += i.value
            W -= i.weight
        else:
            temp = (i.value / i.weight) * W
            res += temp
            W = 0
    
    return res