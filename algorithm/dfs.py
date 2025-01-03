from collections import deque
from typing import Dict


def solution(n: int, graph: Dict[int, Dict[int, int]]):
    def dfs(start):
        from collections import deque
        width = 0
        
        stack = deque([(start, 0)]) 
        visit = set([start])

        while stack:
            curr, wei = stack.pop()
            if wei > width:
                width = wei
                node = curr

            for nx, nx_wei in graph[curr].items():
                if nx not in visit:
                    stack.append((nx, nx_wei+wei))
                    visit.add(nx)
        return (node, width)
    
    node, _ = dfs(1)
    _, result = dfs(node)

    return result


if __name__ == "__main__":
    n = int(input())
    graph = {k: {} for k in range(1, n+1)}

    for _ in range(n):
        tmp = list(map(int, input().split()))
        start = tmp[0]
        i = 1
        while True:
            node = tmp[i]
            if node == -1:
                break
            graph[start][node] = tmp[i+1]
            i += 2
    print(solution(n, graph))