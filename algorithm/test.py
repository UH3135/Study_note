def main(n, h_list):
    from collections import deque
    stack = []

    for h in h_list:
        if not stack:  # 스택이 비었으면 처음 값 append
            stack.append(h)
            continue
        
        while stack:
            curr = stack.pop()
            if curr > h:
                stack.append(curr)
                break
        stack.append(h)
    return stack 

print(main(7, [6,9,7,6,4,6, 10]))
