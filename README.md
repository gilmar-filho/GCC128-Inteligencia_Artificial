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

[![Assista no YouTube](https://img.youtube.com/vi/xve_7U4ccgQ/0.jpg)](https://www.youtube.com/watch?v=xve_7U4ccgQ)

---

### 🔹 Projeto 4 - Busca (8-Puzzle)
🚧 Em desenvolvimento

---

### 🔹 Projeto 5 - Algoritmos Genéticos
🚧 Em desenvolvimento

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