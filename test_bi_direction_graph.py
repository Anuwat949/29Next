import unittest
from bi_direction_graph import BiDirectionGraph
from node import Node


class TestBiDirectionGraph(unittest.TestCase):
    def test_get_shortest_path(self):
        """Test on finding the shortest path between two nodes"""
        bi_direct_graph = BiDirectionGraph()
        
        # case: pendant node
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'A', 'B'), 'Path from A to B is A->B, and have cost 5.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'B', 'A'), 'Path from B to A is B->A, and have cost 5.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'C', 'F'), 'Path from C to F is C->G->H->F, and have cost 10.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'F', 'G'), 'Path from F to G is F->H->G, and have cost 8.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'F', 'C'), 'Path from F to C is F->H->G->C, and have cost 10.')

        # case: isolated node
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'A', 'I'), 'Path from A to I is not found.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'B', 'I'), 'Path from B to I is not found.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'I', 'F'), 'Path from I to F is not found.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'I', 'G'), 'Path from I to G is not found.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'F', 'I'), 'Path from F to I is not found.')

        # case: a given node does not exist 
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'A', 'AZ'), 'a given goal node: AZ does not exist')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'X', 'I'), 'a given start node: X does not exist')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'T', 'Q'), 'a given start node: T does not exist')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'F', 'Z'), 'a given goal node: Z does not exist')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'U', 'A'), 'a given start node: U does not exist')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'B', 'R'), 'a given goal node: R does not exist')

        # case: start node = goal node 
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'A', 'A'), 'Path from A to A is A, and have cost 0.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'B', 'B'), 'Path from B to B is B, and have cost 0.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'C', 'C'), 'Path from C to C is C, and have cost 0.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'D', 'D'), 'Path from D to D is D, and have cost 0.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'E', 'E'), 'Path from E to E is E, and have cost 0.')
        self.assertEqual(bi_direct_graph.get_shortest_path('graph.csv', 'I', 'I'), 'Path from I to I is I, and have cost 0.')

    def test_create_graph(self):
        """Test on reading data from a given file"""
        bi_direct_graph = BiDirectionGraph()

        # case: valid file name and path
        self.assertTrue(bi_direct_graph.create_graph('graph.csv'))
        self.assertTrue(bi_direct_graph.create_graph('graph2.csv'))

        # case: a given file does not exist 
        with self.assertRaises(OSError) as exception_context:
            bi_direct_graph.create_graph('graphkjklkljl.csv')
        self.assertEqual(str(exception_context.exception), 'no such file or directory')

        with self.assertRaises(OSError) as exception_context:
            bi_direct_graph.create_graph('graph')
        self.assertEqual(str(exception_context.exception), 'no such file or directory')

        with self.assertRaises(OSError) as exception_context:
            bi_direct_graph.create_graph('invalid_format_input.cs')
        self.assertEqual(str(exception_context.exception), 'no such file or directory')

        # case: data in the given file is not in the incorrect form
        with self.assertRaises(IndexError) as exception_context:
            bi_direct_graph.create_graph('invalid_format.csv')
        self.assertEqual(str(exception_context.exception), 'list index out of range')

        # case: data in the given file is invalid
        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.create_graph('invalid_data.csv')
        self.assertEqual(str(exception_context.exception), 'could not convert data into a graph')

    def test_calc_distance(self):
        """Test on calculating distance between two nodes"""
        bi_direct_graph = BiDirectionGraph()

        # case: valid input nodes
        self.assertEqual(bi_direct_graph.calc_distance(Node('B', 'A', 5),Node('C', 'B', 7)), 12)
        self.assertEqual(bi_direct_graph.calc_distance(Node('C', 'A', 1),Node('D', 'C', 2)), 3)
        self.assertEqual(bi_direct_graph.calc_distance(Node('H', 'A', 12),Node('D', 'H', 2)), 14)
        self.assertEqual(bi_direct_graph.calc_distance(Node('G', 'D', 9),Node('H', 'G', 3)), 12)
        self.assertEqual(bi_direct_graph.calc_distance(Node('H', 'F', 15),Node('G', 'H', 3)), 18)


        # case: two given nodes are not connected to each other 
        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', 5),Node('Z', 'C', 7))
        self.assertEqual(str(exception_context.exception), 'start_node and neighbor_node are not connected')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', 5),Node('Z', None, 7))
        self.assertEqual(str(exception_context.exception), 'start_node and neighbor_node are not connected')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', 5),Node('Z', 'X', 7))
        self.assertEqual(str(exception_context.exception), 'start_node and neighbor_node are not connected')

        # case: not an instance of Node is given as an input
        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(3, Node('Z', 'C', 7))
        self.assertEqual(str(exception_context.exception), 'start_node or neighbor_node is not an instance of Node')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance('A', 3)
        self.assertEqual(str(exception_context.exception), 'start_node or neighbor_node is not an instance of Node')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(None, None)
        self.assertEqual(str(exception_context.exception), 'start_node or neighbor_node is not an instance of Node')

        # case: invalid distance value is given
        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', None),Node('Z', 'A', 7))
        self.assertEqual(str(exception_context.exception), 'indicated distance(s) is not a number')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', 7),Node('Z', 'A', False))
        self.assertEqual(str(exception_context.exception), 'indicated distance(s) is not a number')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', None),Node('Z', 'A', None))
        self.assertEqual(str(exception_context.exception), 'indicated distance(s) is not a number')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', -7),Node('Z', 'A', None))
        self.assertEqual(str(exception_context.exception), 'indicated distance(s) is not a number')

        with self.assertRaises(ValueError) as exception_context:
            bi_direct_graph.calc_distance(Node('A', 'C', -7),Node('Z', 'A', -1))
        self.assertEqual(str(exception_context.exception), 'indicated distance(s) is less than 0')    

    def test_get_all_neighbor_nodes(self):
        """Test on getting neighbor need corresponding to a given node"""
        bi_direct_graph = BiDirectionGraph()

        # case: test key error, not create a graph yet -> should raise an error when trying to access
        with self.assertRaisesRegex(KeyError, 'node: A'):
            bi_direct_graph.get_all_neighbor_nodes('A')

        with self.assertRaisesRegex(KeyError, 'node:  '):
            bi_direct_graph.get_all_neighbor_nodes('')
        
        with self.assertRaisesRegex(KeyError, 'node: Z'):
            bi_direct_graph.get_all_neighbor_nodes('Z')

        # case: graph is created and valid node name is given
        bi_direct_graph.create_graph('graph.csv')
        self.assertEqual(str(bi_direct_graph.get_all_neighbor_nodes('A')), str({'B': Node('B', 'A', 5), 'D':Node('D', 'A', 3), 'E': Node('E', 'A', 4)}))
        self.assertEqual(str(bi_direct_graph.get_all_neighbor_nodes('B')), str({'A': Node('A', 'B', 5), 'C':Node('C', 'B', 4)}))
        self.assertEqual(str(bi_direct_graph.get_all_neighbor_nodes('C')), str({'B': Node('B', 'C', 4), 'G':Node('G', 'C', 2)}))
        self.assertEqual(str(bi_direct_graph.get_all_neighbor_nodes('G')), str({'C': Node('C', 'G', 2), 'D':Node('D', 'G', 6), 'H': Node('H', 'G', 3)}))
        self.assertEqual(str(bi_direct_graph.get_all_neighbor_nodes('I')), str({}))

        # case: graph is created and invalid node name is given
        with self.assertRaisesRegex(KeyError, 'node: Z'):
            bi_direct_graph.get_all_neighbor_nodes('Z')

        with self.assertRaisesRegex(KeyError, 'node: AA'):
            bi_direct_graph.get_all_neighbor_nodes('AA')

        with self.assertRaisesRegex(KeyError, 'node:  '):
            bi_direct_graph.get_all_neighbor_nodes('')


if __name__=='__main__':
    unittest.main()
