import random
import timeit
import unittest


class Node:
    """Node class used for representing nodes in a network."""

    def __init__(self, name):
        self.name = str(name)

    def __repr__(self):
        return self.name


class BarabasiDirectedNetwork:
    """A class that generates a directed network based on the Erdos-Renyi model."""

    def __init__(self, max_notes: int):
        self.max_notes = max_notes
        self.nodes = []
        self.edges = []

    def generate(self):
        """A Method that generates the edges for the network using the Barabasi-Albert method"""

        # Initial network
        first_node = Node(0)
        second_node = Node(1)
        self.nodes = [first_node, second_node]
        self.edges = [(first_node, second_node)]
        node_current_id = 2

        for i in range(self.max_notes):
            new_node = Node(node_current_id)
            new_edges = []

            #  Generate new edges for each node
            for node in self.nodes:
                if random.random() <= self.calculate_p(node):  # Can you add the node?
                    new_edges.append((new_node, node))
                if len(new_edges) >= self.node_sum * (self.node_sum - 1):
                    break

            self.edges = self.edges + new_edges
            self.nodes.append(new_node)
            node_current_id += 1
        return self.edges

    @property
    def edge_sum(self):
        """Return the sum of all current edges."""
        return len(self.edges)

    @property
    def node_sum(self):
        """Returns the sum of all current nodes."""
        return len(self.nodes)

    def calculate_p(self, target_node):
        """Calculates probability that a new node should have an edge to target node."""
        target_node_edges = 0
        for edge in self.edges:
            if target_node in edge:
                target_node_edges += 1
        return target_node_edges / self.edge_sum


class BarabasiDirectedNetworkUnitTest(unittest.TestCase):
    """A class that runs unitest for the BarabasiDirectedNetwork class."""

    def test_edge_sum(self):
        test_network = BarabasiDirectedNetwork(10)
        test_network.edges += [(1, 2), (2, 3)]
        self.assertEqual(test_network.edge_sum, 2, "Edge sum is not return the sum of edges.")

    def test_node_sum(self):
        test_network = BarabasiDirectedNetwork(10)
        test_network.nodes += [Node("TestNode1"), Node("TestNode2")]
        self.assertEqual(test_network.node_sum, 2, "Edge sum is not return the sum of edges.")

    def test_one_max_node(self):
        test_network = BarabasiDirectedNetwork(1)
        self.assertEqual(len(test_network.generate()), 3, "With max_nodes = 1 there should be 3 edges because p = 1.")

    def test_zero_max_node(self):
        test_network = BarabasiDirectedNetwork(0)
        self.assertEqual(len(test_network.generate()), 1,
                         "With max_nodes = 0 there should be 1 edge because no other edges are added.")

    def test_minus_one_max_node(self):
        test_network = BarabasiDirectedNetwork(-1)
        self.assertEqual(len(test_network.generate()), 1,
                         "With max_nodes = -1 there should be 1 edge because no other edges are added.")

    def test_three_max_node(self):
        test_network = BarabasiDirectedNetwork(2)
        self.assertGreater(len(test_network.generate()), 3, "With max_nodes = 2 there should be more then 3 edges")

    def test_calculate_p(self):
        test_network = BarabasiDirectedNetwork(4)
        test_network.edges = [(1, 2), (1, 0), (2, 3)]
        self.assertAlmostEqual(test_network.calculate_p(1), 2 / 3, 5 ," The outcome of this test should be 2/3.")


print("Time it takes to run a generation: ", timeit.timeit(BarabasiDirectedNetwork(10).generate, number=1))
print(BarabasiDirectedNetwork(2).generate())

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
