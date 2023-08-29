# Execução do Código de Geração e Visualização de Grafos

Este repositório contém um código em Python para gerar e visualizar grafos a partir de um arquivo de entrada. Os grafos são criados utilizando a biblioteca NetworkX e visualizados com a ajuda da biblioteca Matplotlib.

## Requisitos

Antes de executar o código, você precisa ter as seguintes bibliotecas instaladas:

- NetworkX
- NumPy
- Matplotlib

Você pode instalar as bibliotecas utilizando o seguinte comando:

`pip install networkx numpy matplotlib`

## Como Executar

1. Clone o repositório para o seu sistema.
2. Certifique-se de que o arquivo de entrada "input.txt" esteja no mesmo diretório que o script "main.py".
3. Abra um terminal ou prompt de comando.
4. Navegue até o diretório do repositório.
5. Execute o script "main.py" utilizando o Python: `python3 main.py`

O código irá ler as informações do arquivo "input.txt", gerar os grafos correspondentes e exibir os desenhos de cada grafo.

## Modificando o Grafo

Para modificar o grafo que deseja gerar, abra o arquivo "input.txt" e insira as arestas do grafo. Cada linha representa uma aresta, e os números devem ser separados por espaços.

Exemplo:

1 2  
2 3  
3 4  
4 5  

Isso irá gerar um grafo com 5 nós e as seguintes conexões: 1-2, 2-3, 3-4, 4-5.

Para inserir um outro grafo no mesmo aquivo você pode utilizar a quebra de linha duas vezes e insira os números em seguida.

Exemplo:

1 2  
2 3  

3 4  
4 5  

6 7  
7 8  
8 6  

Após editar o arquivo "input.txt", execute o código novamente para ver as mudanças no desenho do grafo.


