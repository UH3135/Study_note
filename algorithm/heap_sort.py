import sys
input = sys.stdin.readline

nums = [0 for _ in range(10001)]

n = int(input())

for _ in range(n):
    curr = int(input())
    nums[curr] += 1

for index, value in enumerate(nums):
    for _ in range(value):
        print(index)

        