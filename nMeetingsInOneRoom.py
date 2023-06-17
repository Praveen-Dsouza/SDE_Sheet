# O(n) time / O(n) space
def maximumMeetings(n, start, end):
    room, count, endTime = [], 0, 0
    
    # append the first meeting
    for i in range(n):
        room.append([start[i], end[i]])
    # sort based on the end time of meetings
    room = sorted(room, key = lambda x:x[1])
    
    for meeting in room:
        # if startTime > endTime inc count and update meeting endTime
        if meeting[0] > endTime:
            count += 1
            endTime = meeting[1]
    return count