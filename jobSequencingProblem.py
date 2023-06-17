# O(nlogn) + O(n*m) time / O(m) space
def JobScheduling(Jobs, n):
    Jobs.sort(key=lambda x:x.profit, reverse=True) # sort based on profits
    done = [-1] * (101)
    totalProfit = count = 0

    for i in range(n):
        deadLine = Jobs[i].deadline
        jobId = Jobs[i].id
        profit = Jobs[i].profit
        for j in range(deadLine, 0, -1): # assign in array based on deadline
            if done[j] == -1:
                done[j] = jobId
                totalProfit += profit
                count += 1
                break
    return (count, totalProfit)