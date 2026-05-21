"""
board.py
Representação do tabuleiro, geração de vizinhos e verificação de resolubilidade.
"""

SIZE = 3

# Estado-meta adotado pelo enunciado
GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

# Deslocamento de índice para cada direção
_MOVES = {
    "cima":     -SIZE,
    "baixo":    +SIZE,
    "esquerda": -1,
    "direita":  +1,
}

# Posições onde o espaço não pode se mover para esquerda/direita (evita quebra de linha)
_BORDER = {
    "esquerda": {0, 3, 6},
    "direita":  {2, 5, 8},
}

# Posição-meta de cada peça: {valor: (linha, coluna)}
GOAL_POSITIONS = {val: divmod(i, SIZE) for i, val in enumerate(GOAL)}

# Paridade das inversões do estado-meta (usada em is_solvable)
def _count_inversions(state: tuple) -> int:
    nums = [n for n in state if n != 0]
    return sum(1 for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] > nums[j])

_GOAL_PARITY = _count_inversions(GOAL) % 2


def get_neighbors(state: tuple) -> list[tuple]:
    """Retorna todos os estados alcançáveis em um único movimento."""
    neighbors = []
    blank = state.index(0)

    for direction, delta in _MOVES.items():
        if direction in _BORDER and blank in _BORDER[direction]:
            continue
        new_pos = blank + delta
        if 0 <= new_pos < SIZE * SIZE:
            s = list(state)
            s[blank], s[new_pos] = s[new_pos], s[blank]
            neighbors.append(tuple(s))

    return neighbors


def is_solvable(state: tuple) -> bool:
    """
    Um estado é resolúvel quando a paridade das suas inversões
    é igual à paridade das inversões do estado-meta.
    """
    return _count_inversions(state) % 2 == _GOAL_PARITY


def manhattan_distance(state: tuple) -> int:
    """Soma das distâncias de Manhattan de cada peça até sua posição-meta."""
    total = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        cur_row, cur_col = divmod(i, SIZE)
        goal_row, goal_col = GOAL_POSITIONS[val]
        total += abs(cur_row - goal_row) + abs(cur_col - goal_col)
    return total


def board_to_str(state: tuple) -> str:
    """Formata o tabuleiro como string para exibição em terminal."""
    lines = []
    for row in range(SIZE):
        cells = []
        for col in range(SIZE):
            val = state[row * SIZE + col]
            cells.append(f" {val if val != 0 else ' '} ")
        lines.append("|".join(cells))
        if row < SIZE - 1:
            lines.append("-" * (SIZE * 4 - 1))
    return "\n".join(lines)
