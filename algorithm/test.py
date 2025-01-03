import heapq

n = int(input())
q = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    heapq.heappush(q,(age, i, name))
for _ in range(n):
    age, _, name = heapq.heappop(q)
    print(age, name)