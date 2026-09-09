from dijkstra import Dijkstra, Node


# Req 1 & 2: starts from a chosen node, ends at a chosen node
def test_simple_path():
    a, b, c = Node("A"), Node("B"), Node("C")
    a.connect(b, 1)
    b.connect(c, 2)

    solver = Dijkstra()
    solver.add_node(a, b, c)
    solver.run(a)

    assert c.path_length == 3
    assert solver.shortest_path(a, c) == [a, b, c]


# Req 3: terminates and returns empty list when no path exists
def test_no_path():
    a, b = Node("A"), Node("B")  # disconnected nodes

    solver = Dijkstra()
    solver.add_node(a, b)
    solver.run(a)

    assert b.path_length == float("inf")
    assert solver.shortest_path(a, b) == []


# Req 4: node can have multiple edges; algorithm picks the shortest
def test_multiple_edges_picks_shortest():
    #        1       5
    #   A ──── B ──── C
    #   └──────────── ┘
    #          3
    a, b, c = Node("A"), Node("B"), Node("C")
    a.connect(b, 1)
    b.connect(c, 5)
    a.connect(c, 3)  # direct shortcut

    solver = Dijkstra()
    solver.add_node(a, b, c)
    solver.run(a)

    assert c.path_length == 3
    assert solver.shortest_path(a, c) == [a, c]


# Req 1 & 2: directed edge — reverse path should not exist
def test_directed_edge_no_reverse():
    a, b = Node("A"), Node("B")
    a.connect(b, 10, directed=True)

    solver = Dijkstra()
    solver.add_node(a, b)

    solver.run(b)
    assert a.path_length == float("inf")  # B cannot reach A


# reset between runs: re-running from a different source gives correct results
def test_reset_between_runs():
    a, b, c = Node("A"), Node("B"), Node("C")
    a.connect(b, 2)
    b.connect(c, 3)

    solver = Dijkstra()
    solver.add_node(a, b, c)

    solver.run(a)
    assert c.path_length == 5

    solver.run(b)
    assert a.path_length == 2             # B→A (undirected, weight 2)
    assert c.path_length == 3             # B→C direct


if __name__ == "__main__":
    test_simple_path()
    test_no_path()
    test_multiple_edges_picks_shortest()
    test_directed_edge_no_reverse()
    test_reset_between_runs()