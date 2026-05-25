"""
app_tk.py
Interface gráfica do Jogo dos Oito.
O usuário pode jogar manualmente, pedir solução via BFS ou A*,
ou fazer os dois na ordem que quiser.
"""

import tkinter as tk
from tkinter import messagebox

from tabuleiro import ESTADO_META, TAMANHO, tem_solucao, estado_aleatorio, mover_peca, mover_teclado
from algoritmos import bfs, a_estrela

# Delay entre cada passo da animação da solução (ms)
DELAY_ANIMACAO = 400


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo dos Oito — GCC 128 IA")
        self.resizable(False, False)

        self.tabuleiro = estado_aleatorio()
        self.movimentos = 0
        self._passos_solucao = []   # fila de estados a animar
        self._animando = False

        self._construir_interface()
        self._configurar_teclado()
        self._atualizar()

    # ── Construção da interface ───────────────────────────────────────────────

    def _construir_interface(self):
        # Tabuleiro: cada peça é um botão clicável
        frame_tabuleiro = tk.Frame(self, padx=16, pady=16)
        frame_tabuleiro.pack()

        self._pecas = []
        for i in range(TAMANHO * TAMANHO):
            btn = tk.Button(
                frame_tabuleiro,
                width=4, height=2,
                font=("Helvetica", 28, "bold"),
                relief="raised",
                borderwidth=3,
                command=lambda pos=i: self._clicar_peca(pos),
            )
            btn.grid(row=i // TAMANHO, column=i % TAMANHO, padx=4, pady=4)
            self._pecas.append(btn)

        # Contador de movimentos
        self._var_status = tk.StringVar()
        tk.Label(self, textvariable=self._var_status, font=("Helvetica", 11)).pack()

        # Botões de algoritmo
        frame_algoritmos = tk.Frame(self, pady=8)
        frame_algoritmos.pack()

        tk.Button(
            frame_algoritmos, text="Resolver com BFS", width=18,
            command=lambda: self._resolver("BFS"),
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            frame_algoritmos, text="Resolver com A*", width=18,
            command=lambda: self._resolver("A*"),
        ).grid(row=0, column=1, padx=6)

        # Resultado do algoritmo
        self._var_resultado = tk.StringVar()
        tk.Label(self, textvariable=self._var_resultado, font=("Helvetica", 10), fg="gray").pack()

        # Novo jogo
        tk.Button(
            self, text="Novo jogo", width=20, pady=4,
            command=self._novo_jogo,
        ).pack(pady=(8, 16))

    def _configurar_teclado(self):
        """
        Setas do teclado movem o número adjacente para o espaço vazio.
        A seta indica a direção em que o número se desloca —
        o espaço se move na direção oposta.
        """
        opostos = {
            "<Up>":    "baixo",
            "<Down>":  "cima",
            "<Left>":  "direita",
            "<Right>": "esquerda",
        }
        for tecla, direcao in opostos.items():
            self.bind(tecla, lambda e, d=direcao: self._mover_teclado(d))

    # ── Atualização visual ────────────────────────────────────────────────────

    def _atualizar(self):
        """Redesenha todas as peças e atualiza o contador de movimentos."""
        for i, btn in enumerate(self._pecas):
            valor = self.tabuleiro[i]
            if valor == 0:
                btn.config(text="", bg="#d9d9d9", relief="flat", state="normal")
            else:
                btn.config(text=str(valor), bg="white", relief="raised", state="normal")

        if self.tabuleiro == ESTADO_META:
            self._var_status.set(f"Resolvido em {self.movimentos} movimentos!")
        else:
            self._var_status.set(f"Movimentos: {self.movimentos}")

    # ── Ações do jogador ──────────────────────────────────────────────────────

    def _clicar_peca(self, posicao):
        """
        O usuário clica em uma peça numerada.
        Se ela for adjacente ao espaço em branco, desliza para lá.
        """
        if self._animando:
            return

        novo = mover_peca(self.tabuleiro, posicao)
        if novo is None:
            return  # peça não é adjacente ao espaço, ignora

        self.tabuleiro = novo
        self.movimentos += 1
        self._var_resultado.set("")
        self._atualizar()

    def _mover_teclado(self, direcao):
        """Move o espaço em branco na direção indicada pelo teclado."""
        if self._animando:
            return

        novo = mover_teclado(self.tabuleiro, direcao)
        if novo is None:
            return

        self.tabuleiro = novo
        self.movimentos += 1
        self._var_resultado.set("")
        self._atualizar()

    def _novo_jogo(self):
        self._animando = False
        self._passos_solucao = []
        self.tabuleiro = estado_aleatorio()
        self.movimentos = 0
        self._var_resultado.set("")
        self._atualizar()

    # ── Resolução com animação ────────────────────────────────────────────────

    def _resolver(self, algoritmo):
        if self._animando:
            return

        if self.tabuleiro == ESTADO_META:
            messagebox.showinfo("Jogo dos Oito", "O tabuleiro já está na posição-meta.")
            return

        if not tem_solucao(self.tabuleiro):
            messagebox.showwarning("Jogo dos Oito", "Estado sem solução.")
            return

        # Executa o algoritmo escolhido a partir do estado atual
        fn = bfs if algoritmo == "BFS" else a_estrela
        resultado = fn(self.tabuleiro)

        if not resultado["encontrou"]:
            messagebox.showerror("Jogo dos Oito", "Solução não encontrada.")
            return

        info = (
            f"{algoritmo}: {resultado['movimentos']} movimentos · "
            f"{resultado['nos']:,} nós · "
            f"{resultado['tempo_ms']:.1f} ms"
        )
        self._var_resultado.set(info)

        # Descarta o primeiro estado (tabuleiro atual já está na tela)
        self._passos_solucao = resultado["caminho"][1:]
        self._animando = True
        self._animar_proximo()

    def _animar_proximo(self):
        """
        Avança um passo da solução e agenda o próximo com after().
        after() é não-bloqueante: a janela permanece responsiva durante a animação.
        """
        if not self._passos_solucao:
            self._animando = False
            self._atualizar()  # exibe a mensagem de vitória ao final
            return

        self.tabuleiro = self._passos_solucao.pop(0)
        self.movimentos += 1
        self._atualizar()

        self.after(DELAY_ANIMACAO, self._animar_proximo)


# ── Ponto de entrada ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    App().mainloop()
