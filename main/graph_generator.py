import networkx as nx
import random

class GraphGenerator:
    def __init__(self):
        self.graph = None

    def generate_graph(self, graph_type, **kwargs):
        """Генерирует граф заданного типа с использованием параметров из kwargs."""
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

if __name__ == "__main__":
    # Пример использования
    graph_generator = GraphGenerator()

    # Генерация полного графа с 10 узлами
    graph_generator.generate_graph("complete", n=10)
    complete_graph = graph_generator.get_graph()

    # Генерация графа Эрдёша-Реньи с 20 узлами и вероятностью p=0.3
    graph_generator.generate_graph("erdos_renyi", n=20, p=0.3)
    erdos_renyi_graph = graph_generator.get_graph()

    # Генерация графа Ваттса-Строгаца с 30 узлами, степенью каждого узла 4 и вероятностью перемешивания 0.1
    graph_generator.generate_graph("watts_strogatz", n=30, k=4, p=0.1)
    watts_strogatz_graph = graph_generator.get_graph()