import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    hpq = [(0, start_vertex)]
    while len(hpq) > 0:
        current_distance, current_vertex = heapq.heappop(hpq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(hpq, (distance, neighbor))
    return distances




if __name__ == "__main__":
    graph = {
    '1': {'2': 5, '8': 10},
    '2': {'1': 5, '8': 3, '3': 1},
    '3': {'2': 1, '9': 2, '4': 5, '6': 4},
    '4': {'3': 5, '5': 2, '6': 4},
    '5': {'4': 2, '6': 3},
    '6': {'3': 4, '4': 4, '5': 3, '7': 2},
    '7': {'6': 2, '8': 1, '9': 5},
    '8': {'1': 10, '2': 3, '7': 1, '9': 6},
    '9': {'3': 2, '7': 5, '8': 6}
    }

    G = nx.Graph()
    for key, value in graph.items():
        for p in value.keys():
            G.add_edge(key, p, weight = value[p])


    # Візуалізація графа
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

   
    print(f"Shortest paths with Dijkstra's algorithm from '1' to all Nodes : {dijkstra(graph, '1')}")
    plt.show()
    
    