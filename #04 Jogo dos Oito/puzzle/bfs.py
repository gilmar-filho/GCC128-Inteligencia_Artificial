"""
bfs.py
Busca em Largura (Breadth-First Search) — método cego, garante solução ótima.
"""

import time
from collections import deque

from puzzle.board import GOAL, get_neighbors


def bfs(start: tuple) -> dict:
    """
    Explora estados nível a nível (fila FIFO).
    Garante o menor número de movimentos por ser completo e ótimo em custo uniforme.

    Retorna dict com: path, nodes (expandidos), depth, time_ms, found.
    """
    if start == GOAL:
        return {"path": [start], "nodes": 0, "depth": 0, "time_ms": 0.0, "found": True}

    t0 = time.perf_counter()

    frontier = deque([start])
    parent = {start: None}   # também serve como conjunto de visitados
    nodes_expanded = 0

    while frontier:
        state = frontier.popleft()
        nodes_expanded += 1

        for neighbor in get_neighbors(state):
            if neighbor in parent:
                continue

            parent[neighbor] = state

            if neighbor == GOAL:
                elapsed = (time.perf_counter() - t0) * 1000
                return {
                    "path": _reconstruct(parent, neighbor),
                    "nodes": nodes_expanded,
                    "depth": len(_reconstruct(parent, neighbor)) - 1,
                    "time_ms": elapsed,
                    "found": True,
                }

            frontier.append(neighbor)

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
