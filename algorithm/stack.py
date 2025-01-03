from typing import List


def solution(n: int, len_list: List[int]):
    from collections import deque

    stack = deque([])

    for curr in len_list:
        if not stack:
            stack.append(curr)
        else:
            while stack:
                over = stack.pop()
                if over > curr:
                    stack.append(over)
                    stack.append(curr)
                    break
            if not stack:
                stack.append(curr)
    return len(stack)

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(solution(n, arr))               