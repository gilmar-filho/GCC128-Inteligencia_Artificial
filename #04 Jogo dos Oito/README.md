# Jogo dos Oito — Busca Heurística

Trabalho Prático 04 · GCC 128 – Inteligência Artificial · UFLA  
Professores: Ahmed Ali Abdalla Esmin · Anna Paula Figueiredo

---

## Sobre o projeto

Implementação do **8-puzzle** com dois algoritmos de busca e interface gráfica interativa.

O tabuleiro é uma grade 3×3 com peças numeradas de 1 a 8 e um espaço em branco.
O objetivo é atingir o estado-meta abaixo a partir de qualquer configuração inicial válida,
movendo o espaço em branco nas quatro direções cardinais.

```
Estado-meta:
 1 | 2 | 3
-----------
 8 |   | 4
-----------
 7 | 6 | 5
```

---

## Algoritmos implementados

### BFS — Busca em Largura (método cego)
Explora os estados nível a nível usando uma fila FIFO.  
Garante a solução de **menor número de movimentos**, mas pode expandir muitos nós.

### A* (método informado)
Seleciona sempre o estado de menor `f(n) = g(n) + h(n)`:
- `g(n)` — movimentos realizados até o estado `n`
- `h(n)` — distância de Manhattan até a meta (heurística admissível)

Garante a mesma solução ótima que BFS, expandindo muito menos nós na prática.

### Distância de Manhattan
Para cada peça, conta quantas linhas + colunas a separam da sua posição-meta,
ignorando as demais peças. É **admissível** (nunca superestima) e **consistente**.

---

## Estrutura do projeto

```
8puzzle/
├── puzzle/
│   ├── board.py    # estado, vizinhos, resolubilidade, heurística
│   ├── bfs.py      # algoritmo BFS
│   ├── astar.py    # algoritmo A*
│   └── game.py     # lógica do modo jogo (movimentos, estado aleatório)
├── app_tk.py          # interface gráfica Tkinter
└── README.md
```

Cada módulo em `puzzle/` tem responsabilidade única e não importa nada de interface.  
`app_tk.py` apenas orquestra — zero lógica de busca nele.

---

## Pré-requisitos

- Python 3.10 ou superior
- Tkinter (incluso na instalação padrão do Python)

Em sistemas Linux onde o Tkinter não esteja disponível:

```bash
sudo apt install python3-tk
```

---

## Como executar

```bash
cd GCC128-Inteligencia_Artificial/\#04\ Jogo\ dos\ Oito
python app_tk.py
```

---

## Como usar

O jogo começa com um estado aleatório já na tela.

**Jogar manualmente:** use as setas do teclado para mover o espaço em branco.

**Resolver com algoritmo:** clique em "Resolver com BFS" ou "Resolver com A\*". O tabuleiro se atualiza passo a passo até atingir a meta. As métricas (movimentos, nós expandidos, tempo) aparecem abaixo dos botões.

**Jogar e depois resolver:** jogue quantos movimentos quiser e acione o algoritmo a qualquer momento — ele resolve a partir do estado atual.

**Novo jogo:** gera um novo estado aleatório e reinicia o contador.

---

## Notas sobre resolubilidade

O espaço de estados do 8-puzzle divide-se em **dois conjuntos disjuntos**:
metade dos estados alcança a meta, a outra metade não.

A condição usada: a paridade do número de inversões do estado inicial deve ser
**igual** à paridade das inversões do estado-meta.
O estado-meta adotado possui 7 inversões (ímpar), portanto apenas estados com
número ímpar de inversões são resolúveis em relação a ele.
