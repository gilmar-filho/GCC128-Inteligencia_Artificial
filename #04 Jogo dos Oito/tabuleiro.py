"""
tabuleiro.py
Representa o estado do tabuleiro e contém as funções de apoio
usadas pelos dois algoritmos de busca.
"""

import random

# O tabuleiro é uma tupla de 9 números (leitura linha por linha).
# O valor 0 representa o espaço em branco.
# Exemplo: (1, 2, 3, 8, 0, 4, 7, 6, 5) é o estado-meta.

TAMANHO = 3  # grade 3x3

ESTADO_META = (1, 2, 3,
               8, 0, 4,
               7, 6, 5)

# Posição-meta de cada peça: {valor: (linha, coluna)}
# Usada para calcular a distância de Manhattan sem remontar o estado-meta a cada chamada.
POSICAO_META = {}
for i, valor in enumerate(ESTADO_META):
    linha = i // TAMANHO
    coluna = i % TAMANHO
    POSICAO_META[valor] = (linha, coluna)


# ---------------------------------------------------------------------------
# Geração de estados vizinhos
# ---------------------------------------------------------------------------

def vizinhos(estado):
    """
    Retorna todos os estados alcançáveis a partir de 'estado' em um único movimento.

    O espaço em branco pode se mover para cima, baixo, esquerda ou direita,
    desde que não saia dos limites do tabuleiro.
    """
    resultado = []
    espaco = estado.index(0)  # posição atual do espaço em branco

    linha_espaco = espaco // TAMANHO
    coluna_espaco = espaco % TAMANHO

    # Cada movimento é definido pelo deslocamento de índice e pela verificação de borda
    movimentos = []

    if linha_espaco > 0:              # pode mover para cima
        movimentos.append(espaco - TAMANHO)
    if linha_espaco < TAMANHO - 1:   # pode mover para baixo
        movimentos.append(espaco + TAMANHO)
    if coluna_espaco > 0:             # pode mover para esquerda
        movimentos.append(espaco - 1)
    if coluna_espaco < TAMANHO - 1:  # pode mover para direita
        movimentos.append(espaco + 1)

    for nova_posicao in movimentos:
        # Cria o novo estado trocando o espaço com a peça adjacente
        novo = list(estado)
        novo[espaco], novo[nova_posicao] = novo[nova_posicao], novo[espaco]
        resultado.append(tuple(novo))

    return resultado


# ---------------------------------------------------------------------------
# Heurística: distância de Manhattan
# ---------------------------------------------------------------------------

def distancia_manhattan(estado):
    """
    Calcula h(n): estimativa do custo restante até a meta.

    Para cada peça, soma quantas linhas + colunas ela ainda precisa
    percorrer para chegar à sua posição correta no estado-meta.

    É admissível: nunca superestima o custo real, pois ignora
    as outras peças e conta apenas o caminho mínimo individual.
    """
    total = 0
    for i, valor in enumerate(estado):
        if valor == 0:
            continue  # o espaço em branco não tem posição-meta

        linha_atual = i // TAMANHO
        coluna_atual = i % TAMANHO

        linha_meta, coluna_meta = POSICAO_META[valor]

        total += abs(linha_atual - linha_meta) + abs(coluna_atual - coluna_meta)

    return total


# ---------------------------------------------------------------------------
# Verificação de resolubilidade
# ---------------------------------------------------------------------------

def contar_inversoes(estado):
    """
    Conta o número de inversões em um estado.

    Uma inversão ocorre quando uma peça de valor maior aparece
    antes de uma peça de valor menor na sequência linear do tabuleiro
    (ignorando o espaço em branco).
    """
    pecas = [v for v in estado if v != 0]
    inversoes = 0
    for i in range(len(pecas)):
        for j in range(i + 1, len(pecas)):
            if pecas[i] > pecas[j]:
                inversoes += 1
    return inversoes


# A paridade do estado-meta determina quais estados iniciais têm solução.
# Estados com a mesma paridade de inversões que a meta são resolúveis.
PARIDADE_META = contar_inversoes(ESTADO_META) % 2


def tem_solucao(estado):
    """
    Retorna True se o estado tem solução.

    O espaço de estados do 8-puzzle divide-se em dois grupos disjuntos:
    metade dos estados alcança a meta, a outra metade não.
    A condição é que a paridade das inversões do estado inicial
    seja igual à paridade das inversões do estado-meta.
    """
    return contar_inversoes(estado) % 2 == PARIDADE_META


# ---------------------------------------------------------------------------
# Geração de estado aleatório
# ---------------------------------------------------------------------------

def estado_aleatorio():
    """Embaralha as peças e garante que o estado gerado tem solução."""
    pecas = list(range(9))
    while True:
        random.shuffle(pecas)
        estado = tuple(pecas)
        if tem_solucao(estado):
            return estado


# ---------------------------------------------------------------------------
# Movimento de uma peça (usado pelo app_tk.py)
# ---------------------------------------------------------------------------

def mover_peca(estado, posicao_clicada):
    """
    O usuário clica em uma peça. Se ela for adjacente ao espaço em branco,
    ela desliza para lá. Retorna o novo estado ou None se o movimento for inválido.
    """
    espaco = estado.index(0)

    linha_espaco   = espaco // TAMANHO
    coluna_espaco  = espaco % TAMANHO
    linha_clicada  = posicao_clicada // TAMANHO
    coluna_clicada = posicao_clicada % TAMANHO

    # A peça deve ser adjacente ao espaço (distância de Manhattan = 1)
    distancia = abs(linha_clicada - linha_espaco) + abs(coluna_clicada - coluna_espaco)
    if distancia != 1:
        return None

    novo = list(estado)
    novo[espaco], novo[posicao_clicada] = novo[posicao_clicada], novo[espaco]
    return tuple(novo)


# ---------------------------------------------------------------------------
# Movimento pelo teclado (usado pelo app_tk.py)
# ---------------------------------------------------------------------------

def mover_teclado(estado, direcao):
    """
    Move o espaço em branco na direção indicada.
    'direcao' é a direção em que o espaço se desloca.
    Retorna o novo estado ou None se o movimento for inválido.
    """
    espaco = estado.index(0)
    linha = espaco // TAMANHO
    coluna = espaco % TAMANHO

    if direcao == "cima"     and linha > 0:
        nova_posicao = espaco - TAMANHO
    elif direcao == "baixo"  and linha < TAMANHO - 1:
        nova_posicao = espaco + TAMANHO
    elif direcao == "esquerda" and coluna > 0:
        nova_posicao = espaco - 1
    elif direcao == "direita"  and coluna < TAMANHO - 1:
        nova_posicao = espaco + 1
    else:
        return None

    novo = list(estado)
    novo[espaco], novo[nova_posicao] = novo[nova_posicao], novo[espaco]
    return tuple(novo)
