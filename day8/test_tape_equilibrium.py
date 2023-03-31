import unittest
import tape_equilibrium

class TestTapeEquilibrium(unittest.TestCase):

    def test_solution(self):

        self.assertEqual(tape_equilibrium.solution([3, 1, 2, 4, 3]), 1)
        self.assertEqual(tape_equilibrium.solution([-1000, 1000]), 2000)
        self.assertEqual(tape_equilibrium.solution([5, -5]), 10)
        self.assertEqual(tape_equilibrium.solution([20, 15, 10, 5, 0]), 10)
        self.assertEqual(tape_equilibrium.solution([1, 1, 1, 1, 1]), 1)

        with self.assertRaises(TypeError):
            tape_equilibrium.solution(-1000, 1000)

if __name__ == "__main__":
    unittest.main()