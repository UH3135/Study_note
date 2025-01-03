def get_next(oper: int, val: int, cnt: int):
    if oper != 2:
        return (cnt+1, val+oper)
    else:
        return (cnt, val*oper)


def bfs(start: int, goal: int):
    from collections import deque
    q = deque([(0, start)])
    visit = set([start])
    move = [-1, 1, 2]
    
    while q:
        cnt, curr = q.popleft()
        
        for oper in move:
            next_cnt, next = get_next(oper, curr, cnt)
            
            if next not in visit:
                q.append((next_cnt, next))
                visit.add(next)
            
            if next == goal:
                return next_cnt           



if __name__ == "__main__":
    n, k = map(int, input().split())
    print(bfs(n, k))