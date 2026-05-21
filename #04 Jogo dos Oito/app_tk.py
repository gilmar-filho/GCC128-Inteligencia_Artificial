"""
app.py
Interface Tkinter do Jogo dos Oito.
O usuário pode jogar manualmente, pedir solução via BFS ou A*,
ou fazer os dois na ordem que quiser.
"""

import tkinter as tk
from tkinter import messagebox

from puzzle.board import GOAL, SIZE, is_solvable
from puzzle.bfs import bfs
from puzzle.astar import astar
from puzzle.game import apply_move, random_state

# Delay entre cada passo da animação da solução (ms)
STEP_DELAY = 400


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo dos Oito — GCC 128 IA")
        self.resizable(False, False)

        self.board = random_state()
        self.moves = 0
        self._solution_steps = []   # fila de estados a animar
        self._animating = False

        self._build_ui()
        self._bind_keys()
        self._refresh()

    # ── Construção da UI ──────────────────────────────────────────────────────

    def _build_ui(self):
        # Tabuleiro: cada peça é um Button clicável
        board_frame = tk.Frame(self, padx=16, pady=16)
        board_frame.pack()

        self._tiles = []
        for i in range(SIZE * SIZE):
            btn = tk.Button(
                board_frame,
                width=4, height=2,
                font=("Helvetica", 28, "bold"),
                relief="raised",
                borderwidth=3,
                command=lambda pos=i: self._click_tile(pos),
            )
            btn.grid(row=i // SIZE, column=i % SIZE, padx=4, pady=4)
            self._tiles.append(btn)

        # Contador de movimentos
        self._status_var = tk.StringVar()
        tk.Label(self, textvariable=self._status_var, font=("Helvetica", 11)).pack()

        # Botões de algoritmo
        algo_frame = tk.Frame(self, pady=8)
        algo_frame.pack()

        tk.Button(
            algo_frame, text="Resolver com BFS", width=18,
            command=lambda: self._solve("BFS"),
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            algo_frame, text="Resolver com A*", width=18,
            command=lambda: self._solve("A*"),
        ).grid(row=0, column=1, padx=6)

        # Resultado do algoritmo
        self._result_var = tk.StringVar()
        tk.Label(self, textvariable=self._result_var, font=("Helvetica", 10), fg="gray").pack()

        # Novo jogo
        tk.Button(
            self, text="Novo jogo", width=20, pady=4,
            command=self._new_game,
        ).pack(pady=(8, 16))

    def _bind_keys(self):
        """
        Setas do teclado movem o número adjacente ao espaço.
        A seta indica a direção em que o número se desloca,
        o que equivale a mover o espaço na direção oposta.
        """
        opposites = {
            "<Up>":    "baixo",
            "<Down>":  "cima",
            "<Left>":  "direita",
            "<Right>": "esquerda",
        }
        for key, direction in opposites.items():
            self.bind(key, lambda e, d=direction: self._move(d))

    # ── Atualização visual ────────────────────────────────────────────────────

    def _refresh(self):
        """Redesenha todas as peças e atualiza o status."""
        for i, btn in enumerate(self._tiles):
            val = self.board[i]
            if val == 0:
                btn.config(text="", bg="#d9d9d9", relief="flat", state="normal")
            else:
                btn.config(text=str(val), bg="white", relief="raised", state="normal")

        if self.board == GOAL:
            self._status_var.set(f"Resolvido em {self.moves} movimentos!")
        else:
            self._status_var.set(f"Movimentos: {self.moves}")

    # ── Ações do jogador ──────────────────────────────────────────────────────

    def _click_tile(self, pos: int):
        """
        O usuário clica em uma peça numerada.
        Se ela for adjacente ao espaço em branco, desliza para lá.
        """
        if self._animating:
            return

        blank = self.board.index(0)

        # Verifica se a peça clicada é vizinha do espaço (mesma linha ou coluna, distância 1)
        row_diff = abs(pos // SIZE - blank // SIZE)
        col_diff = abs(pos % SIZE  - blank % SIZE)
        is_adjacent = (row_diff + col_diff) == 1

        if not is_adjacent:
            return

        # Troca a peça clicada com o espaço em branco
        new_board = list(self.board)
        new_board[blank], new_board[pos] = new_board[pos], new_board[blank]
        self.board = tuple(new_board)
        self.moves += 1
        self._result_var.set("")
        self._refresh()

    def _move(self, direction: str):
        """Move o espaço em branco na direção indicada (usado pelo teclado)."""
        if self._animating:
            return
        new_board = apply_move(self.board, direction)
        if new_board is None:
            return
        self.board = new_board
        self.moves += 1
        self._result_var.set("")
        self._refresh()

    def _new_game(self):
        self._animating = False
        self._solution_steps = []
        self.board = random_state()
        self.moves = 0
        self._result_var.set("")
        self._refresh()

    # ── Solver com animação ───────────────────────────────────────────────────

    def _solve(self, algo: str):
        if self._animating:
            return

        if self.board == GOAL:
            messagebox.showinfo("Jogo dos Oito", "O tabuleiro já está na posição-meta.")
            return

        if not is_solvable(self.board):
            messagebox.showwarning("Jogo dos Oito", "Estado sem solução.")
            return

        fn = bfs if algo == "BFS" else astar
        result = fn(self.board)

        if not result["found"]:
            messagebox.showerror("Jogo dos Oito", "Solução não encontrada.")
            return

        info = (
            f"{algo}: {result['depth']} movimentos · "
            f"{result['nodes']:,} nós · "
            f"{result['time_ms']:.1f} ms"
        )
        self._result_var.set(info)

        # Descarta o primeiro passo (estado atual já exibido)
        self._solution_steps = result["path"][1:]
        self._animating = True
        self._animate_next()

    def _animate_next(self):
        """Avança um passo da solução e agenda o próximo com after()."""
        if not self._solution_steps:
            self._animating = False
            self._refresh()  # garante que o status de vitória seja exibido
            return

        self.board = self._solution_steps.pop(0)
        self.moves += 1
        self._refresh()

        self.after(STEP_DELAY, self._animate_next)


# ── Entrada ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    App().mainloop()