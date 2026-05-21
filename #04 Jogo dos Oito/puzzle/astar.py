"""
astar.py
Busca A* com heurística de distância de Manhattan — método informado, ótimo e eficiente.
"""

import heapq
import time

from puzzle.board import GOAL, get_neighbors, manhattan_distance


def astar(start: tuple) -> dict:
    """
    Seleciona sempre o estado de menor f(n) = g(n) + h(n):
      g(n) = custo real acumulado (número de movimentos)
      h(n) = distância de Manhattan até a meta (heurística admissível)

    Usa lazy deletion para ignorar entradas desatualizadas no heap.

    Retorna dict com: path, nodes (expandidos), depth, time_ms, found.
    """
    if start == GOAL:
        return {"path": [start], "nodes": 0, "depth": 0, "time_ms": 0.0, "found": True}

    t0 = time.perf_counter()

    heap = [(manhattan_distance(start), 0, start)]  # (f, g, estado)
    g_cost = {start: 0}
    parent = {start: None}
    nodes_expanded = 0

    while heap:
        f, g, state = heapq.heappop(heap)

        # Entrada desatualizada — já foi processada com custo menor
        if g > g_cost.get(state, float("inf")):
            continue

        nodes_expanded += 1

        if state == GOAL:
            path = _reconstruct(parent, state)
            elapsed = (time.perf_counter() - t0) * 1000
            return {
                "path": path,
                "nodes": nodes_expanded,
                "depth": len(path) - 1,
                "time_ms": elapsed,
                "found": True,
            }

        for neighbor in get_neighbors(state):
            new_g = g + 1
            if new_g < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = new_g
                parent[neighbor] = state
                heapq.heappush(heap, (new_g + manhattan_distance(neighbor), new_g, neighbor))

    elapsed = (time.perf_counter() - t0) * 1000
    return {"path": [], "nodes": nodes_expanded, "depth": -1, "time_ms": elapsed, "found": False}


def _reconstruct(parent: dict, node: tuple) -> list[tuple]:
    """Reconstrói o caminho do estado inicial até `node`."""
    path = []
    cur = node
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
