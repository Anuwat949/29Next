
import unittest
import app

class TestApp(unittest.TestCase):
    def test_get_shortest_routes(self):
        self.assertEqual(app.get_shortest_route('graph.csv','A','B'), 'Path from A to B is A->B, and have cost 5.')
        self.assertEqual(app.get_shortest_route('graph.csv','B','A'), 'Path from B to A is B->A, and have cost 5.')
        self.assertEqual(app.get_shortest_route('graph.csv','C','F'), 'Path from C to F is C->G->H->F, and have cost 10.')
        self.assertEqual(app.get_shortest_route('graph.csv','F','G'), 'Path from F to G is F->H->G, and have cost 8.')
        self.assertEqual(app.get_shortest_route('graph.csv','F','C'), 'Path from F to C is F->H->G->C, and have cost 10.')


if __name__=='__main__':
    unittest.main()
