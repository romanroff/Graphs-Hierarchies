import matplotlib.pyplot as plt
import networkit as nk
import networkx as nx
import random

class GraphGenerator:
    def __init__(self):
        self.graph = None

    def generate_graph(self, graph_type, **kwargs):
        """

        Генерирует граф заданного типа с использованием параметров из kwargs.

        Пример:
        >>> graph_generator.generate_graph("complete", n=10)
        >>> graph_generator.generate_graph("erdos_renyi", n=20, p=0.3)
        >>> graph_generator.generate_graph("watts_strogatz", n=30, k=4, p=0.1, weight=True)

        """
        if graph_type == "complete":
            self.graph = nx.complete_graph(kwargs.get("n", 10))
        elif graph_type == "path":
            self.graph = nx.path_graph(kwargs.get("n", 10))
        elif graph_type == "cycle":
            self.graph = nx.cycle_graph(kwargs.get("n", 10))
        elif graph_type == "star":
            self.graph = nx.star_graph(kwargs.get("n", 10))
        elif graph_type == "wheel":
            self.graph = nx.wheel_graph(kwargs.get("n", 10))
        elif graph_type == "erdos_renyi":
            self.graph = nx.erdos_renyi_graph(kwargs.get("n", 10), kwargs.get("p", 0.5))
        elif graph_type == "barabasi_albert":
            self.graph = nx.barabasi_albert_graph(kwargs.get("n", 10), kwargs.get("m", 2))
        elif graph_type == "watts_strogatz":
            self.graph = nx.watts_strogatz_graph(kwargs.get("n", 10), kwargs.get("k", 2), kwargs.get("p", 0.5))
        elif graph_type == "balanced_tree":
            self.graph = nx.balanced_tree(kwargs.get("r", 2), kwargs.get("h", 3))
        elif graph_type == "turan":
            self.graph = nx.turan_graph(kwargs.get("n", 10), kwargs.get("r", 2))
        elif graph_type == "gnm_random":
            self.graph = nx.gnm_random_graph(kwargs.get("n", 10), kwargs.get("m", 20))
        elif graph_type == "random_regular":
            self.graph = nx.random_regular_graph(kwargs.get("d", 3), kwargs.get("n", 10))
        elif graph_type == "small_world":
            self.graph = nx.connected_watts_strogatz_graph(kwargs.get("n", 10), kwargs.get("k", 2), kwargs.get("p", 0.5))
        elif graph_type == "grid_2d":
            self.graph = nx.grid_2d_graph(kwargs.get("m", 5), kwargs.get("n", 5))
        elif graph_type == "hexagonal_lattice":
            self.graph = nx.hexagonal_lattice_graph(kwargs.get("m", 2), kwargs.get("n", 2))
        else:
            raise ValueError(f"Unknown graph type: {graph_type}")

        # Если требуются веса для ребер, можно добавить их здесь
        if kwargs.get("weighted", False):
            for u, v in self.graph.edges():
                self.graph.edges[u, v]['weight'] = random.randint(1, 100)

    def get_graph(self):
        """Возвращает сгенерированный граф."""
        return self.graph
    
class HierarchicalGraph:
    def __init__(self, graph):
        self.graph = graph
        self.graph_dict = self.create_graph_dict()

    def create_graph_dict(self):
        """Создает словарь графа."""
        return {node: list(self.graph.neighbors(node)) for node in self.graph.nodes()}

    def find_path(self, node1, node2):
        """Ищет кратчайший путь между двумя узлами."""
        nk_graph = nk.nxadapter.nx2nk(self.graph, weightAttr='weight')
        dijkstra = nk.distance.Dijkstra(nk_graph, node1, True, False, node2)
        dijkstra.run()
        
        path = dijkstra.getPath(node2)
        if path:
            return path
        else:
            return None

    def draw_graph(self, edge_labels=False, figsize=(10, 10)):
        """Рисует начальный граф с метками узлов и ребер."""
        plt.figure(figsize=figsize)
        # if nx.check_planarity(self.graph)[0]:
        #     pos = nx.planar_layout(self.graph, )
        # else:
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        
        # Метки узлов
        node_labels = {node: str(node) for node in self.graph.nodes()}
        nx.draw_networkx_labels(self.graph, pos, labels=node_labels)
        
        # Метки ребер
        if edge_labels:
            edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in self.graph.edges(data=True)}
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        
        plt.show()

    def draw_route(self, node1, node2, edge_labels=False, figsize=(10, 10)):
        """Рисует маршрут между двумя точками."""
        path = self.find_path(node1, node2)
        
        if path:
            plt.figure(figsize=figsize)
            # if nx.check_planarity(self.graph)[0]:
            #     pos = nx.planar_layout(self.graph)
            # else:
            pos = nx.spring_layout(self.graph, seed=42)
            nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
            
            # Рисование пути
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='red')

            if edge_labels:
                edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in self.graph.edges(data=True)}
                nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
            
            plt.show()
        else:
            print(f"No path found between node {node1} and node {node2}")