# Jogo dos Oito - Busca Heurística

Trabalho Prático 04 | GCC128 - Inteligência Artificial | UFLA  
Professores: Ahmed Ali Abdalla Esmin

---

## Sobre o projeto

A ideia do projeto é usar o **Jogo dos Oito** para comparar o uso de algoritmos cegos e informados para a resolução de problemas de busca.
O tabuleiro é uma grade 3×3 com peças numeradas de 1 a 8 e um espaço em branco. O objetivo é atingir o estado-meta abaixo a partir de qualquer configuração inicial válida, movendo uma peça por vez para o espaço vazio.

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

### BFS - Busca em Largura (método cego)

Usa uma fila FIFO (primeiro a entrar, primeiro a sair) para explorar os estados nível a nível: primeiro todos a 1 movimento, depois todos a 2, e assim por diante. Não usa nenhuma informação sobre o objetivo - examina estados na ordem em que chegam, sem critério de prioridade.
Garante a solução de **menor número de movimentos**, mas pode expandir muitos nós.

### A* (método informado)

Seleciona sempre o estado de menor `f(n) = g(n) + h(n)`:
- `g(n)` - movimentos já realizados para chegar até o estado `n`
- `h(n)` - distância de Manhattan até a meta (heurística admissível)

Garante a mesma solução ótima que o BFS, expandindo muito menos nós na prática.

### Distância de Manhattan

Para cada peça, conta quantas linhas + colunas a separam da sua posição-meta, ignorando as demais peças. É **admissível** porque nunca superestima o custo real - cada peça precisaria de pelo menos essa quantidade de movimentos, mesmo sem obstáculos.

---

## Estrutura do projeto

```
#04 Jogo dos Oito/
├── tabuleiro.py   # estado, vizinhos, heurística, resolubilidade, movimentos
├── algoritmos.py  # BFS e A* no mesmo arquivo
├── app_tk.py      # interface gráfica Tkinter
└── README.md
```

`tabuleiro.py` concentra toda a lógica do tabuleiro e não sabe nada de interface ou busca.  
`algoritmos.py` importa apenas de `tabuleiro.py` e não sabe nada de interface.  
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

**Jogar manualmente:** clique em uma peça adjacente ao espaço vazio para movê-la, ou use as setas do teclado (a seta indica a direção em que o número se desloca).

**Resolver com algoritmo:** clique em "Resolver com BFS" ou "Resolver com A\*". O tabuleiro se atualiza passo a passo até atingir a meta. As métricas (movimentos, nós expandidos, tempo) aparecem abaixo dos botões.

**Jogar e depois resolver:** jogue quantos movimentos quiser e acione o algoritmo a qualquer momento - ele resolve a partir do estado atual.

**Novo jogo:** gera um novo estado aleatório e reinicia o contador.