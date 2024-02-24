# Um grafo é uma estrutura de dados que consiste em um conjunto
# de vértices (ou nós)
# e um conjunto de arestas que conectam pares de vértices.
#
# Grafos podem ser direcionados (arestas têm uma direção)
# ou não direcionados (arestas não têm uma direção específica).

# Componentes:
# Vértices (Nós): Representam entidades no grafo.
# Arestas: Conexões entre os vértices.

# Implementação de um grafo para representar relacionamento em uma rede social

# Biblioteca: networkx - uma biblioteca para a criação, manipulação e
# estudo da estrutura,
#                        dinâmica e funções de redes complexas.
# pip install networkx

# Biblioteca matplotlib - É uma biblioteca de visualização que é
# utilizada para exibir o grafo.
# pip install matplotlib
import matplotlib.pyplot as plt
import networkx as nx

# Cria um grafo direcionado (DiGraph) vazio.
Grafo = nx.DiGraph()
usuarios = ["Alice", "Bob", "Carol", "Dave", "Eva"]

# Adicionar os Nós no Grafo
Grafo.add_nodes_from(usuarios)

# Criar um Lista de Amizades
amizades = [("Alice", "Bob"), ("Bob", "Carol"),
            ("Carol", "Dave"), ("Dave", "Eva"), ("Bob", "Eva")]

# Adicionar as Arestas no Grafo
Grafo.add_edges_from(amizades)

# Definir o formato do Nó (circular)
formato = nx.circular_layout(Grafo)

# x.draw(...): Desenha o grafo com vários parâmetros de estilo.
nx.draw(Grafo, formato, with_labels=True, arrows=True, node_size=800,
        node_color="lightblue", font_size=10, font_color="black",
        font_weight="bold", width=2)
plt.title("Rede de Amizades")
plt.show()
