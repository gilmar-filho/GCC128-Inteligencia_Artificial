"""
game.py
Modo jogo: o usuário resolve o puzzle manualmente pelo terminal.
"""

import random

from puzzle.board import GOAL, SIZE, get_neighbors, is_solvable, board_to_str

_DIRECTION_ALIASES = {
    "w": "cima",    "cima":     "cima",
    "s": "baixo",   "baixo":    "baixo",
    "a": "esquerda","esquerda": "esquerda",
    "d": "direita", "direita":  "direita",
}

_MOVE_DELTA = {
    "cima":     -SIZE,
    "baixo":    +SIZE,
    "esquerda": -1,
    "direita":  +1,
}

_BORDER = {
    "esquerda": {0, 3, 6},
    "direita":  {2, 5, 8},
}


def random_state(seed: int | None = None) -> tuple:
    """Gera um estado inicial aleatório e resolúvel."""
    rng = random.Random(seed)
    nums = list(range(9))
    while True:
        rng.shuffle(nums)
        state = tuple(nums)
        if is_solvable(state):
            return state


def apply_move(state: tuple, direction: str) -> tuple | None:
    """
    Aplica um movimento ao estado. Retorna o novo estado ou None se o movimento for inválido.
    O movimento refere-se à direção em que o espaço em branco se desloca.
    """
    blank = state.index(0)
    if direction in _BORDER and blank in _BORDER[direction]:
        return None
    new_pos = blank + _MOVE_DELTA[direction]
    if not (0 <= new_pos < SIZE * SIZE):
        return None
    s = list(state)
    s[blank], s[new_pos] = s[new_pos], s[blank]
    return tuple(s)


def play_terminal(initial_state: tuple | None = None) -> None:
    """Loop principal do modo jogo no terminal."""
    state = initial_state or random_state()
    moves = 0

    print("\n=== JOGO DOS OITO ===")
    print("Mova o espaço em branco com W/A/S/D ou cima/baixo/esquerda/direita.")
    print("Digite 'sair' para encerrar.\n")
    print("Meta:")
    print(board_to_str(GOAL))

    while True:
        print(f"\nMovimentos: {moves}")
        print(board_to_str(state))

        if state == GOAL:
            print(f"\nParabéns! Você resolveu em {moves} movimentos.")
            break

        cmd = input("\nDireção: ").strip().lower()

        if cmd == "sair":
            print("Jogo encerrado.")
            break

        direction = _DIRECTION_ALIASES.get(cmd)
        if direction is None:
            print("Entrada inválida. Use W/A/S/D ou escreva a direção.")
            continue

        new_state = apply_move(state, direction)
        if new_state is None:
            print("Movimento inválido (fora dos limites).")
            continue

        state = new_state
        moves += 1
