import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build adjacency list where g[u] contains (cost, v) for all outgoing edges from u
        g = defaultdict(list)
        for u, v, cost in times:
            g[u].append((cost, v))

        # Step 2: Min-heap to always process the node with the smallest known distance
        # (current_time, node)
        min_heap = [(0, k)]

        # Step 3: Track visited nodes to avoid processing a node more than once
        visited = set()

        # Step 4: Initialize distance to all nodes as infinity, except starting node k
        distance = {i: float('inf') for i in range(1, n + 1)}
        distance[k] = 0

        # Step 5: Dijkstra's algorithm loop
        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)

            # Skip if already visited
            if u in visited:
                continue

            # Mark node as visited
            visited.add(u)

            # Early exit: all nodes visited
            if len(visited) == n:
                return curr_dist  # Maximum time taken to reach any node

            # Step 6: Traverse all neighbors of u
            for direct_dist, v in g[u]:
                # Relax the edge if a shorter path is found and v is not visited
                if curr_dist + direct_dist < distance[v] and v not in visited:
                    distance[v] = curr_dist + direct_dist
                    heapq.heappush(min_heap, (distance[v], v))

        # Step 7: If not all nodes are reachable, return -1
        return -1
