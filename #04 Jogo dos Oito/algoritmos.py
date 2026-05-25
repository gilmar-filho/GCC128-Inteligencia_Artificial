"""
algoritmos.py
Implementação dos dois algoritmos de busca: BFS e A*.

Ambos recebem um estado inicial e retornam um dicionário com:
  - caminho:  lista de estados do início até a meta
  - nos:      número de estados expandidos (medida de esforço)
  - movimentos: número de passos da solução
  - tempo_ms: tempo de execução em milissegundos
  - encontrou: True se a solução foi encontrada
"""

import time
import heapq
from collections import deque

from tabuleiro import ESTADO_META, vizinhos, distancia_manhattan


# ---------------------------------------------------------------------------
# Função auxiliar compartilhada
# ---------------------------------------------------------------------------

def reconstruir_caminho(pai, estado_final):
    """
    Reconstrói a sequência de estados do início até a meta.

    O dicionário 'pai' guarda, para cada estado visitado,
    de qual estado ele veio. Basta seguir esse rastro de volta.
    """
    caminho = []
    estado_atual = estado_final
    while estado_atual is not None:
        caminho.append(estado_atual)
        estado_atual = pai[estado_atual]
    caminho.reverse()  # estava de trás para frente
    return caminho


# ---------------------------------------------------------------------------
# BFS — Busca em Largura
# ---------------------------------------------------------------------------

def bfs(inicio):
    """
    Busca em Largura (Breadth-First Search) — método cego.

    Usa uma fila FIFO: o primeiro estado a entrar é o primeiro a ser examinado.
    Isso garante que os estados mais rasos (menos movimentos) sejam sempre
    processados antes dos mais profundos — logo, a solução encontrada
    é sempre a de menor número de movimentos.

    Não usa nenhuma informação sobre o objetivo: examina estados
    na ordem em que chegam, sem critério de prioridade.
    """
    if inicio == ESTADO_META:
        return {"caminho": [inicio], "nos": 0, "movimentos": 0, "tempo_ms": 0.0, "encontrou": True}

    inicio_tempo = time.perf_counter()

    # fila FIFO: estados aguardando para serem examinados
    fila = deque([inicio])

    # pai[estado] = estado anterior no caminho
    # também serve como "visitados": se está no dicionário, já foi visto
    pai = {inicio: None}

    nos_expandidos = 0

    while fila:
        estado = fila.popleft()  # pega o mais antigo da fila
        nos_expandidos += 1

        for vizinho in vizinhos(estado):
            if vizinho in pai:
                continue  # já visitado, ignora

            pai[vizinho] = estado

            if vizinho == ESTADO_META:
                caminho = reconstruir_caminho(pai, vizinho)
                tempo = (time.perf_counter() - inicio_tempo) * 1000
                return {
                    "caminho": caminho,
                    "nos": nos_expandidos,
                    "movimentos": len(caminho) - 1,
                    "tempo_ms": tempo,
                    "encontrou": True,
                }

            fila.append(vizinho)

    tempo = (time.perf_counter() - inicio_tempo) * 1000
    return {"caminho": [], "nos": nos_expandidos, "movimentos": -1, "tempo_ms": tempo, "encontrou": False}


# ---------------------------------------------------------------------------
# A* — Busca com Heurística
# ---------------------------------------------------------------------------

def a_estrela(inicio):
    """
    Busca A* — método informado.

    A cada passo, escolhe o estado de menor f(n) = g(n) + h(n):
      g(n) = movimentos já realizados para chegar até n
      h(n) = distância de Manhattan de n até a meta (heurística)

    Usa uma fila de prioridade (min-heap) para sempre processar
    o estado mais promissor primeiro.

    Garante a solução ótima porque h(n) é admissível:
    nunca superestima o custo real restante.
    """
    if inicio == ESTADO_META:
        return {"caminho": [inicio], "nos": 0, "movimentos": 0, "tempo_ms": 0.0, "encontrou": True}

    inicio_tempo = time.perf_counter()

    # Fila de prioridade: cada entrada é (f, g, estado)
    # O heap garante que sempre processamos o menor f primeiro
    h_inicial = distancia_manhattan(inicio)
    heap = [(h_inicial, 0, inicio)]  # f = h (g=0 no início)

    # pai[estado] = estado anterior no caminho
    pai = {inicio: None}

    # visitados: estados já expandidos — não precisam ser revisitados
    visitados = set()

    nos_expandidos = 0

    while heap:
        f, g, estado = heapq.heappop(heap)  # estado de menor f

        if estado in visitados:
            continue  # já foi expandido com custo ótimo, ignora
        visitados.add(estado)
        nos_expandidos += 1

        if estado == ESTADO_META:
            caminho = reconstruir_caminho(pai, estado)
            tempo = (time.perf_counter() - inicio_tempo) * 1000
            return {
                "caminho": caminho,
                "nos": nos_expandidos,
                "movimentos": len(caminho) - 1,
                "tempo_ms": tempo,
                "encontrou": True,
            }

        for vizinho in vizinhos(estado):
            if vizinho in visitados:
                continue

            g_vizinho = g + 1  # cada movimento custa 1
            h_vizinho = distancia_manhattan(vizinho)
            f_vizinho = g_vizinho + h_vizinho

            # Só adiciona ao heap se ainda não foi visto por outro caminho
            if vizinho not in pai:
                pai[vizinho] = estado

            heapq.heappush(heap, (f_vizinho, g_vizinho, vizinho))

    tempo = (time.perf_counter() - inicio_tempo) * 1000
    return {"caminho": [], "nos": nos_expandidos, "movimentos": -1, "tempo_ms": tempo, "encontrou": False}
