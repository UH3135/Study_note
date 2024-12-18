import heapq

def add_process(jobs, queue, time, complete):
    for i, li in enumerate(jobs):
        if li[0] <= time and i not in complete:
            heapq.heappush(queue, (li[1], li[0], i))
    return queue
            
def solution(jobs):
    count = len(jobs)
    result = []
    time = 0
    queue = []
    complete = set()
    
    while len(complete) != count:
        queue = add_process(jobs, queue, time, complete)
        if queue:
            burst, request, num = heapq.heappop(queue)
            time += burst
            result.append(time-request)
            complete.add(num)
        else:
            time += 1
        
    
    return sum(result) // count