def merge(Intervals):
    # sort intervals by 1st index
    Intervals.sort(key = lambda x:x[0])
    mergedInterval = [Intervals[0]] # add initial interval
    
    for start, end in Intervals[1:]:
        lastEndInterval = mergedInterval[-1][1] #get end interval
        
        if start <= lastEndInterval:
            mergedInterval[-1][1] = max(end, lastEndInterval)
        else:
            mergedInterval.append([start, end])
        
    return mergedInterval