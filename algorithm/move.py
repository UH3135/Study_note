END = 10**5

def solution(n, k):
    if k <= n:
        return n-k

    import heapq

    q = []
    visit = [float("Inf") for _ in range(END+1)]
    visit[n] = 0
    heapq.heappush(q, (0, n))

    while q:
        cnt, x = heapq.heappop(q)

        for nx in [x*2, x+1, x-1]:
            if 0 >= nx or nx > END:
                continue
            if nx == x*2 and cnt <= visit[nx]:
                visit[nx] = cnt
                heapq.heappush(q, (cnt, nx))
            elif nx != x*2 and cnt+1 < visit[nx]:
                visit[nx] = cnt+1
                heapq.heappush(q, (cnt+1, nx))
    return visit[k]
                

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(n, k))