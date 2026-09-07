import heapq
from threading import Thread


class Dijkstra:
    num_threads: int
    threads: list[Thread]

    def __init__(self, num_threads = 4):
        self.num_threads = num_threads
        self.threads = []

class Node:
    pass