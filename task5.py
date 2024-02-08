import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title = None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

dfs_counter = 0
def dfs_tree_travelsal(root):
    if root:
        global dfs_counter
        dfs_counter += 1
        print(root.val)
        root.color = (0 + 0.15 * dfs_counter, 0 + 0.15 * dfs_counter , 1)
        dfs_tree_travelsal(root.left)
        dfs_tree_travelsal(root.right)

bfs_counter = 0
def bfs_tree_travelsal(root, queue):
    root = queue.popleft()
    global bfs_counter
    bfs_counter += 1
    print(root.val)
    root.color = (0 + 0.15 * bfs_counter, 0 + 0.15 * bfs_counter, 1)
    if root.left:
        queue.append(root.left)
    if root.right:
        queue.append(root.right)
    while queue:
        bfs_tree_travelsal(root, queue)

if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    draw_tree(root)

    print("Tree traversal order with DFS algorithm:")
    dfs_tree_travelsal(root)
    draw_tree(root, "DFS")

    print("Tree traversal order with BFS algorithm:")
    bfs_tree_travelsal(root, deque([root]))
    draw_tree(root, "BFS")