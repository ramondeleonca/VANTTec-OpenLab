from dijkstra import Dijkstra, Node


# Req 1 & 2: starts from a chosen node, ends at a chosen node
def test_simple_path():
    a, b, c = Node("A"), Node("B"), Node("C")
    a.connect(b, 1)
    b.connect(c, 2)

    result = Dijkstra().run(a)

    assert result.dist_to(c) == 3
    assert result.path_to(c) == [a, b, c]


# Req 3: terminates and returns empty list when no path exists
def test_no_path():
    a, b = Node("A"), Node("B")  # disconnected nodes

    result = Dijkstra().run(a)

    assert result.dist_to(b) == float("inf")
    assert result.path_to(b) == []


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

    result = Dijkstra().run(a)

    assert result.dist_to(c) == 3
    assert result.path_to(c) == [a, c]


# Req 1 & 2: directed edge — reverse path should not exist
def test_directed_edge_no_reverse():
    a, b = Node("A"), Node("B")
    a.connect(b, 10, directed=True)

    result = Dijkstra().run(b)

    assert result.dist_to(a) == float("inf")  # B cannot reach A


# timing: every Result carries an elapsed field
def test_result_has_elapsed():
    a, b = Node("A"), Node("B")
    a.connect(b, 5)

    result = Dijkstra().run(a)

    assert result.elapsed >= 0.0


# run_many: parallel runs return results in the same order as sources
def test_run_many_order_and_correctness():
    #   A ──1── B ──2── C
    a, b, c = Node("A"), Node("B"), Node("C")
    a.connect(b, 1)
    b.connect(c, 2)

    results = Dijkstra().run_many([a, b, c])

    assert len(results) == 3
    # result[0]: from A
    assert results[0].source is a
    assert results[0].dist_to(c) == 3
    # result[1]: from B
    assert results[1].source is b
    assert results[1].dist_to(c) == 2
    assert results[1].dist_to(a) == 1
    # result[2]: from C (undirected, so can reach A)
    assert results[2].source is c
    assert results[2].dist_to(a) == 3


if __name__ == "__main__":
    test_simple_path()
    test_no_path()
    test_multiple_edges_picks_shortest()
    test_directed_edge_no_reverse()
    test_result_has_elapsed()
    test_run_many_order_and_correctness()