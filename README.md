# Repositório de Projetos - GCC128: Inteligência Artificial

Este repositório reúne os projetos desenvolvidos na disciplina **GCC128 - Inteligência Artificial**, da **Universidade Federal de Lavras (UFLA)**.

O foco da disciplina é a aplicação prática de conceitos fundamentais de IA, incluindo algoritmos de classificação, aprendizado de máquina, análise de dados e avaliação de modelos.

---

## 📂 Estrutura do Repositório

### 🔹 Projeto 1 - KNN (K-Nearest Neighbors)

Neste projeto, foi implementado o algoritmo de classificação **K-Nearest Neighbors (KNN)** utilizando o dataset Iris.

Foram desenvolvidas duas abordagens:

- Implementação **manual (hardcore)** do algoritmo  
- Implementação utilizando a biblioteca **Scikit-learn**

### 📊 O que foi feito:
- Pré-processamento dos dados (normalização com StandardScaler)
- Divisão em treino e teste (80/20 com stratify)
- Implementação do KNN do zero
- Avaliação com métricas:
  - Acurácia
  - Precisão
  - Revocação
- Geração de matriz de confusão
- Comparação entre as implementações
- Análise de desempenho (tempo de execução)

📘 O projeto foi desenvolvido em formato de **Jupyter Notebook**, permitindo visualização passo a passo do processo.

### 🎥 Vídeo de apresentação

