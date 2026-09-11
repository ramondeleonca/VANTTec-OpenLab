from __future__ import annotations

import heapq
import math
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from itertools import count
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(eq=False)
class Node(Generic[T]):
    value: T
    neighbors: list[tuple[Node, int]] = field(default_factory=list, repr=False)

    def connect(self, other: Node, weight: int = 1, directed: bool = False) -> None:
        # directed=False: both u→v and v→u; directed=True: only u→v
        self.neighbors.append((other, weight))
        if not directed:
            other.neighbors.append((self, weight))


@dataclass
class Result:
    source: Node
    dist: dict[Node, float]
    prev: dict[Node, Node | None]
    elapsed: float  # wall-clock seconds

    def dist_to(self, target: Node) -> float:
        # returns shortest distance from source to target, inf if unreachable
        return self.dist.get(target, math.inf)

    def path_to(self, target: Node) -> list[Node]:
        # reconstructs optimal path from source to target; returns [] if unreachable
        path: list[Node] = []
        current: Node | None = target
        while current is not None:
            path.append(current)
            current = self.prev.get(current)
        path.reverse()
        if not path or path[0] is not self.source:
            return []
        return path


class Dijkstra:
    def run(self, source: Node) -> Result:
        # Dijkstra from source; returns Result with dist map, prev pointers, and elapsed time
        dist: dict[Node, float] = {source: 0.0}
        prev: dict[Node, Node | None] = {}
        tiebreak = count()  # unique int per push - avoids comparing Node objects
        heap: list[tuple[float, int, Node]] = [(0.0, next(tiebreak), source)]

        t0 = time.perf_counter()
        while heap:
            d, _, u = heapq.heappop(heap)
            if d > dist.get(u, math.inf):
                continue  # stale heap entry
            for v, w in u.neighbors:
                alt = d + w
                if alt < dist.get(v, math.inf):
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(heap, (alt, next(tiebreak), v))
        elapsed = time.perf_counter() - t0

        return Result(source=source, dist=dist, prev=prev, elapsed=elapsed)

    def run_many(self, sources: list[Node], *, workers: int | None = None) -> list[Result]:
        # parallel Dijkstra from each source using threads; results in input order
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(self.run, src) for src in sources]
        return [f.result() for f in futures]