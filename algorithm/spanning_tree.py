from typing import Tuple, List
import sys
import heapq
sys.setrecursionlimit(10**4)

def find(parents: List[int], x: int) -> int:
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents, parents[x])
        return parents[x]

def union(parents: List[int], a: int, b: int) -> List[int]:
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return parents

def compare_parents(parents: List[int], a: int, b: int) -> bool:
    a_parent = find(parents, a)
    b_parent = find(parents, b)
    return a_parent == b_parent

def minimum_span_tree(V: int, E: int) -> int:
    graph = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        heapq.heappush(graph, (c, (a, b)))

    parents = [i for i in range(V+1)]
    result = 0

    while graph:
        weight, nodes = heapq.heappop(graph)
        
        if not compare_parents(parents, nodes[0], nodes[1]):
            parents = union(parents, nodes[0], nodes[1])
            result += weight

    return result


if __name__ == "__main__":
    V, E = map(int, input().split())
    print(minimum_span_tree(V, E))