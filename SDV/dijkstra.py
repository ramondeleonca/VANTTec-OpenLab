from __future__ import annotations

import heapq
import math
from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")

@dataclass
class Node(Generic[T]):
    # value is the first positional arg; path_length starts at infinity
    value: T
    path_length: float = math.inf
    prev: Node | None = field(default=None, repr=False)
    neighbors: list[tuple[Node, int]] = field(default_factory=list, repr=False)

    def __lt__(self, other: Node) -> bool:
        # required by heapq to break ties when path_length is equal
        return self.path_length < other.path_length

    def connect(self, other: Node, weight: int = 1, directed: bool = False) -> None:
        # directed=False: both u→v and v→u; directed=True: only u→v
        self.neighbors.append((other, weight))
        if not directed:
            other.neighbors.append((self, weight))


class Dijkstra:
    nodes: list[Node]

    def __init__(self):
        self.nodes = []

    def add_node(self, *nodes: Node) -> None:
        # register nodes so the solver can reset them between runs
        self.nodes.extend(nodes)

    def _reset(self) -> None:
        for node in self.nodes:
            node.path_length = math.inf
            node.prev = None

    def run(self, source: Node) -> None:
        # sets path_length and prev on every reachable node from source
        self._reset()
        source.path_length = 0
        heap: list[tuple[float, Node]] = [(0, source)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > u.path_length:
                continue  # stale heap entry, already found a better path
            for v, w in u.neighbors:
                alt = u.path_length + w
                if alt < v.path_length:
                    v.path_length = alt
                    v.prev = u
                    heapq.heappush(heap, (alt, v))

    def shortest_path(self, source: Node, target: Node) -> list[Node]:
        # reconstructs path from source to target; run() must be called first
        path: list[Node] = []
        current: Node | None = target
        while current is not None:
            path.append(current)
            current = current.prev
        path.reverse()
        if not path or path[0] is not source:
            return []  # no reachable path
        return path