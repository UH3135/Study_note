n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i, v in enumerate(arr):
    if i+1 != v:
        answer += 1
print(answer)
           