[![Assista no YouTube](https://img.youtube.com/vi/XwBJordteyo/0.jpg)](https://www.youtube.com/watch?v=XwBJordteyo)

---

### 🔹 Projeto 2 - K-Means Clustering

Neste projeto, desenvolvemos a implementação do algoritmo de agrupamento não supervisionado **K-Means** utilizando o dataset Iris (excluindo a variável alvo durante o treinamento).

Foram desenvolvidas duas abordagens para fins de comparação arquitetural e de desempenho:

- Implementação **manual (hardcore)** do algoritmo do zero
- Implementação utilizando a biblioteca **Scikit-learn**

### 📊 O que foi feito:
- Implementação completa do K-Means (inicialização, atribuição de clusters, atualização de centróides e convergência).
- Testes práticos variando o número de clusters ($k=3$ e $k=5$).
- Avaliação da qualidade dos clusters utilizando a métrica **Silhouette Score**.
- Análise de Desempenho, comparando o tempo de execução (fit e predict) entre a solução manual e a biblioteca consolidada.
- Redução de Dimensionalidade com **PCA** (Análise de Componentes Principais) para 1D e 2D, permitindo a visualização gráfica dos clusters e centróides.
- Validação Externa utilizando uma **Matriz de Contingência (Heatmap)** para cruzar os clusters descobertos matematicamente com as classes reais das espécies.

📘 O projeto foi desenvolvido em formato de **Jupyter Notebook**, permitindo visualização passo a passo do processo.

### 🎥 Vídeo de apresentação

[![Assista no YouTube](https://img.youtube.com/vi/xve_7U4ccgQ/0.jpg)](https://www.youtube.com/watch?v=xve_7U4ccgQ)

---

### 🔹 Projeto 3 - MLPClassifier (Perceptron / Redes Neurais)

Neste projeto, exploramos os conceitos de Redes Neurais Artificiais (*Eager Learning*) através da implementação do algoritmo **Multilayer Perceptron (MLPClassifier)**.

O modelo foi treinado e avaliado em duas bases de dados multiclasse distintas para testar sua capacidade de generalização:
- **Dataset Iris:** Problema com separabilidade quase linear e menor dimensionalidade.
- **Dataset Wine:** Base de dados com maior dimensionalidade (13 atributos químicos) e maior complexidade de padrões não lineares.

### 📊 O que foi feito:
- Divisão dos dados em conjuntos de treino e teste (80/20 com stratify).
- Pré-processamento dos dados com padronização rigorosa (utilizando `StandardScaler`), um passo crítico para a convergência correta dos pesos via descida do gradiente na rede neural.
- Treinamento do classificador `MLPClassifier` da biblioteca **Scikit-learn**.
- Extração de métricas de avaliação do classificador:
  - Acurácia
  - Precisão (Macro)
  - Revocação (Macro)
- Geração e visualização da matriz de confusão.
- **Análise Comparativa** de desempenho entre o modelo baseado em redes neurais (MLP) e o modelo baseado em instâncias (KNN - desenvolvido no Projeto 1).

📘 O projeto foi desenvolvido em formato de **Jupyter Notebook**, acompanhado de um **Relatório Técnico em PDF** com a conclusão detalhada da comparação algorítmica.

### 🎥 Vídeo de apresentação

[![Assista no YouTube](https://img.youtube.com/vi/1n4PkdkJV50/0.jpg)](https://www.youtube.com/watch?v=1n4PkdkJV50)

---

### 🔹 Projeto 4 - Busca (8-Puzzle)

Neste projeto, exploramos a resolução do clássico Jogo dos Oito, comparando algoritmos de busca estruturados aplicados à Inteligência Artificial. Foram implementadas e comparadas duas abordagens distintas de busca para encontrar o caminho mais curto até a meta:

- **Busca Cega:** Algoritmo de Busca em Largura (BFS).
- **Busca Informada:** Algoritmo A* (A-Estrela) utilizando a heurística da Distância de Manhattan.

### 📊 O que foi feito:
- Modelagem do ambiente do jogo em um tabuleiro $3\times3$ com 8 peças numeradas e um espaço vazio.
- Implementação de um verificador de paridade de inversões para garantir que os estados iniciais gerados aleatoriamente possuam solução matemática viável.
- Implementação do algoritmo BFS utilizando uma fila FIFO, realizando uma busca exaustiva nível por nível sem prioridade de estados.
- Implementação do algoritmo A* guiado pela função matemática `f(n)=g(n)+h(n)` para priorizar os caminhos mais promissores.
- Criação da heurística da Distância de Manhattan, contabilizando o deslocamento estimado em linhas e colunas que cada peça precisa andar até sua posição correta.
- Análise de desempenho computacional comparando a complexidade de espaço e a quantidade de nós expandidos, evidenciando o esforço típico de ~50.000 nós na busca cega contra apenas ~200 nós na busca informada.
- Desenvolvimento de uma Interface Gráfica (GUI) utilizando a biblioteca `tkinter`, permitindo jogar manualmente via cliques ou teclado, além de acompanhar a animação passo a passo da resolução feita pelos algoritmos.

📘 O projeto foi desenvolvido de forma modular em **Python** (`app_tk.py`, `algoritmos.py` e `tabuleiro.py`), focado na demonstração visual interativa do funcionamento interno dos algoritmos.

### 🎥 Vídeo de apresentação

[![Assista no YouTube](https://img.youtube.com/vi/1mdwqqZJ9ro/0.jpg)](https://www.youtube.com/watch?v=1mdwqqZJ9ro)

---

### 🔹 Projeto 5 - Algoritmos Genéticos

Neste projeto, aplicamos os conceitos de computação evolutiva através da implementação de um **Algoritmo Genético (AG)** do zero para a otimização de funções matemáticas. O objetivo fundamental foi encontrar o valor máximo (ótimo global) da função quadrática $f(x)=x^{2}-3x+4$ restringindo o espaço de busca ao intervalo contínuo $[-10, +10]$.

### 📊 O que foi feito:
- Implementação completa do pipeline de um Algoritmo Genético em Python.
- Codificação das soluções candidatas (indivíduos) utilizando representação de cromossomos em **vetores binários** de 5 bits, mapeados matematicamente para o domínio real.
- Definição da função de **Aptidão (Fitness)** para avaliar a qualidade de cada indivíduo.
- Construção dos operadores genéticos:
  - **Seleção por Torneio** para priorizar a reprodução dos genes mais fortes mantendo certa diversidade.
  - **Crossover de um ponto** (taxa de 70%) para promover a herança de características promissoras.
  - **Mutação** (taxa de 1% via inversão de bits) para introduzir variação aleatória no ambiente.
- Execução automatizada de uma bateria de testes variando os hiperparâmetros arquiteturais: Tamanho da População (4 e 30 indivíduos) e Número de Gerações (5 e 20 gerações).
- Análise aprofundada dos resultados, comprovando empiricamente a vulnerabilidade de populações pequenas ao fenômeno do **Ótimo Local**, em contraste com a convergência robusta para o **Ótimo Global** gerada pela alta diversidade genética.

📘 O projeto foi desenvolvido em formato de **Jupyter Notebook**, acompanhado de um **Relatório Técnico em PDF** com as conclusões analíticas e tabelas de métricas.

### 🎥 Vídeo de apresentação

[![Assista no YouTube](https://img.youtube.com/vi/vZVfpfUpIM4/0.jpg)](https://www.youtube.com/watch?v=vZVfpfUpIM4)


---

### 🔹 Projeto 6 - Sistemas Multiagentes
🚧 Em desenvolvimento

---

## 🎯 Objetivo

O objetivo deste repositório é consolidar o aprendizado prático em Inteligência Artificial, com foco em:

- Implementação de algoritmos do zero  
- Uso de bibliotecas consolidadas (Scikit-learn)  
- Comparação de desempenho entre abordagens  
- Análise de dados e métricas de avaliação  
- Desenvolvimento de soluções aplicadas  

---

## ⚙️ Tecnologias Utilizadas

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## ▶️ Como Utilizar

1. Clone o repositório:
```bash
git clone https://github.com/gilmar-filho/GCC128-Inteligencia_Artificial.git
cd GCC128-Inteligencia_Artificial
```

2. Abra e execute o arquivo `.ipynb` do projeto desejado.
> Lembre-se de instalar as bibliotecas necessárias para rodar o projeto!

---

## 📌 Observações

- Os projetos são organizados em notebooks para facilitar o entendimento passo a passo.  
- Cada projeto pode ser executado de forma independente.  

---

## 👥 Autores

| [<img src="https://avatars.githubusercontent.com/u/154689201?v=4" width="100px"><br><sub>@gilmar-filho</sub>](https://github.com/gilmar-filho) | [<img src="https://avatars.githubusercontent.com/u/123120658?v=4" width="100px"><br><sub>@SamuVanoni</sub>](https://github.com/SamuVanoni) |
| :---: | :---: |

---

## 📄 Licença

Este projeto é de uso acadêmico.