length = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))
sorted_dict = dict()
result = list()

for i, v in enumerate(sorted_arr):
    sorted_dict[v] = i

for i in arr:
    result.append(sorted_dict[i])
print(" ".join(map(str, result)))