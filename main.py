def minTime(processorTime, taskTime):
    # Sort the processor times and task times
    processorTime.sort()
    taskTime.sort(reverse=True)
    
    result = 0
    curTask = 0
    for proctime in processorTime:
        for _ in range(4):
            completionTime = taskTime[curTask] + proctime
            curTask+=1
            result = result if result>completionTime else completionTime
    return result


n = 2
processorTime = [8, 10]
taskTime = [2, 2, 3, 1, 8, 7, 4, 5]

earliest_time = minTime(processorTime, taskTime)
print(f"Earliest time to process all tasks: {earliest_time} units of time")
