# Importando as bibliotecas necessárias
import networkx as nx  # Biblioteca para grafos
import numpy as np     # Biblioteca para manipulação de matrizes
import matplotlib.pyplot as plt  # Biblioteca para visualização de gráficos

# Definindo a função para gerar um grafo a partir de uma lista de arestas
def gerar_grafo(arestas):
    G = nx.Graph()  # Criando um objeto NetworkX do tipo Graph
    
    # Iterando através das arestas e adicionando-as ao grafo
    for aresta in arestas:
        if len(aresta) == 2:  # Verificando se a aresta contém dois elementos
            no1, no2 = aresta
            G.add_edge(no1, no2)  # Adicionando a aresta ao grafo
    
    return G  # Retornando o grafo gerado

# Definindo a função para desenhar um grafo
def desenhar_grafo(grafo):
    nx.draw(grafo, with_labels=True)  # Desenhando o grafo com rótulos nos nós
    plt.show()  # Mostrando o desenho do grafo

# Lendo os testes a partir do arquivo "input.txt"
with open('input.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

testes = []       # Lista para armazenar os testes encontrados
teste_atual = []  # Lista temporária para armazenar as arestas do teste atual

# Iterando pelas linhas do arquivo
for linha in linhas:
    if linha.strip():  # Verificando se a linha não está vazia
        aresta = linha.strip().split()  # Dividindo a linha em partes para obter as arestas
        teste_atual.append(aresta)       # Adicionando a aresta ao teste atual
    else:
        if teste_atual:
            testes.append(teste_atual)  # Adicionando o teste atual à lista de testes
            teste_atual = []            # Limpando o teste atual

# Verificando se há um último teste não adicionado
if teste_atual:
    testes.append(teste_atual)

# Executando cada teste e exibindo informações e desenhos
for i, teste in enumerate(testes, start=1):
    grafo_teste = gerar_grafo(teste)  # Gerando o grafo a partir do teste
    
    print(f'Grafo {i}:')
    print(f'Vértices: {grafo_teste.nodes()}')
    print(f'Arestas: {grafo_teste.edges()}')
    
    desenhar_grafo(grafo_teste)  # Desenhando o grafo
