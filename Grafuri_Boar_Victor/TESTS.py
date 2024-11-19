import unittest
from FUNCTIONS import Functions
from REPOSITORY import Repository

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Initialize Functions and Repository objects
        self.repository = Repository("test_graph.txt")
        self.functions = Functions(self.repository)

    def test_print_the_number_of_vertices(self):
        # Test printing the number of vertices
        self.repository.vertices_number = 5
        self.assertEqual(self.functions.print_the_number_of_vertices(), 5)

    def test_print_all_vertices(self):
        # Test printing all vertices
        self.repository.vertices_out = {0: [1, 2], 1: [0], 2: []}
        expected_output = {0: [1, 2], 1: [0], 2: []}
        self.assertEqual(self.functions.print_all_vertices(), expected_output)

    def test_find_an_edge_between_two_vertices(self):
        # Test finding an edge between two vertices
        self.repository.vertices_out = {0: [1], 1: [0], 2: []}
        self.assertTrue(self.functions.find_an_edge_between_two_vertices(0, 1))
        self.assertFalse(self.functions.find_an_edge_between_two_vertices(0, 2))

    def test_find_the_in_degree_and_the_out_degree_of_a_specified_vertex(self):
        # Test finding the in-degree and out-degree of a specified vertex
        self.repository.vertices_in = {0: [1], 1: [0]}
        self.repository.vertices_out = {0: [1], 1: []}
        self.assertEqual(self.functions.find_the_in_degree_and_the_out_degree_of_a_specified_vertex(0), (1, 1))

    def test_print_all_out_edges_for_a_specified_vertex(self):
        # Test printing all out-edges for a specified vertex
        self.repository.vertices_out = {0: [1, 2], 1: [0], 2: []}
        self.assertEqual(self.functions.print_all_out_edges_for_a_specified_vertex(0), [1, 2])

    def test_print_all_in_edges_for_a_specified_vertex(self):
        # Test printing all in-edges for a specified vertex
        self.repository.vertices_in = {0: [1,2], 1: [0], 2: [0]}
        self.assertEqual(self.functions.print_all_in_edges_for_a_specified_vertex(0), [1, 2])

    def test_modify_the_cost_of_the_edge(self):
        # Test modifying the cost of an edge
        self.repository.costs = {(0, 1): 10, (1, 2): 20}
        self.functions.modify_the_cost_of_the_edge(0, 1, 15)
        self.assertEqual(self.repository.costs[(0, 1)], 15)

    def test_delete_a_specified_vertex(self):
        # Test deleting a specified vertex
        self.repository.vertices_out = {0: [1], 1: []}
        self.repository.vertices_in = {0: [], 1: [0]}
        self.repository.costs = {(0, 1): 10}
        self.functions.delete_a_specified_vertex(0)
        self.assertNotEqual({0: [1], 1: []}, self.repository.vertices_out)
        self.assertNotEqual({0: [], 1: [0]}, self.repository.vertices_in)
        self.assertNotEqual((0, 1), self.repository.costs)

    def test_delete_a_specified_edge(self):
        # Test deleting a specified edge
        self.repository.vertices_out = {0: [1], 1: []}
        self.repository.vertices_in = {0: [], 1: [0]}
        self.repository.costs = {(0, 1): 10}
        self.functions.delete_a_specified_edge(0, 1)
        self.assertNotIn(1, self.repository.vertices_out[0])
        self.assertNotIn(0, self.repository.vertices_in[1])
        self.assertNotIn((0, 1), self.repository.costs)

    def test_random_graph(self):
        # Test generating a random graph
        self.functions.random_graph(5, 7)
        self.assertEqual(len(self.repository.vertices_out), 5)
        self.assertEqual(len(self.repository.vertices_in), 5)
        self.assertTrue(len(self.repository.costs) >= 4)

    def tearDown(self):
        # Clean up after each test
        self.repository = None
        self.functions = None

if __name__ == "_main_":
   unittest.main()